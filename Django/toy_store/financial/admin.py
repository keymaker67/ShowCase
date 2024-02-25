from django.contrib import admin
from django.contrib.admin import register

from .models import PaymentModel


# Admin actions
@admin.action(description='Activate selected items')
def activate_selected_items(self, request, queryset):
    queryset.update(is_active=True)


@admin.action(description='Deactivate selected items')
def deactivate_selected_items(self, request, queryset):
    queryset.update(is_active=False)


# Register your models here.
@register(PaymentModel)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'order',
        'is_active',
        'payment',
        'created_date',
    )
    list_display_links = (
        'id',
        'user',
    )
    list_filter = (
        'is_active',
        'created_date',
        'updated_date',
        'id',
        'user',
    )
    search_fields = (
        'user',
        'order',
    )
    
    actions = (
        activate_selected_items,
        deactivate_selected_items,
    )
