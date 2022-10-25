from dataclasses import fields
from rest_framework import serializers 
from .models import Category,Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            'name',
            'get_absolute_url',
            'description',
            'price',
            'get_image',
            'thumbnail'
        )
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields=(
            'id',
            'name',
            'get_absolute_url',
            'products',
        )