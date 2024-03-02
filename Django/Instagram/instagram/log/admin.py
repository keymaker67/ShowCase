from django.contrib import admin
from django.contrib.admin.decorators import register

from .models import PreviewModel


# Create Preview admin and register it
@register(PreviewModel)
class PreviewAdmin(admin.ModelAdmin):
    list_display = ('object_id', 'content_type', 'content_object', 'created_date', )
    list_display_links = ('object_id', 'content_type', 'content_object', 'created_date', )
    search_fields = ('object_id', 'content_type', 'content_object', 'created_date', )
    date_hierarchy = 'created_date'
