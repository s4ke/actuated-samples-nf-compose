# Generated by Django 3.1.2 on 2021-01-11 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flow', '0028_auto_20210109_1520'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flowpermissions',
            options={'default_permissions': [], 'managed': False, 'permissions': (('system.engine', 'Allowed to access system engine'), ('impl', 'Allowed to access flow implementation endpoints'))},
        ),
    ]
