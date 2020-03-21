from django.db import models
from accounts.models import Item


# Create your models here.

class Cart(models.Model):
    user = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default=None, blank=True, related_name="cart_item")
    quantity = models.PositiveIntegerField(default=None)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id}-{self.user}-{self.item}-{self.quantity}'

class Orders(models.Model):
    user = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.DecimalField(max_digits=6, decimal_places=0)
    order_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}-{self.user}-{self.order_date}'
