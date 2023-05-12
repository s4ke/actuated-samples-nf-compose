# Generated by Django 3.2.4 on 2021-08-05 09:35

from django.db import migrations, models
import django.db.models.deletion
import django_multitenant.mixins  # type: ignore
import skipper.core.models.softdelete


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_delete_tasklogentry'),
        ('dataseries', '0070_alter_dataseries_backend'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileLookup',
            fields=[
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('data_series_id', models.UUIDField(editable=False)),
                ('fact_id', models.UUIDField(editable=False)),
                ('data_point_id', models.CharField(default=None, max_length=512)),
                ('point_in_time', models.DateTimeField()),
                ('sub_clock', models.BigIntegerField()),
                ('file_name', models.TextField(db_index=True)),
                ('tenant', models.ForeignKey(db_constraint=False, db_index=False, on_delete=django.db.models.deletion.DO_NOTHING, to='core.tenant')),
            ],
            options={
                'db_table': '_3_file_lookup',
                'managed': True,
                'default_permissions': [],
            },
            bases=(django_multitenant.mixins.TenantModelMixin, models.Model),
            managers=[
                ('all_objects', skipper.core.models.softdelete.SoftDeletionTenantManager(alive_only=False)),
                ('objects', skipper.core.models.softdelete.SoftDeletionTenantManager()),
            ],
        ),
        migrations.AddConstraint(
            model_name='filelookup',
            constraint=models.UniqueConstraint(fields=('tenant_id', 'data_series_id', 'fact_id', 'data_point_id', 'point_in_time', 'sub_clock'), name='unique_file_lookup'),
        ),
    ]
