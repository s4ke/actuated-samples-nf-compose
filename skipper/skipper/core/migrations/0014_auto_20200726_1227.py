# Generated by Django 3.0.7 on 2020-07-26 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_job'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Job',
            new_name='DefaultJob',
        ),
    ]
