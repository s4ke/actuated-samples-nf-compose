# Generated by Django 4.0.3 on 2022-04-23 11:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flow', '0034_auto_20210118_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engine',
            name='upstream',
            field=models.URLField(max_length=256, validators=[django.core.validators.URLValidator(schemes=['https', 'http'])]),
        ),
    ]
