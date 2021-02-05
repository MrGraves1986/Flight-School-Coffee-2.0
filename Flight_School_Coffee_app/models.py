from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

class Coffees(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=255, null=True)
    roast = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Styles(models.Model):
    style_name = models.CharField(max_length=20)
    style_for_coffee = models.ManyToManyField(Coffees, related_name="coffee_style")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Sizes(models.Model):
    order_size = models.IntegerField()
    size_for_coffee = models.ManyToManyField(Coffees, related_name="coffee_size")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Customers(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    street_address = models.CharField(max_length=255)
    address_two = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    zip_code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# This class combines the coffee with the size and style to place it in the cart. A shopping cart order can have multiple instances of this class.
class SingleCartItems(models.Model):
    ordered_coffee = models.ForeignKey(Coffees, related_name="coffee_selected", on_delete = models.CASCADE)
    ordered_style = models.ForeignKey(Styles, related_name="style_selected", on_delete = models.CASCADE)
    ordered_size = models.ForeignKey(Sizes, related_name="size_selected", on_delete = models.CASCADE)
    order_price = models.DecimalField(decimal_places=2, max_digits=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# This class is for all of the items in the shopping cart and then links that to the customer.
class TotalCartItems(models.Model):
    cart_item = models.ForeignKey(SingleCartItems, related_name="shopping_cart", on_delete=models.CASCADE)
    total_price = models.DecimalField(decimal_places=2, max_digits=5)
    ordered_by = models.ForeignKey(Customers, related_name="order", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

