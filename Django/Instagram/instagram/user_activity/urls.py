from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Import Views and ViewSets
from .views import (
    CommentViewSet,
    LikeViewSet,
    like_story_view,
    like_post_view,
    like_comment_view,
)

# Create Default router
user_activity_router = DefaultRouter()
user_activity_router.register('comment', CommentViewSet, 'comment')
user_activity_router.register('like', LikeViewSet, 'like')

urlpatterns = [
    path('', include(user_activity_router.urls, )),
    path('like_story/<int:pk>', like_story_view, name='like_story'),
    path('like_post/<int:pk>', like_post_view, name='like_post'),
    path('like_comment/<int:pk>', like_comment_view, name='like_comment'),
]