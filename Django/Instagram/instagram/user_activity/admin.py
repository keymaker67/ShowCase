from django.contrib import admin
from django.contrib.admin.decorators import register

from .models import LikeModel, CommentModel


# Register and Create admin classes
@register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'created_date', 'updated_date', 'get_like_count')
    list_display_links = ('comment', )
    list_filter = ('created_date', )
    search_fields = ('comment', )
    date_hierarchy = 'created_date'


@register(LikeModel)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('created_date', 'updated_date', )
    date_hierarchy = 'created_date'

