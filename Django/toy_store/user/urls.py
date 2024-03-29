from django.urls import path
from django.contrib.auth import views

from .views import register_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
