from django.urls import path
from . import views


urlpatterns = [
    path('', views.explore_home, name='explore_home'),
    path('turkish_learning/', views.turkish_learning, name='turkish_learning'),
    path('cryptocurrency/', views.cryptocurrency, name='cryptocurrency'),
    path('saat_oyunu/', views.saat_oyunu, name='saat_oyunu')
]
