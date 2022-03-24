from django.contrib.gis.db import models


class PipeLine(models.Model):
    class Meta:
        db_table = 'pipeline'

    housing_area_code = models.BigIntegerField(null=False)
    upper_facility_key = models.CharField(max_length=4000, null=True)
    lower_facility_key = models.CharField(max_length=4000, null=True)
    facility_type = models.MultiLineStringField(null=False, geography=True)
    fabricated_type_code = models.BigIntegerField(null=True)
    pref = models.CharField(max_length=4000, null=True)

    created_by = models.CharField(max_length=4000, null=True)
    created_at = models.DateTimeField(null=True)

    updated_by = models.CharField(max_length=4000, null=True)
    updated_at = models.DateTimeField(null=True)
