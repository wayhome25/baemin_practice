from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=20)
    tel = models.CharField(max_length=20)
    addr = models.CharField(max_length=100)

class Item(models.Model):
    shop = models.ForeignKey(Shop)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    
