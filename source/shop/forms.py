from django import forms
from .models import (Product, Category, CartItem, Order)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        status = forms.ModelChoiceField(queryset=Category.objects.all())
        fields = ('name','description', 'category', 'remainder', 'price')

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('user_name','phone', 'address')


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Search")