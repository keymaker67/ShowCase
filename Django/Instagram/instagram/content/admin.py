from django.contrib import admin
from django.contrib.admin.decorators import register

from .models import (
    PostModel, MediaModel, StoryModel, MentionModel
)


# Create inline classes
class MediaInline(admin.TabularInline):
    model = MediaModel
    extra = 1


class MentionInline(admin.TabularInline):
    model = MentionModel
    extra = 1


# Create admin classes
@register(PostModel)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'allow_comments', 'show_like', 'close_friends_only', 'caption',
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

    inlines = [MediaInline, MentionInline]


@register(MentionModel)
class MentionAdmin(admin.ModelAdmin):
    list_display = ('post', 'story', 'user', )
    list_display_links = ('post', 'story', 'user', )
    list_filter = ('post', 'story', 'user', )
    search_fields = ('user__username', 'post__caption', )
    date_hierarchy = 'created_date'


@register(StoryModel)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'allow_comments', 'close_friends_only', )
    list_display_links = ('user', )
    list_filter = ('user', 'close_friends_only', 'allow_comments')
    search_fields = ('user__username', 'post__caption', )
    date_hierarchy = 'created_date'

    inlines = [MediaInline, MentionInline, ]


@register(MediaModel)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('post', 'story', 'media_file', 'media_type', )
    list_display_links = ('post', )
    list_filter = ('post', 'media_type', )
    search_fields = ('media_type', 'post__caption', )
    date_hierarchy = 'created_date'
