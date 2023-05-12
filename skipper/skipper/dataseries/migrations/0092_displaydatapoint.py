# Generated by Django 4.1.7 on 2023-02-25 15:07

from django.db import migrations, models
import skipper.core.models.fields
import skipper.core.models.validation


class Migration(migrations.Migration):

    dependencies = [
        ('dataseries', '0091_alter_consumer_target'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisplayDataPoint',
            fields=[
                ('id', models.CharField(default=None, max_length=512, primary_key=True, serialize=False)),
                ('payload', skipper.core.models.fields.EmptyDictNotBlankJSONField(default=dict)),
                ('external_id', models.CharField(max_length=256, validators=[skipper.core.models.validation.external_id_validator_sql_safe])),
                ('point_in_time', models.CharField(default=None, max_length=100)),
                ('versions', skipper.core.models.fields.EmptyDictNotBlankJSONField(default=dict, null=True)),
                ('pagination_data', skipper.core.models.fields.EmptyDictNotBlankJSONField(default=dict)),
            ],
            options={
                'db_table': 'DOES_NOT_EXIST',
                'managed': False,
                'default_permissions': [],
            },
        ),
    ]
