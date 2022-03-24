from rest_framework import serializers
from api.src.category.CategoryModel import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_id', 'category_name', 'created_at', 'updated_at']

    category_id = serializers.IntegerField(read_only=True)
    category_name = serializers.CharField(max_length=1000)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
