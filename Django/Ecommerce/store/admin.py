from django.contrib import admin

from .models import CategoryModel, ProductModel


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'is_active', 'created_at', 'modified_at']
    prepopulated_fields = {'slug': ('name', )}
    list_display_links = ['name']
    list_filter = ['name', 'is_active', 'created_at', 'modified_at']


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'category',
        'creator',
        'price',
        'in_stock',
        'slug',
        'is_active',
        'created_at',
        'modified_at',
    ]
    prepopulated_fields = {'slug': ('title', )}
    list_editable = ['price', 'in_stock', 'is_active']
    list_filter = ['in_stock', 'is_active']
