import uuid
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

class Dealer(models.Model):
    company_name = models.CharField(max_length=100, blank=False,unique=True)
    phone_number = PhoneNumberField(blank=False, unique=True)
    email = models.EmailField(max_length=100, blank=False)
    address = models.TextField(blank=False)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id}-{self.company_name}-{self.email}-{self.phone_number}-{self.address}'

class Item(models.Model):
    title = models.CharField(max_length=100, blank=False)
    category = models.CharField(max_length=100, blank=False, default=None)
    seller_id = models.ForeignKey(Dealer, on_delete = models.CASCADE)
    product_description = models.TextField(blank=False)
    brand = models.CharField(max_length=50, blank=False)
    manufacturer = models.CharField(max_length=50, blank=False)
    quantity = models.PositiveIntegerField(blank=False, default=None)
    item_height = models.PositiveSmallIntegerField(blank=False)
    item_width = models.PositiveSmallIntegerField(blank=False)
    item_length = models.PositiveSmallIntegerField(blank=False)
    item_price = models.DecimalField(max_digits= 8, decimal_places=2, blank=False)
    

    def __str__(self):
        return f'{self.id}-{self.title}-{self.brand}-{self.category}'


class Cart(models.Model):
    cart_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart_user", default=None)
    cart_item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="cart_item", default=None)
    quantity = models.PositiveSmallIntegerField(blank=False, default=None)

    def __str__(self):
        return f'{self.id}-{self.cart_user}'
