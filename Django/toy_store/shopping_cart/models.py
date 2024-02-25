from django.db import models
from django.contrib.auth import get_user_model

from shop.models import ProductModel
from user.models import MyBaseModel


# Create your models here.
UserModel = get_user_model()


class OrderModel(MyBaseModel):
    title = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Title',
        unique=True,
    )
    user = models.ForeignKey(
        UserModel,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        verbose_name='User',
        related_name='Orders'
    )
    transaction_id = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Transaction ID',
    )

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.title


class OrderItemModel(MyBaseModel):
    product = models.ForeignKey(
        ProductModel,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        verbose_name='Product',
        related_name='OrderItems'
    )
    order = models.ForeignKey(
        OrderModel,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        verbose_name='Order',
        related_name='OrderItems'
    )
    quantity = models.IntegerField(
        default=0,
        null=False,
        blank=False,
        verbose_name='Quantity',
    )

    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'

    def __str__(self):
        return str(self.product)
