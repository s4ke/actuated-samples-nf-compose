# Generated by Django 3.2.2 on 2021-05-13 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataseries', '0067_auto_20210223_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskdata',
            name='sub_clock',
            field=models.BigIntegerField(null=True),
        ),
    ]
