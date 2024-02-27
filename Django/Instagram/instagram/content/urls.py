from django.urls import path

from .views import post_view

# Create path
urlpatterns = [
    path('', post_view, name="home")
]