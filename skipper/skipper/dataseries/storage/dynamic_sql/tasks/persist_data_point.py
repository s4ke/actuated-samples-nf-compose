# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. 
# If a copy of the MPL was not distributed with this file, 
# You can obtain one at https://mozilla.org/MPL/2.0/.
# This file is part of NF Compose
# [2019] - [2023] © NeuroForge GmbH & Co. KG

import datetime
import itertools
import uuid
from typing import Iterable, Dict, Any, List, Tuple, Type, TypeVar, Callable, Generator, Union, cast, Optional

from celery.utils.log import get_task_logger  # type: ignore
from django.db import transaction
from django_multitenant.utils import set_current_tenant, get_current_tenant  # type: ignore

from skipper import settings
from skipper.core.celery import task
from skipper.core.models.tenant import Tenant
from skipper.dataseries.models import BulkInsertTaskData
from skipper.dataseries.models.event import data_point_event, ConsumerEventType
from skipper.dataseries.storage.contract import StorageBackendType, file_registry
from skipper.dataseries.storage.contract.file_registry import HistoryDataPointIdentifier, \
    HistoryDataPointIdentifierBulkElem
from skipper.dataseries.storage.dynamic_sql.models.base_relation import BaseDataPointFactRelation
from skipper.dataseries.storage.dynamic_sql.models.datapoint import WritableDataPoint
from skipper.dataseries.storage.dynamic_sql.models.dimension import WritableDataPoint_Dimension
from skipper.dataseries.storage.dynamic_sql.models.facts.boolean_fact import WritableDataPoint_BooleanFact
from skipper.dataseries.storage.dynamic_sql.models.facts.file_fact import WritableDataPoint_FileFact
from skipper.dataseries.storage.dynamic_sql.models.facts.float_fact import WritableDataPoint_FloatFact
from skipper.dataseries.storage.dynamic_sql.models.facts.image_fact import WritableDataPoint_ImageFact
from skipper.dataseries.storage.dynamic_sql.models.facts.json_fact import WritableDataPoint_JsonFact
from skipper.dataseries.storage.dynamic_sql.models.facts.string_fact import WritableDataPoint_StringFact
from skipper.dataseries.storage.dynamic_sql.models.facts.text_fact import WritableDataPoint_TextFact
from skipper.dataseries.storage.dynamic_sql.models.facts.timestamp_fact import WritableDataPoint_TimestampFact
from skipper.dataseries.storage.dynamic_sql.queries.modification_materialized.insert import insert_or_update_data_points
from skipper.dataseries.storage.dynamic_sql.tasks.common import get_or_fail
from skipper.dataseries.storage.static_ds_information import DataPointSerializationKeys

logger = get_task_logger(__name__)


def create_facts(
        tenant_id: Union[str, uuid.UUID],
        data_series_id: Union[str, uuid.UUID],
        name: str,
        validated_datas: Iterable[Dict[str, Dict[str, Any]]],
        relevant_keys: List[Tuple[str, str]],
        data_points: Iterable[WritableDataPoint],
        dp_relation_type: Type[BaseDataPointFactRelation],
        insert_dates: List[datetime.datetime],
        user_id: str,
        record_source: str,
        sub_clocks: List[int],
        register_file: bool = False
     ) -> None:
    _relation_objects = []

    for data_point, validated_data, insert_date, sub_clock in zip(data_points, validated_datas, insert_dates, sub_clocks):
        if name in validated_data:
            values: Dict[str, Any] = validated_data[name]
            for _key, _uuid in relevant_keys:
                _value = None
                _value_set = False
                if _key in values:
                    _value = values[_key]
                    _value_set = True

                # value may be none if we update
                if _value_set:
                    to_store = dp_relation_type(
                        point_in_time=insert_date,
                        data_point_id=data_point.id,
                        fact_id=_uuid,
                        value=_value,  # type: ignore
                        user_id=user_id,
                        record_source=record_source,
                        sub_clock=sub_clock
                    )
                    _relation_objects.append(to_store)

    if len(_relation_objects) > 0:
        dp_relation_type.objects.bulk_create(_relation_objects)
        if register_file:
            bulk = [
                HistoryDataPointIdentifierBulkElem(
                    fact_id=elem.fact_id,
                    file_name=elem.value.name,
                    history_data_point_identifier=HistoryDataPointIdentifier(
                        data_point_id=elem.data_point_id,
                        point_in_time=elem.point_in_time,
                        sub_clock=elem.sub_clock
                    )
                ) for elem in _relation_objects
                if elem.value is not None and elem.value.name is not None
            ]

            file_registry.register_bulk(
                tenant_id=tenant_id,
                data_series_id=data_series_id,
                bulk=bulk
            )



