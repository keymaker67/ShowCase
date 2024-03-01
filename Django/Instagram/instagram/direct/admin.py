from django.contrib import admin
from django.contrib.admin.decorators import register
from django.template.loader import render_to_string

from .models import DirectMessageModel


# Create admin for direct messages after registering it
@register(DirectMessageModel)
class DirectMessageAdmin(admin.ModelAdmin):
    list_display = (
        'text_message', 'user', 'media_type', 'display_media_link'
    )
    list_display_links = ('sending_user', 'receiving_user', )
    list_filter = ('sending_user', 'receiving_user', 'media_type')
    search_fields = ('text_message', 'sending_user__username', 'receiving_user__username', )
    date_hierarchy = 'created_date'

    def display_media_link(self, obj):
        # Define a custom method to render the media file link using a template
        if obj.media_file:
            return render_to_string('media_file_link.html', {'obj': obj})
        else:
            return '-'

    display_media_link.allow_tags = True
    display_media_link.short_description = 'Media File'
