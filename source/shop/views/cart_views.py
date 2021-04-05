from django.shortcuts import render, get_object_or_404, redirect
from ..models import Product, Category, CartItem, OrderProducts, Order
from ..forms import SimpleSearchForm
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView, View
from django.db.models import Q
from django.utils.http import urlencode

class CartView(ListView):
    template_name = 'cart/cart.html'
    context_object_name = 'cart_products'
    model = CartItem
    paginate_by = 5
    paginate_orphans = 2


    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(item__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


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







