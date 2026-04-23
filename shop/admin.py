from django.contrib import admin

# Register your models here.

from django.contrib import admin
from shop.models import Product, ContactMessage

class ShopAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, ShopAdmin)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp', 'message')
    # This makes sure the team can only edit the response field
    fields = ('user', 'message', 'admin_response', 'timestamp')
    readonly_fields = ('user', 'message', 'timestamp')