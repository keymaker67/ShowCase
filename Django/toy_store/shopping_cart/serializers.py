from rest_framework import serializers

from .models import OrderModel, OrderItemModel


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        exclude = ('user', 'is_active', )


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItemModel
        exclude = ('is_active', 'order', )
