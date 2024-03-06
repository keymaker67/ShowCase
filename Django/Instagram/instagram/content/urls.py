from django.urls import path, include
from rest_framework import routers

from .views import (
    post_view,
    post_detail_view,
    story_detail_view,
    add_post_view,
    add_story_view,
    drf_view,
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
    path('post_detail/<int:pk>', post_detail_view, name="post_detail"),
    path('story_detail/<int:pk>', story_detail_view, name="story_detail"),
    path('drf/', drf_view, name="drf"),
    path('add_post/', add_post_view, name="add_post"),
    path('add_story/', add_story_view, name="add_story"),
    path('', include(content_router.urls, )),
]
