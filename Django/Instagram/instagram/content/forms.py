from django import forms

from .models import PostModel, StoryModel


# Create Post and Story Forms
class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = (
            'user', 'allow_comments', 'show_like', 'caption',
            'close_friends_only',
        )


class StoryForm(forms.ModelForm):
    class Meta:
        model = StoryModel
        fields = (
            'user', 'allow_comments', 'close_friends_only',
        )
