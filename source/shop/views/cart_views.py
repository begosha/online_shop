from django.shortcuts import render, get_object_or_404, redirect
from shop.models import Product, Category, CartItem, OrderProducts, Order
from ..forms import OrderForm
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView, View
from django.views.generic.edit import FormMixin

class CartView(ListView, FormMixin):
    template_name = 'cart/cart.html'
    context_object_name = 'cart_products'
    model = CartItem
    paginate_by = 5
    paginate_orphans = 2
    form_class = OrderForm





class CartAddProductView(CreateView):
    model = CartItem
    redirect_url = '/products/'

    def post(self, request, *args, **kwargs):
        product = Product.objects.get(id=kwargs.get('pk'))
        print(product)
        quantity = int(request.POST.get('quantity'))
        if quantity <= product.remainder:
            try:
                cart_item = CartItem.objects.get(item=product)
                cart_item.quantity += quantity
                product.remainder = product.remainder - quantity
                cart_item.save()
                product.save()
            except CartItem.DoesNotExist:
                CartItem.objects.create(
                    item=product,
                    quantity=quantity
                )
                product.remainder = product.remainder - quantity
                product.save()
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







