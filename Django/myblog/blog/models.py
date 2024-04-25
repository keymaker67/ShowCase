from django.db import models
from django.contrib.auth import get_user_model

the_user = get_user_model()


# Create my base models
class MyBaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["created_date"]


# Create other models
class ArticleModel(MyBaseModel):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Article Title')
    slug = models.SlugField(max_length=100, null=True, blank=True, verbose_name='Slug')
    body = models.TextField(null=False, blank=False, verbose_name='Article Body')
    thumb = models.ImageField(null=True, blank=True, verbose_name='Thumbnail', default='default.png')
    author = models.ForeignKey(
        the_user,
        verbose_name='Author',
        related_name='article_models',
        on_delete=models.PROTECT,
        null=False,
        blank=False,
    )

    def snippet(self):
        return self.body[:50]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
