from django.shortcuts import render, get_object_or_404, redirect
from shop.models import Product
from ..forms import OrderForm
from django.views.generic import ListView, DeleteView, CreateView, View
from django.views.generic.edit import FormMixin
from django.contrib.sessions.models import Session
from django.contrib import messages

class CartView(ListView, FormMixin):
    template_name = 'cart/cart.html'
    context_object_name = 'cart_products'
    paginate_by = 5
    paginate_orphans = 2
    form_class = OrderForm

    def get_queryset(self):
        queryset = []
        total = 0
        carts = self.request.session.get('cart', {})
        for id, count in carts.items():
            product = {}
            product['product'] = Product.objects.get(pk=id)
            product['count'] = count
            total += Product.objects.get(pk=id).price * count
            queryset.append(product)
        queryset.append(total)
        return queryset


class CartAddProductView(CreateView):
    model = Product
    redirect_url = '/products/'

    def post(self, request, *args, **kwargs):
        cart = self.get_cart()
        product = Product.objects.get(id=kwargs.get('pk'))
        quantity = int(request.POST.get('quantity'))
        if quantity <= product.remainder:
            try:
                product_count = cart[str(product.id)]
                cart[str(product.id)] = product_count + quantity
            except KeyError:
                cart[str(product.id)] = quantity
            request.session['cart'] = cart
            messages.add_message(request, messages.SUCCESS, f'Added {quantity} {product.name} to your cart!')
        else:
            messages.add_message(request, messages.ERROR, f'The quantity of {product.name} in our storage is less than your desirable amount :(')
            return redirect(self.redirect_url)
        return redirect(self.redirect_url)

    def get_cart(self):
        cart = self.request.session.get('cart', {})
        if not cart:
            cart = self.request.session['cart'] = {}
        return cart

class CartDeleteProductView(DeleteView):
    model = Product
    redirect_url = '/products/cart'

    def get_cart(self):
        cart = self.request.session.get('cart')
        if not cart:
            cart = self.request.session['cart'] = {}
        return cart

    def post(self, request, *args, **kwargs):
        product = Product.objects.get(id=kwargs.get('pk'))
        cart = self.get_cart()
        quantity = int(request.POST.get('quantity'))
        if quantity <= cart[str(product.id)]:
            if cart[str(product.id)] == 1:
                del cart[str(product.id)]
            else:
                cart[str(product.id)] = cart[str(product.id)] - quantity
            request.session['cart'] = cart
            messages.add_message(request, messages.WARNING, f'{quantity} {product.name} products have/s been removed!')
        else:
            messages.add_message(request, messages.ERROR, f'The quantity of {product.name} in your cart is less than you want to remove!')
            
            return redirect(self.redirect_url)
        return redirect(self.redirect_url)







