# Generated by Django 3.1.2 on 2021-01-06 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flow', '0022_auto_20210105_1330'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='engine',
            options={'permissions': [('engine_get_engine', 'Can run GET on entity engine and action engine'), ('engine_options_engine', 'Can run OPTIONS on entity engine on action engine'), ('engine_head_engine', 'Can run HEAD on entity engine on action engine'), ('engine_post_engine', 'Can run POST on entity engine on action engine'), ('engine_put_engine', 'Can run PUT on entity engine on action engine'), ('engine_patch_engine', 'Can run PATCH on entity engine on action engine'), ('engine_delete_engine', 'Can run DELETE on entity engine on action engine'), ('engine_get_permission', 'Can run GET on entity engine and action permission'), ('engine_options_permission', 'Can run OPTIONS on entity engine on action permission'), ('engine_head_permission', 'Can run HEAD on entity engine on action permission'), ('engine_post_permission', 'Can run POST on entity engine on action permission'), ('engine_put_permission', 'Can run PUT on entity engine on action permission'), ('engine_patch_permission', 'Can run PATCH on entity engine on action permission'), ('engine_delete_permission', 'Can run DELETE on entity engine on action permission'), ('engine_get_access', 'Can run GET on entity engine and action access')]},
        ),
    ]