__T = TypeVar('__T')

__U = TypeVar('__U')


def chunks(iterable: Iterable[__T], size: int = 10, map_fn: Callable[[__T], Any] = lambda x: x) \
        -> Generator[Generator[List[__U], None, None], None, None]:
    iterator = iter(iterable)
    for first in iterator:  # stops when iterator is depleted
        def chunk() -> Generator[List[__U], None, None]:  # construct generator for next chunk
            yield map_fn(first)  # yield element from for loop
            for more in itertools.islice(iterator, size - 1):
                yield map_fn(more)  # yield more elements from the iterator

        yield chunk()  # in outer generator, yield next chunk


def create_dimensions(name: str, validated_datas: Iterable[Dict[str, Any]], relevant_keys: List[Tuple[str, str]],
                      data_points: List[WritableDataPoint],
                      dp_relation_type: Type[WritableDataPoint_Dimension],
                      insert_dates: List[datetime.datetime],
                      user_id: str,
                      record_source: str,
                      sub_clocks: List[int]) -> None:
    _relation_objects: List[Any] = []

    for data_point, validated_data, insert_date, sub_clock in zip(data_points, validated_datas, insert_dates, sub_clocks):
        if name in validated_data:
            values: Dict[str, Any] = validated_data[name]
            for _key, _uuid in relevant_keys:
                _value = None
                _value_set = False
                if _key in values:
                    _value = values[_key]
                    _value_set = True

                # value may be none if we update
                if _value_set:
                    to_store = dp_relation_type(
                        point_in_time=insert_date,
                        data_point_id=data_point.id,
                        dimension_id=_uuid,
                        value=_value,
                        user_id=user_id,
                        record_source=record_source,
                        sub_clock=sub_clock
                    )
                    _relation_objects.append(to_store)

    if len(_relation_objects) > 0:
        dp_relation_type.objects.bulk_create(_relation_objects)


