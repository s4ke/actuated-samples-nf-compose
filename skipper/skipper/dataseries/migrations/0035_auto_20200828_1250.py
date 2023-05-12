# Generated by Django 3.0.9 on 2020-08-28 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataseries', '0034_auto_20200806_1715'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dataseries',
            options={'permissions': [('ds_get_data_series', 'Can run GET on action data_series'), ('ds_options_data_series', 'Can run OPTIONS on action data_series'), ('ds_head_data_series', 'Can run HEAD on action data_series'), ('ds_post_data_series', 'Can run POST on action data_series'), ('ds_put_data_series', 'Can run PUT on action data_series'), ('ds_patch_data_series', 'Can run PATCH on action data_series'), ('ds_delete_data_series', 'Can run DELETE on action data_series'), ('ds_get_data_point', 'Can run GET on action data_point'), ('ds_options_data_point', 'Can run OPTIONS on action data_point'), ('ds_head_data_point', 'Can run HEAD on action data_point'), ('ds_post_data_point', 'Can run POST on action data_point'), ('ds_put_data_point', 'Can run PUT on action data_point'), ('ds_patch_data_point', 'Can run PATCH on action data_point'), ('ds_delete_data_point', 'Can run DELETE on action data_point'), ('ds_get_history_data_point', 'Can run GET on action history_data_point'), ('ds_options_history_data_point', 'Can run OPTIONS on action history_data_point'), ('ds_head_history_data_point', 'Can run HEAD on action history_data_point'), ('ds_post_history_data_point', 'Can run POST on action history_data_point'), ('ds_put_history_data_point', 'Can run PUT on action history_data_point'), ('ds_patch_history_data_point', 'Can run PATCH on action history_data_point'), ('ds_delete_history_data_point', 'Can run DELETE on action history_data_point'), ('ds_get_structure_element', 'Can run GET on action structure_element'), ('ds_options_structure_element', 'Can run OPTIONS on action structure_element'), ('ds_head_structure_element', 'Can run HEAD on action structure_element'), ('ds_post_structure_element', 'Can run POST on action structure_element'), ('ds_put_structure_element', 'Can run PUT on action structure_element'), ('ds_patch_structure_element', 'Can run PATCH on action structure_element'), ('ds_delete_structure_element', 'Can run DELETE on action structure_element'), ('ds_get_create_view', 'Can run GET on action create_view'), ('ds_options_create_view', 'Can run OPTIONS on action create_view'), ('ds_head_create_view', 'Can run HEAD on action create_view'), ('ds_post_create_view', 'Can run POST on action create_view'), ('ds_put_create_view', 'Can run PUT on action create_view'), ('ds_patch_create_view', 'Can run PATCH on action create_view'), ('ds_delete_create_view', 'Can run DELETE on action create_view'), ('ds_get_prune_history', 'Can run GET on action prune_history'), ('ds_options_prune_history', 'Can run OPTIONS on action prune_history'), ('ds_head_prune_history', 'Can run HEAD on action prune_history'), ('ds_post_prune_history', 'Can run POST on action prune_history'), ('ds_put_prune_history', 'Can run PUT on action prune_history'), ('ds_patch_prune_history', 'Can run PATCH on action prune_history'), ('ds_delete_prune_history', 'Can run DELETE on action prune_history'), ('ds_get_truncate_data_series', 'Can run GET on action truncate_data_series'), ('ds_options_truncate_data_series', 'Can run OPTIONS on action truncate_data_series'), ('ds_head_truncate_data_series', 'Can run HEAD on action truncate_data_series'), ('ds_post_truncate_data_series', 'Can run POST on action truncate_data_series'), ('ds_put_truncate_data_series', 'Can run PUT on action truncate_data_series'), ('ds_patch_truncate_data_series', 'Can run PATCH on action truncate_data_series'), ('ds_delete_truncate_data_series', 'Can run DELETE on action truncate_data_series'), ('ds_get_cube_sql', 'Can run GET on action cube_sql'), ('ds_options_cube_sql', 'Can run OPTIONS on action cube_sql'), ('ds_head_cube_sql', 'Can run HEAD on action cube_sql'), ('ds_post_cube_sql', 'Can run POST on action cube_sql'), ('ds_put_cube_sql', 'Can run PUT on action cube_sql'), ('ds_patch_cube_sql', 'Can run PATCH on action cube_sql'), ('ds_delete_cube_sql', 'Can run DELETE on action cube_sql'), ('ds_get_data_point_bulk', 'Can run GET on action data_point_bulk'), ('ds_options_data_point_bulk', 'Can run OPTIONS on action data_point_bulk'), ('ds_head_data_point_bulk', 'Can run HEAD on action data_point_bulk'), ('ds_post_data_point_bulk', 'Can run POST on action data_point_bulk'), ('ds_put_data_point_bulk', 'Can run PUT on action data_point_bulk'), ('ds_patch_data_point_bulk', 'Can run PATCH on action data_point_bulk'), ('ds_delete_data_point_bulk', 'Can run DELETE on action data_point_bulk'), ('ds_get_check_external_ids', 'Can run GET on action check_external_ids'), ('ds_options_check_external_ids', 'Can run OPTIONS on action check_external_ids'), ('ds_head_check_external_ids', 'Can run HEAD on action check_external_ids'), ('ds_post_check_external_ids', 'Can run POST on action check_external_ids'), ('ds_put_check_external_ids', 'Can run PUT on action check_external_ids'), ('ds_patch_check_external_ids', 'Can run PATCH on action check_external_ids'), ('ds_delete_check_external_ids', 'Can run DELETE on action check_external_ids'), ('ds_get_permission', 'Can run GET on action permission'), ('ds_options_permission', 'Can run OPTIONS on action permission'), ('ds_head_permission', 'Can run HEAD on action permission'), ('ds_post_permission', 'Can run POST on action permission'), ('ds_put_permission', 'Can run PUT on action permission'), ('ds_patch_permission', 'Can run PATCH on action permission'), ('ds_delete_permission', 'Can run DELETE on action permission'), ('ds_get_consumer', 'Can run GET on action consumer'), ('ds_options_consumer', 'Can run OPTIONS on action consumer'), ('ds_head_consumer', 'Can run HEAD on action consumer'), ('ds_post_consumer', 'Can run POST on action consumer'), ('ds_put_consumer', 'Can run PUT on action consumer'), ('ds_patch_consumer', 'Can run PATCH on action consumer'), ('ds_delete_consumer', 'Can run DELETE on action consumer')]},
        ),
    ]
