from django.contrib.gis.db import models


class MH(models.Model):
    class Meta:
        db_table = 'MH'

    housing_area_code = models.BigIntegerField(null=False)
    facility_key = models.CharField(max_length=4000, null=True)
    shape_wkt = models.PointField(null=False, geography=True)
    facility_type = models.CharField(max_length=4000, null=True)
    ordinal_number = models.IntegerField(null=True)
    structure_type = models.CharField(max_length=4000, null=True)
    shape = models.CharField(max_length=4000, null=True)
    fabricated_type_code = models.BigIntegerField(null=True)
    pref = models.CharField(max_length=4000, null=True)

    created_by = models.CharField(max_length=4000, null=True)
    created_at = models.DateTimeField(null=True)

    updated_by = models.CharField(max_length=4000, null=True)
    updated_at = models.DateTimeField(null=True)
