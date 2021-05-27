import itertools
from rest_framework import serializers
from shop.models import Order, OrderProducts
from .orders import OrderListSerializer, OrdersSerializer
from .products import ProductDetailSerializer, ProductListSerializer

class OrderDetailsSerializer(serializers.ModelSerializer):
    order = OrdersSerializer(many=True)
    class Meta:
        model = Order
        fields = ('id', 'user_order', 'user_name', 'phone', 'address', 'created_at', 'order')
        read_only_fields = ('id', 'created_at')

class OrderCreateSerializer(serializers.ModelSerializer):
    order = OrderListSerializer(many=True)

    class Meta:
        model = Order
        fields = ('user_order', 'user_name', 'phone', 'address', 'order')
        read_only_fields = ('id', 'created_at')

    def create(self, validated_data):
        order_data = validated_data.pop('order')
        print(order_data)
        instance = Order.objects.create(**validated_data)
        for i in order_data:
            product = i['product']
            qty = i['quantity']
            OrderProducts.objects.create(product=product, quantity=qty, order=instance)

        validated_data['order'] = order_data
        return validated_data


