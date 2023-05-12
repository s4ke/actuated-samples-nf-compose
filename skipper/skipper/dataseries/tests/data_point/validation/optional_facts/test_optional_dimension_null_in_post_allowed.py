# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. 
# If a copy of the MPL was not distributed with this file, 
# You can obtain one at https://mozilla.org/MPL/2.0/.
# This file is part of NF Compose
# [2019] - [2023] © NeuroForge GmbH & Co. KG


import io
from typing import Any, Dict

from PIL import Image as PIL_Image  # type: ignore

from skipper import modules
from skipper.core.tests.base import BaseViewTest, BASE_URL

from rest_framework import status

DATA_SERIES_BASE_URL = BASE_URL + modules.url_representation(modules.Module.DATA_SERIES) + '/'


class DimensionTest(BaseViewTest):
    # the list endpoint is disabled for datapoints if we do not select for a data series
    url_under_test = DATA_SERIES_BASE_URL + 'dataseries/'
    simulate_other_tenant = True

    data_series: Dict[str, Any]
    other_data_series: Dict[str, Any]

    fact_type: str

    def setUp(self) -> None:
        super().setUp()

        self.data_series = self.create_payload(DATA_SERIES_BASE_URL + 'dataseries/', payload={
            'name': 'my_data_series_1',
            'external_id': 'external_id1'
        }, simulate_tenant=False)

        self.other_data_series = self.create_payload(DATA_SERIES_BASE_URL + 'dataseries/', payload={
            'name': 'my_data_series_2',
            'external_id': 'external_id2'
        }, simulate_tenant=False)

    def add_dim(self, optional: bool) -> None:
        self.create_payload(self.data_series['dimensions'], {
            'external_id': '1',
            'optional': optional,
            'reference': self.other_data_series['url'],
            'name': '1'
        })

    def test_missing_altogether(self) -> None:
        self.add_dim(optional=False)

        response = self.client.post(
            path=self.data_series['data_points'],
            data={
                f"external_id": 'should_fail',
                "payload": {
                    "1": None
                }
            }, format='json')
        self.assertEquals(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_missing_as_null(self) -> None:
        self.add_dim(optional=False)

        response = self.client.post(
            path=self.data_series['data_points'],
            data={
                f"external_id": 'should_fail',
                "payload": {
                    "1": None
                }
            }, format='json')
        self.assertEquals(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_null_as_optional(self) -> None:
        self.add_dim(optional=True)

        response = self.client.post(
            path=self.data_series['data_points'],
            data={
                f"external_id": 'should_fail',
                "payload": {
                    "1": None
                }
            }, format='json')
        self.assertEquals(status.HTTP_201_CREATED, response.status_code)