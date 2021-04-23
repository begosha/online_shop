from django.shortcuts import render, get_object_or_404, redirect
from shop.models import Product, Category, CartItem, OrderProducts, Order
from ..forms import OrderForm
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, View
from django.contrib.auth import get_user_model


class OrderList(ListView):
    template_name = 'order/orders.html'
    context_object_name = 'orders'
    model = Order
    paginate_by = 5
    paginate_orphans = 2
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user_order=self.request.user.id)
        return queryset


class MakeOrderView(CreateView):
    form_class = OrderForm
    model = OrderProducts

    def form_valid(self, form, **kwargs):
        order = Order()
        order.user_order=self.request.user
        cart = self.request.session.get('cart')
        for key, value in form.cleaned_data.items():
            setattr(order, key, value)
        order.save()
        print(order)
        for id in cart:
            make_order = OrderProducts()
            product = Product.objects.get(pk=id)
            make_order.product = product
            make_order.quantity=cart[str(product.id)]
            make_order.order = order
            make_order.save()
        self.request.session['cart'] = {}
        return self.get_success_url()

    def get_success_url(self):
        return redirect('index')