from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (IndexView, ProductView, ProductDeleteView, ProductUpdateView, ProductCreateView, CartAddProductView, CartView, CartDeleteProductView, MakeOrderView, OrderList)


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cart', CartView.as_view(), name='cart'),
    path('<int:pk>/product', ProductView.as_view(), name='product'),
    path('add/', ProductCreateView.as_view(), name='product-add'),
    path('<int:pk>/update', ProductUpdateView.as_view(), name='product-update'),
    path('<int:pk>/delete', ProductDeleteView.as_view(), name='product-delete'),
    path('<int:pk>/delete/cart', CartDeleteProductView.as_view(), name='cart-delete'),
    path('<int:pk>/add/cart', CartAddProductView.as_view(), name='cart-add'),
    path('order', MakeOrderView.as_view(), name='order'),
    path('order/list', OrderList.as_view(), name='order-list')
]