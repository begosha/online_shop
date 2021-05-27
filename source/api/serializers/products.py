from rest_framework import serializers
from shop.models import Product
from .categories import CategorySerializer

class ProductListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'category', 'remainder', 'price')
        read_only_fields = ('id',)