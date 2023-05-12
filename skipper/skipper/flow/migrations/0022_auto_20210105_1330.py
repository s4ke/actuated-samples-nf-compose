# Generated by Django 3.1.2 on 2021-01-05 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flow', '0021_auto_20210105_1018'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='flow',
            constraint=models.UniqueConstraint(condition=models.Q(deleted_at__isnull=True), fields=('tenant_id', 'external_id'), name='_4_flow_tenant_id_external_id__1'),
        ),
    ]
