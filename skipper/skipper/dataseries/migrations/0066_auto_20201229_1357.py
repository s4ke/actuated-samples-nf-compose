# Generated by Django 3.1.2 on 2020-12-29 13:57

from django.db import migrations, models
import skipper.core.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dataseries', '0065_auto_20201221_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskdata',
            name='data',
            field=models.JSONField(encoder=skipper.core.models.fields.JSONEncoder),  # type: ignore
        ),
    ]
