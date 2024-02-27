from django.contrib import admin
from django.contrib.admin import register

from .models import UserProfile


@admin.action(description='Activate selected items')
def activate_selected_items(self, request, queryset):
    queryset.update(is_active=True)


@admin.action(description='Deactivate selected items')
def deactivate_selected_items(self, request, queryset):
    queryset.update(is_active=False)


@register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'public', 'location')
    list_filter = ('public', 'location')
    search_fields = ('user', 'location', 'user__username', 'user__first_name', 'user__last_name')
    list_display_links = ('user', )

    actions = (
        activate_selected_items,
        deactivate_selected_items,
    )
