from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Import Views and ViewSets
from .views import CommentViewSet, LikeViewSet

# Create Default router
user_activity_router = DefaultRouter()
user_activity_router.register('like', CommentViewSet, 'like')
user_activity_router.register('like', LikeViewSet, 'like')

urlpatterns = [
    path('', include(user_activity_router.urls, ))
]