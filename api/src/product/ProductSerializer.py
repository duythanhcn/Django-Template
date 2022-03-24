from rest_framework import serializers
from api.src.product.ProductModel import Product
from api.src.category.CategoryModel import Category
from api.src.category.CategorySerializer import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

    product_id = serializers.IntegerField(read_only=True)
    product_name = serializers.CharField(max_length=1000)
    category = CategorySerializer()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
