from django.shortcuts import render, get_object_or_404, redirect
from shop.models import Product, Category, CartItem, OrderProducts, Order
from ..forms import OrderForm
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView, View
from django.views.generic.edit import FormMixin


class MakeOrderView(CreateView):
    form_class = OrderForm
    model = OrderProducts


    def form_valid(self, form, **kwargs):
        order = Order()
        make_order = OrderProducts()
        for key, value in form.cleaned_data.items():
            setattr(order, key, value)
        order.save()
        make_order.order = order
        for item in CartItem.objects.all():
            make_order = OrderProducts()
            make_order.order = order
            make_order.product = item.item
            make_order.quantity=item.quantity
            make_order.save()
        CartItem.objects.all().delete()
        return self.get_success_url()

    def get_success_url(self):
        return redirect('index')