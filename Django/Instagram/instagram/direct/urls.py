from django.urls import path, include
from rest_framework import routers

# Import ViewSets
from .views import DirectMessageViewSet, direct_view

# Add routers
direct_router = routers.DefaultRouter()
direct_router.register('direct', DirectMessageViewSet, 'direct')

urlpatterns = [
    path('', include(direct_router.urls, )),
    path('direct_messages', direct_view, name='direct_messages'),
]
