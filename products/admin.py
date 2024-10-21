from django.contrib import admin
from .models import Product, Category


# Category Admin Class
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'friendly_name')


# Product Admin Class
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'description', 'image')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)


# Register the models with the admin site
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
