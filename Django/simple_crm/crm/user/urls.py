from django.urls import path

from .views import login_user_view, logout_user_view, register_user_view

urlpatterns = [
    path('login/', login_user_view, name='login', ),
    path('logout/', logout_user_view, name='logout', ),
    path('register/', register_user_view, name='register', ),
]