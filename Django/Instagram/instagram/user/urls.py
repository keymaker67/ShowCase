from django.urls import path, include
from rest_framework.routers import DefaultRouter

# import Views and ViewSets
from .views import (
    signup_view,
    login_view,
    logout_view,
    follow_request_view,
    handle_follow_request_view,
    user_profile_view,
    UserProfileViewSet,
    UserRelationViewSet,
    CloseFriendViewSet,
    user_content_view,
)

# Create Default router
user_profile_router = DefaultRouter()
user_profile_router.register('user_profile', UserProfileViewSet, 'user_profile')
user_profile_router.register('user_relate', UserRelationViewSet, 'user_relate')
user_profile_router.register('close_friend', CloseFriendViewSet, 'close_friend')

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', user_profile_view, name='profile'),
    path('user_content/<int:pk>', user_content_view, name='user_content'),
    path('follow_request/<int:pk>', follow_request_view, name='follow_request'),
    path('handle_follow_request/<int:pk>', handle_follow_request_view, name='handle_follow_request'),
    path('', include(user_profile_router.urls, )),
]
