# Generated by Django 3.1.2 on 2020-12-12 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataseries', '0056_auto_20201212_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskdata',
            name='point_in_time',
            field=models.DateTimeField(),
        ),
    ]
