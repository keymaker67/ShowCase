from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

# Import ViewSets
from .views import TagViewSet

# Create Default router
tag_router = DefaultRouter()
tag_router.register('tag', TagViewSet, 'tag')

urlpatterns = [
    path('', include(tag_router.urls, ))
]