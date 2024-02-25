from rest_framework import routers

from .views import PaymentViewSet


financial_router = routers.DefaultRouter()
financial_router.register('payment_viewset', PaymentViewSet, basename='payment_viewset')

urlpatterns = financial_router.urls