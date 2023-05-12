# Generated by Django 3.1.2 on 2020-10-22 23:17

from django.db import migrations
import skipper.core.models.softdelete


class Migration(migrations.Migration):

    dependencies = [
        ('flow', '0008_flow_public'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='flow',
            managers=[
                ('all_objects', skipper.core.models.softdelete.SoftDeletionTenantManager(alive_only=False)),
                ('objects', skipper.core.models.softdelete.SoftDeletionTenantManager()),
            ],
        ),
    ]
