# Generated by Django 3.1.2 on 2020-10-30 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataseries', '0041_merge_20201023_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumerevent',
            name='event_type',
            field=models.CharField(choices=[('DATA_POINT_CHANGED', 'DATA_POINT_CHANGED'), ('DATA_POINT_DELETED', 'DATA_POINT_DELETED'), ('DATA_SERIES_TRUNCATED', 'DATA_SERIES_TRUNCATED')], max_length=100),
        ),
    ]
