# Generated by Django 3.0.9 on 2020-09-25 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flow', '0006_auto_20200716_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flow',
            name='method',
            field=models.CharField(choices=[('GET', 'GET'), ('POST', 'POST'), ('PUT', 'PUT'), ('PATCH', 'PATCH'), ('DELETE', 'DELETE'), ('HEAD', 'HEAD')], max_length=10),
        ),
    ]
