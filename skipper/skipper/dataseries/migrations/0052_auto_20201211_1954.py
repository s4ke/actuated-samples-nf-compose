# Generated by Django 3.1.2 on 2020-12-11 19:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0025_delete_tasklogentry'),
        ('dataseries', '0051_asyncdata_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AsyncData',
            new_name='TaskData',
        ),
    ]
