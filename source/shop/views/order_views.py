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
        queryset = []
        for order in Order.objects.filter(user_order=self.request.user.id):
            total = 0
            for product_order in order.order.all():
                total += product_order.order_total()
            queryset.append((order,total))
        print(queryset)
        return queryset


class MakeOrderView(CreateView):
    form_class = OrderForm
    model = OrderProducts

    def form_valid(self, form, **kwargs):
        order = Order()
        try:
            order.user_order=self.request.user
        except ValueError:
            order.user_order=None
        cart = self.request.session.get('cart')
        for key, value in form.cleaned_data.items():
            setattr(order, key, value)
        order.save()
        for id in cart:
            store_product = Product.objects.get(pk=id)
            make_order = OrderProducts()
            product = store_product
            make_order.product = product
            make_order.quantity=cart[str(product.id)]
            store_product.remainder -= int(make_order.quantity)
            make_order.order = order
            make_order.save()
            store_product.save()
        self.request.session['cart'] = {}
        return self.get_success_url()

    def get_success_url(self):
        return redirect('index')