from django.db import models


class Category(models.Model):
    class Meta:
        db_table = 'categories'

    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=1000, unique=True)
    created_at = models.DateTimeField('date published')
    updated_at = models.DateTimeField('date published')

    def __str__(self):
        return self.category_id
