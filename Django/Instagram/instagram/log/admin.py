from django.contrib import admin
from django.contrib.admin.decorators import register

from .models import PreviewModel


# Create Preview admin and register it
@register(PreviewModel)
class PreviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile', 'story', 'post', )
    list_display_links = ('user', 'profile', 'story', 'post', )
    list_filter = ('user', )
    search_fields = ('user', 'post', 'story', 'profile')
