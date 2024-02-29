from django.contrib import admin
from django.contrib.admin.decorators import register

from .models import LikeModel, CommentModel


# Register and Create admin classes
@register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'user', 'post', 'story', )
    list_display_links = ('comment', 'user', 'post', 'story', )
    list_filter = ('user', )
    search_fields = ('comment', 'user', 'post', 'story', )