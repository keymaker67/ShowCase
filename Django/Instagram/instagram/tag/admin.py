from django.contrib import admin
from django.contrib.admin.decorators import register

from .models import TagModel


# Register Tag model and create admin
@register(TagModel)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'object_id', 'content_type', 'content_object', )
    list_display_links = ('title', 'object_id', 'content_type', 'content_object', )
    list_filter = ('title', )
    search_fields = ('title', 'object_id', 'content_type', 'content_object', )
    date_hierarchy = 'created_date'
