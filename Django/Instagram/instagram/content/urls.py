from django.urls import path, include
from rest_framework import routers

from .views import (
    post_view,
    MentionViewSet,
    MediaViewSet,
    PostViewSet,
    StoryViewSet
)

# Create routes
content_router = routers.DefaultRouter()
content_router.register('mention', MentionViewSet, basename='mention')
content_router.register('media', MediaViewSet, basename='media')
content_router.register('post', PostViewSet, basename='post')
content_router.register('story', StoryViewSet, basename='story')

# Create path
urlpatterns = [
    path('', post_view, name="home"),
    path('', include(content_router.urls, )),
]