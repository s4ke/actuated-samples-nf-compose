# Generated by Django 3.0.7 on 2020-06-11 12:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0010_presharedtoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presharedtoken',
            name='key',
            field=models.CharField(help_text='The actual preshared token credential. Must be unique across all users in the whole system', max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='presharedtoken',
            name='user',
            field=models.ForeignKey(help_text='the user this token is referring to', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
