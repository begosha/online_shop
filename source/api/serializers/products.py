from rest_framework import serializers
from shop.models import Product
from .categories import CategorySerializer

class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'price')
        read_only_fields = ('id',)


class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'category', 'remainder', 'price')
        read_only_fields = ('id',)

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("__all__")
        read_only_fields = ('id',)