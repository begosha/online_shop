from django.urls import path, include
from rest_framework import routers
from .views import ProductListView, ProductDetailView, ProductCreateView, OrderListView, OrderCreateView

app_name='api_v1'

api_urls = [
    path('', ProductListView.as_view(), name='index'),
    path('orders', OrderListView.as_view(), name='orders'),
    path('create-orders', OrderCreateView.as_view(), name='orders_create'),
    path('create', ProductCreateView.as_view(), name='create'),
    path('<int:pk>/', ProductDetailView.as_view(), name='detail')
]

urlpatterns = [
    path('products/', include(api_urls)),
]