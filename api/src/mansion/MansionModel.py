from django.contrib.gis.db import models


class Mansion(models.Model):
    class Meta:
        db_table = 'mansion'

    gid = models.BigAutoField(primary_key=True)
    housing_area_code = models.BigIntegerField(null=False)
    facility_key = models.CharField(max_length=4000, null=True)
    shape_wkt = models.MultiLineStringField(null=False, geography=True)
    fabricated_type_code = models.BigIntegerField(null=True)
    pref = models.CharField(max_length=4000, null=True)

    created_by = models.CharField(max_length=4000, null=True)
    created_at = models.DateTimeField(null=True)

    updated_by = models.CharField(max_length=4000, null=True)
    updated_at = models.DateTimeField(null=True)
