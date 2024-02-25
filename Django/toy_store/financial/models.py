from django.db import models
from django.contrib.auth import get_user_model

from shopping_cart.models import OrderModel
from user.models import MyBaseModel


# Create your models here.
UserModel = get_user_model()


class PaymentModel(MyBaseModel):
    user = models.ForeignKey(
        UserModel,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        verbose_name='User',
        related_name='Payments'
    )
    order = models.ForeignKey(
        OrderModel,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        verbose_name='Order',
        related_name='Payments'
    )
    payment = models.FloatField(
        null=False,
        blank=False,
        verbose_name='Payment',
    )

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

    def __str__(self):
        return str(f"{self.user} | {self.payment} |")
    
