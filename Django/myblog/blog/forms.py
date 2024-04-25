from django import forms
from .models import ArticleModel


class CreateArticle(forms.ModelForm):
    class Meta:
        model = ArticleModel
        fields = ["title", "slug", "body", "thumb"]
