from django.urls import path

from .views import home_view, product_detail_view, category_detail_view

app_name = "store"

urlpatterns = [
    path('', home_view, name='home'),
    path('item/<slug:slug>', product_detail_view, name='product_detail'),
    path('category/<slug:slug>', category_detail_view, name='category_detail'),
]
