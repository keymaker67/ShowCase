from django.urls import path

from .views import (
    home_view,
    customer_detail_view,
    customer_delete_view,
    customer_add_view,
    customer_update_view,
)

urlpatterns = [
    path('', home_view, name='home'),
    path('customer_detail/<int:pk>', customer_detail_view, name='customer_detail'),
    path('customer_delete/<int:pk>', customer_delete_view, name='customer_delete'),
    path('customer_add/', customer_add_view, name='customer_add'),
    path('customer_update/<int:pk>', customer_update_view, name='customer_update'),
]
