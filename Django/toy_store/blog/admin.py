from django.contrib import admin
from django.contrib.admin import register
from django.template.loader import render_to_string

from .models import (
    CategoryModel,
    PostModel,
    CommentModel,
    MediaModel
)

INLINE_MAX_NUM = 1


class CommentInline(admin.StackedInline):
    model = CommentModel
    max_num = INLINE_MAX_NUM


class MediaInline(admin.StackedInline):
    model = MediaModel
    max_num = INLINE_MAX_NUM


class PostInline(admin.StackedInline):
    model = PostModel
    max_num = INLINE_MAX_NUM


# Admin actions
@admin.action(description='Activate selected items')
def activate_selected_items(self, request, queryset):
    queryset.update(is_active=True)


@admin.action(description='Deactivate selected items')
def deactivate_selected_items(self, request, queryset):
    queryset.update(is_active=False)


# Register your models here.
@register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'is_active',
        'created_date',
        'updated_date'
    )
    list_display_links = (
        'id',
        'title'
    )
    list_filter = (
        'is_active',
        'created_date',
        'updated_date',
        'id',
        'title'
    )
    search_fields = (
        'title',
        'description'
    )

    actions = (
        activate_selected_items,
        deactivate_selected_items,
    )

    inlines = [PostInline, ]



@register(MediaModel)
class MediaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'media_type',
        'display_media_file_link',  # Add custom method to display media file link
        'post',
        'is_active',
        'created_date',
        'updated_date'
    )
    list_display_links = (
        'id',
        'title'
    )
    list_filter = (
        'id',
        'title',
        'is_active',
        'created_date',
        'updated_date',
    )
    search_fields = (
        'title',
        'description'
    )

    actions = (
        activate_selected_items,
        deactivate_selected_items,
    )

    def display_media_file_link(self, obj):
        # Define a custom method to render the media file link using a template
        if obj.media_file:
            return render_to_string('media_file_link.html', {'obj': obj})
        else:
            return '-'  # Display '-' if no media file is available

    display_media_file_link.allow_tags = True
    display_media_file_link.short_description = 'Media File'  # Set column header


@register(PostModel)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'the_post',
        'category',
        'is_active',
        'created_date',
        'updated_date'
    )
    list_display_links = (
        'id',
        'title'
    )
    list_filter = (
        'id',
        'title',
        'is_active',
        'created_date',
        'updated_date',
    )
    search_fields = (
        'title',
        'the_post',
        'category__title',
        'category__description'
    )

    actions = (
        activate_selected_items,
        deactivate_selected_items,
    )

    inlines = [MediaInline, CommentInline]


@register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'user',
        'post',
        'is_active',
        'created_date',
        'updated_date'
    )
    list_display_links = (
        'id',
        'title'
    )
    list_filter = (
        'is_active',
        'created_date',
        'updated_date',
        'id',
        'title',
        'user'
    )
    search_fields = (
        'title',
        'comment_body',
        'user'
    )

    actions = (
        activate_selected_items,
        deactivate_selected_items,
    )
