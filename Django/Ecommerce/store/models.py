from django.db import models
from django.contrib.auth import get_user_model

from core.models import MyBaseModel

the_user = get_user_model()


class CategoryModel(MyBaseModel):
    name = models.CharField(verbose_name="Name", null=False, blank=False, max_length=255)
    slug = models.SlugField(verbose_name="Slug", null=False, blank=False, unique=True, max_length=255)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class ProductModel(MyBaseModel):
    category = models.ForeignKey(CategoryModel, related_name="products", on_delete=models.PROTECT)
    created_by = models.ForeignKey(the_user, related_name="products", on_delete=models.PROTECT)
    title = models.CharField(verbose_name="Title", null=False, blank=False, max_length=255)
    creator = models.CharField(verbose_name="Creator", default="admin", max_length=255)
    description = models.TextField(verbose_name="Description", blank=True)
    image = models.ImageField(upload_to='media/products')
    slug = models.SlugField(verbose_name="Slug", null=False, blank=False, unique=True, max_length=255)
    price = models.DecimalField(verbose_name="Price", max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(verbose_name="In stock", default=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('-created_at', )

    def __str__(self):
        return self.title
