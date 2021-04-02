from django.contrib import admin
from django.apps import apps
from .models import Product, OrderProducts, Category, CartItem, Order

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category']
    list_filter = ['category']
    search_fields = ['category']
    fields = ['category']

class CartItemAdmin(admin.ModelAdmin):
    list_display = ['item', 'quantity']
    list_filter = ['item']
    search_fields = ['item']
    fields = ['item', 'quantity']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description','category','remainder', 'price']
    list_filter = ['name']
    search_fields = ['name', 'category']
    fields = ['id', 'name', 'description','category','remainder', 'price']
    readonly_fields = ['id']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'phone', 'address', 'created_at']
    list_filter = ['user_name']
    search_fields = ['user_name']
    fields =  ['id', 'user_name', 'phone', 'address', 'created_at']
    readonly_fields = ['id', 'created_at']

class OrderProductsAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'order']
    list_filter = ['product']
    search_fields = ['product']
    fields = ['id','product', 'quantity', 'order']
    readonly_fields = ['id']

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(OrderProducts, OrderProductsAdmin)

