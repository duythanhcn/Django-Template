from django.contrib.gis.db import models


class OverBurden(models.Model):
    class Meta:
        db_table = 'overburden'

    upper_housing_station_code = models.BigIntegerField(null=False)
    upper_facility_key = models.CharField(max_length=4000, null=True)
    lower_housing_station_code = models.BigIntegerField(null=True)
    lowwer_facility_key = models.CharField(max_length=4000, null=True)
    shape_wkt = models.PointField(null=False, geography=True)

    p000_ground_height = models.FloatField(null=True)
    p000_formation_height = models.FloatField(null=True)
    p000_overburden_value = models.FloatField(null=True)
    p000_kuzushi_column = models.IntegerField(null=True)
    p000_kuzushi_step = models.IntegerField(null=True)
    p000_safety_type = models.CharField(max_length=4000, null=True)
    p000_safety_value = models.FloatField(null=True)

    p001_distance_from_prev = models.FloatField(null=True)
    p001_ground_height = models.FloatField(null=True)
    p001_formation_height = models.FloatField(null=True)
    p001_overburden_value = models.FloatField(null=True)
    p001_kuzushi_column = models.IntegerField(null=True)
    p001_kuzushi_step = models.IntegerField(null=True)
    p001_safety_type = models.CharField(max_length=4000, null=True)
    p001_safety_value = models.FloatField(null=True)

    p002_distance_from_prev = models.FloatField(null=True)
    p002_ground_height = models.FloatField(null=True)
    p002_formation_height = models.FloatField(null=True)
    p002_overburden_value = models.FloatField(null=True)
    p002_kuzushi_column = models.IntegerField(null=True)
    p002_kuzushi_step = models.IntegerField(null=True)
    p002_safety_type = models.CharField(max_length=4000, null=True)
    p002_safety_value = models.FloatField(null=True)

    p003_distance_from_prev = models.FloatField(null=True)
    p003_ground_height = models.FloatField(null=True)
    p003_formation_height = models.FloatField(null=True)
    p003_overburden_value = models.FloatField(null=True)
    p003_kuzushi_column = models.IntegerField(null=True)
    p003_kuzushi_step = models.IntegerField(null=True)
    p003_safety_type = models.CharField(max_length=4000, null=True)
    p003_safety_value = models.FloatField(null=True)

    p004_distance_from_prev = models.FloatField(null=True)
    p004_ground_height = models.FloatField(null=True)
    p004_formation_height = models.FloatField(null=True)
    p004_overburden_value = models.FloatField(null=True)
    p004_kuzushi_column = models.IntegerField(null=True)
    p004_kuzushi_step = models.IntegerField(null=True)
    p004_safety_type = models.CharField(max_length=4000, null=True)
    p004_safety_value = models.FloatField(null=True)

    p005_distance_from_prev = models.FloatField(null=True)
    p005_ground_height = models.FloatField(null=True)
    p005_formation_height = models.FloatField(null=True)
    p005_overburden_value = models.FloatField(null=True)
    p005_kuzushi_column = models.IntegerField(null=True)
    p005_kuzushi_step = models.IntegerField(null=True)
    p005_safety_type = models.CharField(max_length=4000, null=True)
    p005_safety_value = models.FloatField(null=True)

    fabricated_type_code = models.BigIntegerField(null=True)

    created_by = models.CharField(max_length=4000, null=True)
    created_at = models.DateTimeField(null=True)

    updated_by = models.CharField(max_length=4000, null=True)
    updated_at = models.DateTimeField(null=True)
