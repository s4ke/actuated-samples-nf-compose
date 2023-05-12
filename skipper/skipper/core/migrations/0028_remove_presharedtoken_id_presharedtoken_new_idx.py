# Generated by Django 4.0 on 2021-12-31 20:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_alter_presharedtoken_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presharedtoken',
            name='id',
        ),
        migrations.AlterField(
            model_name='presharedtoken',
            name='new_idx',
            field=models.UUIDField(default=uuid.uuid4, null=False, editable=False, primary_key=True, serialize=False),
        ),
    ]