def create_data_points(
        tenant_id: Union[uuid.UUID, str],
        tenant_name: str,
        data_series_id: Union[uuid.UUID, str],
        data_series_external_id: str,
        data_series_backend: str,
        validated_datas: Iterable[Dict[str, Any]],
        serialization_keys: DataPointSerializationKeys,
        point_in_time: datetime.datetime,
        user_id: str,
        record_source: str,
        partial: bool,
        sub_clock: int
) -> List[Any]:
    """
    :param data_series_id:
    :param validated_datas:
    :param serialization_keys:
    :param point_in_time: defaults to now
    :return:
    """

    def _create_bare_data_points(validated_datas: Iterable[Any]) -> Tuple[
        List[WritableDataPoint], List[datetime.datetime], List[Optional[int]]]:
        _data_points: List[WritableDataPoint] = []
        _point_in_time_times = []
        _sub_clocks = []

        for validated_data in validated_datas:
            _data_points.append(WritableDataPoint(
                id=validated_data['id'],
                external_id=validated_data['external_id'],
                data_series_id=data_series_id,
                point_in_time=point_in_time,
                user_id=user_id,
                record_source=record_source,
                sub_clock=sub_clock
            ))
            _point_in_time_times.append(point_in_time)
            _sub_clocks.append(sub_clock)

        if data_series_backend != StorageBackendType.DYNAMIC_SQL_NO_HISTORY.value \
                and data_series_backend != StorageBackendType.DYNAMIC_SQL_MATERIALIZED_FLAT_HISTORY.value:
            # FIXME: HACK! we return the objects, but dont save them!
            WritableDataPoint.objects.bulk_create(_data_points)
        return _data_points, _point_in_time_times, _sub_clocks

    data_points, point_in_time_times, sub_clocks = _create_bare_data_points(validated_datas=validated_datas)

    if data_series_backend != StorageBackendType.DYNAMIC_SQL_NO_HISTORY.value \
            and data_series_backend != StorageBackendType.DYNAMIC_SQL_MATERIALIZED_FLAT_HISTORY.value:

        create_facts(tenant_id, data_series_id, 'payload', validated_datas, serialization_keys['float_facts'], data_points,
                     WritableDataPoint_FloatFact,
                     point_in_time_times, user_id, record_source, sub_clocks)
        create_facts(tenant_id, data_series_id, 'payload', validated_datas, serialization_keys['string_facts'], data_points,
                     WritableDataPoint_StringFact,
                     point_in_time_times, user_id, record_source, sub_clocks)
        create_facts(tenant_id, data_series_id, 'payload', validated_datas, serialization_keys['text_facts'], data_points,
                     WritableDataPoint_TextFact,
                     point_in_time_times, user_id, record_source, sub_clocks)
        create_facts(tenant_id, data_series_id, 'payload', validated_datas, serialization_keys['timestamp_facts'], data_points,
                     WritableDataPoint_TimestampFact,
                     point_in_time_times, user_id, record_source, sub_clocks)
        create_facts(tenant_id, data_series_id, 'payload', validated_datas, serialization_keys['image_facts'], data_points,
                     WritableDataPoint_ImageFact,
                     point_in_time_times, user_id, record_source, sub_clocks, register_file=True)
        create_facts(tenant_id, data_series_id, 'payload', validated_datas, serialization_keys['file_facts'], data_points,
                     WritableDataPoint_FileFact,
                     point_in_time_times, user_id, record_source, sub_clocks, register_file=True)
        create_facts(tenant_id, data_series_id, 'payload', validated_datas, serialization_keys['json_facts'], data_points,
                     WritableDataPoint_JsonFact,
                     point_in_time_times, user_id, record_source, sub_clocks)
        create_facts(tenant_id, data_series_id, 'payload', validated_datas, serialization_keys['boolean_facts'], data_points,
                     WritableDataPoint_BooleanFact,
                     point_in_time_times, user_id, record_source, sub_clocks)

        create_dimensions('payload', validated_datas, serialization_keys['dimensions'], data_points,
                          WritableDataPoint_Dimension,
                          point_in_time_times, user_id, record_source, sub_clocks)

    if data_series_backend == StorageBackendType.DYNAMIC_SQL_MATERIALIZED.value\
            or data_series_backend == StorageBackendType.DYNAMIC_SQL_NO_HISTORY.value\
            or data_series_backend == StorageBackendType.DYNAMIC_SQL_MATERIALIZED_FLAT_HISTORY.value:
        insert_or_update_data_points(
            tenant_id=tenant_id,
            tenant_name=tenant_name,
            data_series_id=str(data_series_id),
            data_series_external_id=data_series_external_id,
            point_in_time=point_in_time,
            data_point_serialization_keys=serialization_keys,
            validated_datas=validated_datas,
            partial=partial,
            sub_clock=sub_clock,
            backend=data_series_backend,
            record_source=record_source,
            user_id=user_id
        )
    data_point_event(
        tenant=get_current_tenant(),
        data_series_id=data_series_id,
        point_in_time=point_in_time,
        payload={
            'data_series': {
                'id': data_series_id,
                'external_id': data_series_external_id
            },
            'data_points': [{
                'id': dp.id,
                'external_id': dp.external_id
            } for dp in data_points]
        },
        event_type=ConsumerEventType.DATA_POINT_CHANGED,
        sub_clock=sub_clock
    )
    # FIXME: returning WritableDataPoint is fine here since all of our
    # code does not really care about the class anyways, it's not nice, though
    return data_points


