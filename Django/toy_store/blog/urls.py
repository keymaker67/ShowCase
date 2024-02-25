from rest_framework.routers import DefaultRouter

from .views import (
    CategoryViewSet,
    PostViewSet,
    MediaViewSet,
    CommentViewSet,
)


blog_router = DefaultRouter()

blog_router.register(
    'category_viewset',
    CategoryViewSet,
    basename='category_viewset'
)
blog_router.register(
    'post_viewset',
    PostViewSet,
    basename='post_viewset'
)
blog_router.register(
    'comment_viewset',
    CommentViewSet,
    basename='comment_viewset'
)
blog_router.register(
    'media_viewset',
    MediaViewSet,
    basename='media_viewset'
)

urlpatterns = blog_router.urls
