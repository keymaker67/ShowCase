from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

# Import ViewSets
from .views import PreviewViewSet

# Set Default router
log_router = DefaultRouter()
log_router.register('preview', PreviewViewSet, 'preview')

urlpatterns = [
    path('', include(log_router.urls, ))
]