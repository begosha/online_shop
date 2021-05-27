from rest_framework import serializers
from shop.models import OrderProducts
from .products import ProductListSerializer

class OrdersSerializer(serializers.ModelSerializer):
    product = ProductListSerializer()
    class Meta:
        model = OrderProducts
        fields = ('id', 'product', 'quantity')
        read_only_fields = ('id',)

class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProducts
        fields = ('id', 'product', 'quantity')
        read_only_fields = ('id',)
