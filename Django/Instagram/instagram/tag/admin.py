from django.contrib import admin
from django.contrib.admin.decorators import register

from .models import TagModel


# Register Tag model and create admin
@register(TagModel)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'post', 'story', )
    list_display_links = ('title', 'user', 'post', 'story', )
    list_filter = ('user', 'post', 'story', )
    search_fields = ('title', 'user__username', 'post', 'story', )
    date_hierarchy = 'created_date'
