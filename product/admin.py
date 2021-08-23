from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'producer', 'manufacture_date', 'expiration_date')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'producer')


admin.site.register(Product, ProductAdmin)
