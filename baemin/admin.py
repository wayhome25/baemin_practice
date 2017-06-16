from django.contrib import admin
from .models import Item, Shop

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'tel']
    list_display_links = ['name']


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'shop', 'name', 'price']
    list_display_links = ['shop', 'name']
