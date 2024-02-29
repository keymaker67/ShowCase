from django.contrib import admin
from django.contrib.admin import register
from django.utils.html import format_html
from django.template.loader import render_to_string

from .models import (
    CategoryModel,
    ProductModel,
    CommentModel,
    MediaModel,
    PriceModel,
)

INLINE_MAX_NUM = 1


class MediaInline(admin.StackedInline):
    model = MediaModel
    max_num = INLINE_MAX_NUM


class ProductInline(admin.StackedInline):
    model = ProductModel
    max_num = INLINE_MAX_NUM


class CommentInline(admin.StackedInline):
    model = CommentModel
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
        'updated_date',
    )
    list_display_links = (
        'id',
        'title',
    )
    list_filter = (
        'is_active',
        'created_date',
        'updated_date',
        'id',
        'title',
    )
    search_fields = (
        'title',
        'description',
    )

    actions = (
        activate_selected_items,
        deactivate_selected_items,
    )

    inlines = [ProductInline, ]


@register(MediaModel)
class GalleryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'media_type',
        'display_media_file_link',  # Add custom method to display media file link
        'product',
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


@register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'price',
        'category',
        'is_active',
        'created_date',
        'updated_date',
        'thumbnail_image',  # Add thumbnail_image to the list_display
    )
    list_display_links = (
        'id',
        'title',
    )
    list_filter = (
        'title',
        'is_active',
        'created_date',
        'updated_date',
    )
    search_fields = (
        'title',
        'description',
        'category__title',
        'category__description',
    )
    readonly_fields = (
        'price',
    )

    actions = (
        activate_selected_items,
        deactivate_selected_items,
    )

    inlines = [MediaInline, CommentInline]

    def thumbnail_image(self, obj):
        # Define the method to display the thumbnail image
        if obj.Medias.exists():  # Check if there are any related MediaModel objects
            # Assuming you want to display the first media file as thumbnail
            first_media = obj.Medias.first()
            if first_media.media_file:
                return format_html(
                    '<img src="{}" style="max-height: 100px; max-width: 100px;" />',
                    first_media.media_file.url
                )
        return 'No Image'  # Display text if no thumbnail image is available

    thumbnail_image.short_description = 'Thumbnail'  # Set the column header in the admin panel


@register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'user',
        'product',
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


@register(PriceModel)
class PriceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'amount',
        'product',
        'is_active',
        'created_date',
        'updated_date',
    )
    list_display_links = (
        'id',
        'amount',
        'product',
        
    )
    list_filter = (
        'id',
        'amount',
        'product',
        'is_active',
        'created_date',
        'updated_date',
    )
    search_fields = (
        'amount',
        'product',
    )

    actions = (
        activate_selected_items,
        deactivate_selected_items,
    )
