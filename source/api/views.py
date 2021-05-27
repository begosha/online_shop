from django.shortcuts import render
from rest_framework import generics
from shop.models import Product, OrderProducts, Order
from .serializers.products import ProductListSerializer, ProductDetailSerializer, ProductCreateSerializer
from .serializers.order_details import OrderDetailsSerializer, OrderCreateSerializer

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductCreateSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()

class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailsSerializer

class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderCreateSerializer
