from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=20)
    tel = models.CharField(max_length=20)
    addr = models.CharField(max_length=100)
