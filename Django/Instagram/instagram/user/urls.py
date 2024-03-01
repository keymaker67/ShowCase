from django.urls import path, include
from rest_framework.routers import DefaultRouter

# import Views and ViewSets
from .views import (
    signup_view, login_view, logout_view, UserProfileViewSet
)

# Create Default router
user_profile_router = DefaultRouter()
user_profile_router.register('user_profile', UserProfileViewSet, 'user_profile')

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', include(user_profile_router.urls, )),
]
