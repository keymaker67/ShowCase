from django.urls import path, include
from rest_framework import routers

from .views import (
    shop_view,
    shop_test_view,
    CategoryViewSet,
    ProductViewSet,
    CommentViewSet,
    MediaViewSet,
)


Shop_router = routers.DefaultRouter()

Shop_router.register('category_viewset', CategoryViewSet, basename='category_viewset')
Shop_router.register('product_viewset', ProductViewSet, basename='product_viewset')
Shop_router.register('comment_viewset', CommentViewSet, basename='comment_viewset')
Shop_router.register('media_viewset', MediaViewSet, basename='media_viewset')

urlpatterns = [
    path('', shop_view, name='home'),
    path('test', shop_test_view, name='shop_test'),
    path('', include(Shop_router.urls, )),
]
