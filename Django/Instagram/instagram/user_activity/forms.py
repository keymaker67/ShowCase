from django import forms

from .models import CommentModel


# Create forms
class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ('comment', 'user', )