class RetryException(Exception):
    pass

# acks late to automatically retry here? or should we keep track differently?


# to prevent weird race conditions under heavy load, we retry if the data is not there yet

@task(
    name="_3_dynamic_sql_persist_data_point_chunk",
    acks_late=True,
    queue='persist_data'
)  # type: ignore
def async_persist_data_point_chunk(
    task_data_reference_id: int
) -> None:
    with transaction.atomic():
        # this must run outside of any tenant context or we dont get all data in a multitenant environment
        set_current_tenant(None)
        # skip the task if it was already claimed by another task
        task_data = BulkInsertTaskData.objects.filter(id=task_data_reference_id).select_for_update(skip_locked=True).first()
        if task_data is None:
            logger.warn('task data not found, either claimed by someone else or task does not exist (anymore)')
        if task_data is not None:
            # should we lock here?
            persist_data_point_chunk(
                tenant_id=str(task_data.tenant.id),
                tenant_name=task_data.tenant.name,
                data_series_id=str(task_data.data_series.id),
                data_series_external_id=task_data.data_series.external_id,
                data_series_backend=task_data.data_series.backend,
                validated_datas=task_data.data['validated_datas'],
                serialization_keys=task_data.data['serialization_keys'],
                point_in_time_timestamp=task_data.point_in_time.timestamp(),
                user_id=str(task_data.user.id),
                record_source=task_data.record_source,
                sub_clock=task_data.sub_clock
            )
            task_data.delete()
            # TODO: write error if error happened


def persist_data_point_chunk(
        tenant_id: str,
        tenant_name: str,
        data_series_id: str,
        data_series_external_id: str,
        data_series_backend: str,
        validated_datas: List[Dict[str, Any]],
        serialization_keys: DataPointSerializationKeys,
        point_in_time_timestamp: float,
        user_id: str,
        record_source: str,
        sub_clock: int
) -> None:
    set_current_tenant(get_or_fail(Tenant.objects.filter(id=tenant_id)))
    point_in_time = datetime.datetime.fromtimestamp(point_in_time_timestamp, tz=datetime.timezone.utc)

    flattened_keys = flatten_serialization_keys(serialization_keys)

    for chunk in cast(Generator[List[Dict[str, Any]], None, None],
                        chunks(
                            validated_datas,
                            size=settings.SKIPPER_DATA_SERIES_BULK_BATCH_SIZE,
                            map_fn=lambda x: set_missing_structure_elements_to_none_with_flattened_keys(
                                x,
                                flattened_keys
                            )
                        )):
        chunk_list = list(chunk)
        create_data_points(
            tenant_id=tenant_id,
            tenant_name=tenant_name,
            data_series_id=data_series_id,
            data_series_external_id=data_series_external_id,
            data_series_backend=data_series_backend,
            validated_datas=chunk_list,
            serialization_keys=serialization_keys,
            point_in_time=point_in_time,
            user_id=user_id,
            record_source=record_source,
            partial=False,
            sub_clock=sub_clock
        )


def flatten_serialization_keys(_dict: DataPointSerializationKeys) -> List[Tuple[str, str]]:
    return _dict['float_facts'] + _dict['string_facts'] + _dict['text_facts'] + _dict['timestamp_facts'] + _dict[
        'json_facts'] + _dict['image_facts'] + _dict['boolean_facts'] + _dict['file_facts'] + _dict['dimensions']


def set_missing_structure_elements_to_none_with_flattened_keys(
    validated_data: Dict[str, Any],
    flattened_keys: List[Tuple[str, str]]
) -> Dict[str, Any]:
    for _external_id, _uuid in flattened_keys:
        if _external_id not in validated_data['payload']:
            validated_data['payload'][_external_id] = None
    return validated_data


def set_missing_structure_elements_to_none(
    serialization_keys: DataPointSerializationKeys,
    validated_data: Dict[str, Any]
) -> Dict[str, Any]:
    return set_missing_structure_elements_to_none_with_flattened_keys(
        validated_data,
        flatten_serialization_keys(serialization_keys)
    )
