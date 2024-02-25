from django.contrib import admin
from django.contrib.admin import register

from .models import OrderItemModel, OrderModel


# Admin actions
@admin.action(description='Activate selected items')
def activate_selected_items(self, request, queryset):
    queryset.update(is_active=True)


@admin.action(description='Deactivate selected items')
def deactivate_selected_items(self, request, queryset):
    queryset.update(is_active=False)


# Register your models here.
@register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'user',
        'is_active',
        'created_date',
        'updated_date',
    )
    list_display_links = (
        'id',
        'title',
    )
    list_filter = (
        'id',
        'title',
        'user',
        'is_active',
        'created_date',
        'updated_date',
    )
    search_fields = (
        'title',
        'user',
    )

    actions = (
        activate_selected_items,
        deactivate_selected_items,
    )


@register(OrderItemModel)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'product',
        'order',
        'quantity',
        'is_active',
        'created_date',
        'updated_date',
    )
    list_display_links = (
        'id',
        'product',
        'order',
    )
    list_filter = (
        'product',
        'order',
        'quantity',
        'is_active',
        'created_date',
        'updated_date',
    )
    search_fields = (
        'title',
        'order',
    )

    actions = (
        activate_selected_items,
        deactivate_selected_items,
    )
