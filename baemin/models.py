from django.conf import settings
from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=20)
    tel = models.CharField(max_length=20)
    addr = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Item(models.Model):
    shop = models.ForeignKey(Shop)
    name = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    shop = models.ForeignKey(Shop)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    item_set = models.ManyToManyField(Item)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    @property
    def total(self):
        return sum(item.price for item in self.item_set.all())
