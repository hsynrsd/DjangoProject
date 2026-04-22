from django.contrib import admin

# Register your models here.

from django.contrib import admin
from shop.models import Product

class ShopAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, ShopAdmin)
