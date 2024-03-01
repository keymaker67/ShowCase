from django.urls import path, include
from rest_framework import routers

# Import ViewSets
from .views import DirectMessageViewSet

# Add routers
direct_router = routers.DefaultRouter()
direct_router.register('direct', DirectMessageViewSet, 'direct')

urlpatterns = [
    path('', include(direct_router.urls, ))
]