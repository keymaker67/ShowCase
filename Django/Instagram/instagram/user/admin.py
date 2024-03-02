from django.contrib import admin
from django.contrib.admin import register

from .models import (
    UserProfileModel, UserRelationModel, CloseFriendModel
)


@admin.action(description='Activate selected items')
def activate_selected_items(self, request, queryset):
    queryset.update(is_active=True)


@admin.action(description='Deactivate selected items')
def deactivate_selected_items(self, request, queryset):
    queryset.update(is_active=False)


@register(UserProfileModel)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'public', 'location')
    list_filter = ('public', 'location')
    search_fields = ('user', 'location', 'user__username', 'user__first_name', 'user__last_name')
    list_display_links = ('user', )
    date_hierarchy = 'created_date'

    actions = (
        activate_selected_items,
        deactivate_selected_items,
    )


@register(UserRelationModel)
class UserRelationAdmin(admin.ModelAdmin):
    list_display = ('user', 'related_with', 'relation_type', )
    list_filter = ('user', 'related_with', 'relation_type', )
    search_fields = (
        'user', 'user__username', 'user__first_name', 'user__last_name',
        'related_with', 'relation_type',
    )
    list_display_links = ('user', 'related_with', 'relation_type', )
    date_hierarchy = 'created_date'

    actions = (
        activate_selected_items,
        deactivate_selected_items,
    )


@register(CloseFriendModel)
class CloseFriendAdmin(admin.ModelAdmin):
    list_display = ('close_friend', )
    list_filter = ('close_friend', )
    search_fields = ('close_friend', )
    list_display_links = ('close_friend', )
    date_hierarchy = 'created_date'

    actions = (
        activate_selected_items,
        deactivate_selected_items,
    )
