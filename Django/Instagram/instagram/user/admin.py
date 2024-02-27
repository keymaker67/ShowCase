from django.contrib import admin
from django.contrib.admin import register
from django.template.loader import render_to_string
from django.utils.html import format_html



from .models import UserProfile


@admin.action(description='Activate selected items')
def activate_selected_items(self, request, queryset):
    queryset.update(is_active=True)


@admin.action(description='Deactivate selected items')
def deactivate_selected_items(self, request, queryset):
    queryset.update(is_active=False)


@register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'id_user', 'public', 'display_profile_picture', 'location')
    list_filter = ('public', 'location')
    search_fields = ('user', 'id_user', 'location', 'user__username', 'user__first_name', 'user__last_name')
    list_display_links = ('user', 'id_user', )

    # Function to display profile picture
    def display_profile_picture(self, obj):
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

    display_profile_picture.short_description = 'Profile Pic'  # Set the column header in the admin panel

    actions = (
        activate_selected_items,
        deactivate_selected_items,
    )

    # def display_profile_picture(self, obj):
    #     # Define a custom method to render the media file link using a template
    #     if obj.media_file:
    #         return render_to_string('profile_pic_link.html', {'obj': obj})
    #     else:
    #         return '-'  # Display '-' if no media file is available
    #
    # display_profile_picture.allow_tags = True
    # display_profile_picture.short_description = 'Profile Picture'  # Set column header
