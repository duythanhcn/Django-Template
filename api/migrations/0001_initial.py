# Generated by Django 3.1.2 on 2020-10-06 07:30

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=1000, unique=True)),
                ('created_at', models.DateTimeField(verbose_name='date published')),
                ('updated_at', models.DateTimeField(verbose_name='date published')),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Mansion',
            fields=[
                ('gid', models.BigAutoField(primary_key=True, serialize=False)),
                ('housing_area_code', models.BigIntegerField()),
                ('facility_key', models.CharField(max_length=4000, null=True)),
                ('shape_wkt', django.contrib.gis.db.models.fields.MultiLineStringField(geography=True, srid=4326)),
                ('fabricated_type_code', models.BigIntegerField(null=True)),
                ('pref', models.CharField(max_length=4000, null=True)),
                ('created_by', models.CharField(max_length=4000, null=True)),
                ('created_at', models.DateTimeField(null=True)),
                ('updated_by', models.CharField(max_length=4000, null=True)),
                ('updated_at', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'mansion',
            },
        ),
        migrations.CreateModel(
            name='MH',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('housing_area_code', models.BigIntegerField()),
                ('facility_key', models.CharField(max_length=4000, null=True)),
                ('shape_wkt', django.contrib.gis.db.models.fields.PointField(geography=True, srid=4326)),
                ('facility_type', models.CharField(max_length=4000, null=True)),
                ('ordinal_number', models.IntegerField(null=True)),
                ('structure_type', models.CharField(max_length=4000, null=True)),
                ('shape', models.CharField(max_length=4000, null=True)),
                ('fabricated_type_code', models.BigIntegerField(null=True)),
                ('pref', models.CharField(max_length=4000, null=True)),
                ('created_by', models.CharField(max_length=4000, null=True)),
                ('created_at', models.DateTimeField(null=True)),
                ('updated_by', models.CharField(max_length=4000, null=True)),
                ('updated_at', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'MH',
            },
        ),
        migrations.CreateModel(
            name='OverBurden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upper_housing_station_code', models.BigIntegerField()),
                ('upper_facility_key', models.CharField(max_length=4000, null=True)),
                ('lower_housing_station_code', models.BigIntegerField(null=True)),
                ('lowwer_facility_key', models.CharField(max_length=4000, null=True)),
                ('shape_wkt', django.contrib.gis.db.models.fields.PointField(geography=True, srid=4326)),
                ('p000_ground_height', models.FloatField(null=True)),
                ('p000_formation_height', models.FloatField(null=True)),
                ('p000_overburden_value', models.FloatField(null=True)),
                ('p000_kuzushi_column', models.IntegerField(null=True)),
                ('p000_kuzushi_step', models.IntegerField(null=True)),
                ('p000_safety_type', models.CharField(max_length=4000, null=True)),
                ('p000_safety_value', models.FloatField(null=True)),
                ('p001_distance_from_prev', models.FloatField(null=True)),
                ('p001_ground_height', models.FloatField(null=True)),
                ('p001_formation_height', models.FloatField(null=True)),
                ('p001_overburden_value', models.FloatField(null=True)),
                ('p001_kuzushi_column', models.IntegerField(null=True)),
                ('p001_kuzushi_step', models.IntegerField(null=True)),
                ('p001_safety_type', models.CharField(max_length=4000, null=True)),
                ('p001_safety_value', models.FloatField(null=True)),
                ('p002_distance_from_prev', models.FloatField(null=True)),
                ('p002_ground_height', models.FloatField(null=True)),
                ('p002_formation_height', models.FloatField(null=True)),
                ('p002_overburden_value', models.FloatField(null=True)),
                ('p002_kuzushi_column', models.IntegerField(null=True)),
                ('p002_kuzushi_step', models.IntegerField(null=True)),
                ('p002_safety_type', models.CharField(max_length=4000, null=True)),
                ('p002_safety_value', models.FloatField(null=True)),
                ('p003_distance_from_prev', models.FloatField(null=True)),
                ('p003_ground_height', models.FloatField(null=True)),
                ('p003_formation_height', models.FloatField(null=True)),
                ('p003_overburden_value', models.FloatField(null=True)),
                ('p003_kuzushi_column', models.IntegerField(null=True)),
                ('p003_kuzushi_step', models.IntegerField(null=True)),
                ('p003_safety_type', models.CharField(max_length=4000, null=True)),
                ('p003_safety_value', models.FloatField(null=True)),
                ('p004_distance_from_prev', models.FloatField(null=True)),
                ('p004_ground_height', models.FloatField(null=True)),
                ('p004_formation_height', models.FloatField(null=True)),
                ('p004_overburden_value', models.FloatField(null=True)),
                ('p004_kuzushi_column', models.IntegerField(null=True)),
                ('p004_kuzushi_step', models.IntegerField(null=True)),
                ('p004_safety_type', models.CharField(max_length=4000, null=True)),
                ('p004_safety_value', models.FloatField(null=True)),
                ('p005_distance_from_prev', models.FloatField(null=True)),
                ('p005_ground_height', models.FloatField(null=True)),
                ('p005_formation_height', models.FloatField(null=True)),
                ('p005_overburden_value', models.FloatField(null=True)),
                ('p005_kuzushi_column', models.IntegerField(null=True)),
                ('p005_kuzushi_step', models.IntegerField(null=True)),
                ('p005_safety_type', models.CharField(max_length=4000, null=True)),
                ('p005_safety_value', models.FloatField(null=True)),
                ('fabricated_type_code', models.BigIntegerField(null=True)),
                ('created_by', models.CharField(max_length=4000, null=True)),
                ('created_at', models.DateTimeField(null=True)),
                ('updated_by', models.CharField(max_length=4000, null=True)),
                ('updated_at', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'overburden',
            },
        ),
        migrations.CreateModel(
            name='PipeLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('housing_area_code', models.BigIntegerField()),
                ('upper_facility_key', models.CharField(max_length=4000, null=True)),
                ('lower_facility_key', models.CharField(max_length=4000, null=True)),
                ('facility_type', django.contrib.gis.db.models.fields.MultiLineStringField(geography=True, srid=4326)),
                ('fabricated_type_code', models.BigIntegerField(null=True)),
                ('pref', models.CharField(max_length=4000, null=True)),
                ('created_by', models.CharField(max_length=4000, null=True)),
                ('created_at', models.DateTimeField(null=True)),
                ('updated_by', models.CharField(max_length=4000, null=True)),
                ('updated_at', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'pipeline',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(verbose_name='date published')),
                ('updated_at', models.DateTimeField(verbose_name='date published')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.category')),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]
