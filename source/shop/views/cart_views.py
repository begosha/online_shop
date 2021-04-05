from django.shortcuts import render, get_object_or_404, redirect
from ..models import Product, Category, CartItem, OrderProducts, Order
from ..forms import CartForm
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView, View
from django.db.models import Q
from django.utils.http import urlencode



class CartAddProductView(CreateView):
    model = CartItem
    redirect_url = '/products/'

    def post(self, request, *args, **kwargs):
        product = Product.objects.get(id=kwargs.get('pk'))
        try:
            cart_item = CartItem.objects.get(item=product)
            if cart_item.quantity <= product.remainder:
                quantity = request.POST.get('quantity')
                cart_item.quantity += int(quantity)
                product.remainder -= int(quantity)
                cart_item.save(force_update=True)
        except CartItem.DoesNotExist:
            CartItem.objects.create(
                item=product,
                quantity=1
            )
        return redirect(self.redirect_url)







