# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. 
# If a copy of the MPL was not distributed with this file, 
# You can obtain one at https://mozilla.org/MPL/2.0/.
# This file is part of NF Compose
# [2019] - [2023] © NeuroForge GmbH & Co. KG


# Generated by Django 2.2.8 on 2020-01-31 15:48

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200106_2307'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllowedLoginRedirectHost',
            fields=[
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('host', models.CharField(default=None, max_length=256)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Tenant')),
            ],
            options={
                'db_table': '_core_allowedloginredirecthost',
            },
            managers=[
                ('all_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
