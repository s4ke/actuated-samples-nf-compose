# Generated by Django 3.1.2 on 2020-12-16 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flow', '0009_auto_20201022_2317'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flowpermissions',
            options={'default_permissions': [], 'managed': False, 'permissions': (('system.edit', 'Allowed to edit system flows'), ('edit', 'Allowed to edit flows'), ('impl', 'Allowed to access flow implementation endpoints'))},
        ),
    ]
