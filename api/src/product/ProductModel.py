from django.db import models
from api.src.category.CategoryModel import Category


class Product(models.Model):
    class Meta:
        db_table = 'products'

    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=1000)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField('date published')
    updated_at = models.DateTimeField('date published')
