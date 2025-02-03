from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile_update, name='profile'),
    path('logout/', views.custom_logout, name='logout'),

    # Password reset urls
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='password_reset.html'),
         name='password_reset'
         ),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'),
         name='password_reset_done'
         ),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'),
         name='password_reset_confirm'
         ),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='Password_reset_complete.html'),
         name='password_reset_complete'
         ),
]
