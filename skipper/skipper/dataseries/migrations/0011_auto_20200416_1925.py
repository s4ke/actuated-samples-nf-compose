# Generated by Django 2.2.8 on 2020-04-16 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataseries', '0010_dataseriespermissions'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dataseriespermissions',
            options={'default_permissions': [], 'managed': False, 'permissions': (('node_red_etl', 'Allowed to use the node red ETL interface (node_red_etl)'), ('storage_backend_data', 'Allowed to view metadata of the backends (storage_backend_data)'))},
        ),
    ]
