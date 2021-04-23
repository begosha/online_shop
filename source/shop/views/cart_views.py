from django.shortcuts import render, get_object_or_404, redirect
from shop.models import Product, Category, CartItem, OrderProducts, Order
from ..forms import OrderForm
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView, View
from django.views.generic.edit import FormMixin
from decimal import Decimal
from django.contrib.sessions.models import Session



class CartView(ListView, FormMixin):
    template_name = 'cart/cart.html'
    context_object_name = 'cart_products'
    paginate_by = 5
    paginate_orphans = 2
    form_class = OrderForm

    def get_queryset(self):
        queryset = []
        carts = self.request.session.get('cart', {})
        print(carts)
        for id, count in carts.items():
            product = {}
            product['product'] = Product.objects.get(pk=id)
            product['count'] = count
            queryset.append(product)
        return queryset




class CartAddProductView(CreateView):
    model = Product
    redirect_url = '/products/'

    def post(self, request, *args, **kwargs):
        cart = request.session.get('cart', {})
        if not cart:
            cart = request.session['cart'] = {}
        product = Product.objects.get(id=kwargs.get('pk'))
        quantity = int(request.POST.get('quantity'))
        if quantity <= product.remainder:
            try:
                product.remainder = product.remainder - quantity
                product.save()
                product_count = cart[str(product.id)]
                cart[str(product.id)] = product_count + quantity
            except KeyError:
                product.remainder = product.remainder - quantity
                product.save()
                cart[str(product.id)] = quantity
            request.session['cart'] = cart
        else:
            return redirect(self.redirect_url)
        return redirect(self.redirect_url)


class CartDeleteProductView(DeleteView):
    model = CartItem
    redirect_url = '/products/'

    def post(self, request, *args, **kwargs):
        product = Product.objects.get(id=kwargs.get('pk'))
        cart_item = CartItem.objects.get(item=product)
        if cart_item.quantity == 1:
            cart_item.delete()
            product.remainder += 1
            product.save()
        else:
            cart_item.quantity = cart_item.quantity - 1
            cart_item.save()
            product.remainder += cart_item.quantity
            product.save()
        return redirect(self.redirect_url)







