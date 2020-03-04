from django.contrib import admin
from .models import Profile, Dealer, Item, Cart

# Register your models here.
admin.site.register(Profile)
admin.site.register(Dealer)
admin.site.register(Item)
admin.site.register(Cart)
