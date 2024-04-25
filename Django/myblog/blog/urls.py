from django.urls import path

from .views import about, home, article, create_article

app_name = 'blog'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('about/<slug>', article, name='article'),
    path('create_article/', create_article, name='create_article'),
]
