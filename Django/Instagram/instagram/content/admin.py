from django.contrib import admin
from django.contrib.admin.decorators import register
from django.template.loader import render_to_string
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import (
    PostModel, MediaModel, StoryModel, MentionModel
)
from tag.models import TagModel


# Create inline classes
class MediaInline(GenericTabularInline):
    model = MediaModel
    extra = 1


class MentionInline(GenericTabularInline):
    model = MentionModel
    extra = 1


class TagInline(GenericTabularInline):
    model = TagModel
    extra = 1


# Create admin classes
@register(PostModel)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'allow_comments', 'show_like', 'close_friends_only',
        'caption', 'created_date', 'updated_date', 'like_count', 'comment_count',
    )
    list_display_links = ('user', )
    list_filter = ('user', )
    search_fields = ('user__username', 'caption', )
    date_hierarchy = 'created_date'
    fieldsets = (
        ('Main Info', {'fields': ('user', 'caption')}),
        ('Additional Info', {
            'fields': ('allow_comments', 'show_like', 'close_friends_only')
        })
    )

    inlines = [MediaInline, MentionInline, TagInline, ]


@register(MentionModel)
class MentionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_date', 'object_id', 'content_type', 'content_object')
    list_display_links = ('user', 'id', 'object_id', 'content_type', 'content_object')
    list_filter = ('user', 'created_date')
    search_fields = ('user__username', 'post__caption', 'object_id', 'content_type', 'content_object')
    date_hierarchy = 'created_date'


@register(StoryModel)
class StoryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'allow_comments', 'close_friends_only',
        'created_date', 'updated_date', 'like_count', 'comment_count',
    )
    list_display_links = ('user', )
    list_filter = ('user', 'close_friends_only', 'allow_comments')
    search_fields = ('user__username', 'post__caption', )
    date_hierarchy = 'created_date'

    inlines = [MediaInline, MentionInline, TagInline, ]


@register(MediaModel)
class MediaAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'display_media_link', 'media_type', 'created_date',
        'object_id', 'content_type', 'content_object'
    )
    list_display_links = ('media_type', 'object_id', 'content_type', 'content_object')
    list_filter = ('created_date', 'media_type', )
    search_fields = ('media_type', )
    date_hierarchy = 'created_date'

    def display_media_link(self, obj):
        # Define a custom method to render the media file link using a template
        if obj.media_file:
            return render_to_string('media/media_file_link.html', {'obj': obj})
        else:
            return '-'

    display_media_link.allow_tags = True
    display_media_link.short_description = 'Media File'
