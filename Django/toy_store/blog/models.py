from django.db import models
from django.contrib.auth import get_user_model

from user.models import MyBaseModel


UserModel = get_user_model()


# Create your models here.
class CategoryModel(MyBaseModel):
    title = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Title',
        unique=True,
    )
    description = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Description',
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class PostModel(MyBaseModel):
    title = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Title',
        unique=True,
    )
    the_post = models.TextField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='The post',
    )
    category = models.ForeignKey(
        CategoryModel,
        verbose_name='Category',
        related_name='posts',
        on_delete=models.PROTECT
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.PROTECT,
        verbose_name='User',
        related_name='posts'
    )

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title


class MediaModel(MyBaseModel):
    MEDIA_CHOICES = (
        ('image', 'Image'),
        ('video', 'Video'),
        ('audio', 'Audio'),
    )
    title = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Title',
        unique=True,
    )
    description = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Description',
    )
    media_type = models.CharField(
        max_length=10,
        choices=MEDIA_CHOICES,
        null=False,
        blank=False,
        verbose_name='Media Type'
    )
    media_file = models.FileField(
        upload_to='%Y/%m/%d',
        null=False,
        blank=False,
        verbose_name='Media File',
    )
    post = models.ForeignKey(
        PostModel,
        on_delete=models.PROTECT,
        verbose_name='Post',
        related_name='Medias'
    )

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'

    def __str__(self):
        return self.title


class CommentModel(MyBaseModel):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.PROTECT,
        verbose_name='User',
        related_name='post_comments'
    )
    post = models.ForeignKey(
        PostModel,
        on_delete=models.PROTECT,
        verbose_name='Post',
        related_name='comments'
    )
    title = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Title',
    )
    comment_body = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='The Comment',
    )

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.title
