# Generated by Django 4.0 on 2021-12-31 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataseries', '0084_remove_userdefinedindex_target_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdefinedindex_target',
            old_name='new_idx',
            new_name='id',
        ),
    ]
