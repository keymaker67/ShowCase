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


class ProductModel(MyBaseModel):
    title = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Title',
        unique=True,
    )
    description = models.TextField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Description',
    )
    category = models.ForeignKey(
        CategoryModel,
        verbose_name='Category',
        related_name='products',
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title

    @property
    def price(self):
        return self.prices.filter(is_active=True).last()


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
    product = models.ForeignKey(
        ProductModel,
        on_delete=models.PROTECT,
        verbose_name='product',
        related_name='Medias'
    )

    class Meta:
        verbose_name = 'Media'
        verbose_name_plural = 'Medias'

    def __str__(self):
        return self.title


class PriceModel(MyBaseModel):
    amount = models.FloatField(
        null=True,
        blank=True,
        verbose_name='Amount',        
    )
    product = models.ForeignKey(
        ProductModel,
        null=False,
        blank=False,
        verbose_name='product',
        related_name='prices',
        on_delete=models.PROTECT
    )        

    class Meta:
        verbose_name = 'Price'
        verbose_name_plural = 'Prices'

    def __str__(self):
        return str(self.amount)


class CommentModel(MyBaseModel):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.PROTECT,
        verbose_name='User',
        related_name='product_comments'
    )
    product = models.ForeignKey(
        ProductModel,
        on_delete=models.PROTECT,
        verbose_name='Product',
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
