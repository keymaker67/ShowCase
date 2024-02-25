from rest_framework import routers

from .views import (
    OrderViewSet,
    OrderItemViewSet
)


Shopping_cart_router = routers.DefaultRouter()

Shopping_cart_router.register('order_viewset', OrderViewSet, basename='order_viewset')
Shopping_cart_router.register('order_item_viewset', OrderItemViewSet, basename='order_item_viewset')

urlpatterns = Shopping_cart_router.urls
