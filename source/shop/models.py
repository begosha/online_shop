from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model

class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Product Name')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Product Description')
    category = models.ForeignKey('shop.Category', related_name='product_category', on_delete=models.PROTECT,verbose_name='Product Category', null=False, blank=False)
    remainder = models.IntegerField(validators=(MinValueValidator(0),), verbose_name='Product Remainder')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Product Price')

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return "{}. {}".format(self.pk, self.name)


class Category(models.Model):
    category = models.CharField(max_length=15, null=False, blank=False, verbose_name='Category')

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category

class CartItem(models.Model):
    item = models.ForeignKey('shop.Product', related_name='cart_product', on_delete=models.CASCADE,verbose_name='Product in Cart', null=False, blank=False)
    quantity = models.IntegerField(validators=(MinValueValidator(0),), verbose_name='Quantity of item')

    class Meta:
        db_table = 'items'
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return "{} {}".format(self.item, self.quantity)

class Order(models.Model):
    user_order = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        related_name='order'
    )
    user_name = models.CharField(max_length=20, null=False, blank=False, verbose_name='User Name')
    phone = models.CharField(max_length=25, null=False, blank=False, verbose_name='User Phone Number')
    address = models.CharField(max_length=150, null=False, blank=False, verbose_name='User Address')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'order'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return "{} {} {} {}".format(self.pk, self.user_name, self.phone, self.address)

class OrderProducts(models.Model):
    product = models.ForeignKey('shop.Product', related_name='order_product', on_delete=models.CASCADE,  verbose_name='Product to Buy', null=False, blank=False)
    quantity = models.IntegerField(validators=(MinValueValidator(0),), verbose_name='Product Quantity')
    order = models.ForeignKey('shop.Order', related_name='order', on_delete=models.CASCADE, verbose_name='Order', null=False, blank=False)

    class Meta:
        db_table = 'order_products'
        verbose_name = 'Order_Product'
        verbose_name_plural = 'Order_Products'

    def __str__(self):
        return "Id:{}, Product: {}, Quantity: {},Order: {}".format(self.pk, self.product, self.quantity, self.order.pk)

    def order_total(self):
        return self.quantity * self.product.price