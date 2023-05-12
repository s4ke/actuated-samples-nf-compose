# Generated by Django 3.0.7 on 2020-08-01 16:07

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django_multitenant.mixins  # type: ignore
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20200731_0920'),
        ('dataseries', '0032_drop_postgresanalyticsuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostgresAnalyticsUser',
            fields=[
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('role', models.CharField(max_length=63)),
                ('tenant_global_read', models.BooleanField()),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Tenant')),
            ],
            options={
                'db_table': '_3_postgresanalyticsuser',
            },
            bases=(django_multitenant.mixins.TenantModelMixin, models.Model),
            managers=[
                ('all_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
