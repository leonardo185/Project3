from django.db import models
from accounts.models import Item

# Create your models here.

class Cart(models.Model):
    user = models.IntegerField()
    item = models.IntegerField(default=None)
    quantity = models.PositiveIntegerField(default=None)

    def __str__(self):
        return f'{self.id}-{self.user}-{self.item}-{self.quantity}'
