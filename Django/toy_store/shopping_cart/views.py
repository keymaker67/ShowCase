from datetime import datetime

from django.shortcuts import render
from rest_framework import viewsets, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import OrderModel, OrderItemModel
from .serializers import OrderItemSerializer, OrderSerializer
from shop.models import ProductModel


# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = OrderModel.objects.filter(is_active=True).order_by('-pk')

    filterset_fields = (
        'title',
        'user',
        'transaction_id',
    )
    filter_backends = (
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    )
    search_fields = (
        'title',
        'user',
        'transaction_id',
    )

    def perform_create(self, request):
        # Create a new order for the user
        user = self.request.user
        new_order = OrderModel.objects.create(
            user=user,
            is_active=True,
            title=request.data['title'],
            transaction_id=request.data['transaction_id'],
        )

        serializer = self.get_serializer(new_order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrderItemViewSet(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer
    queryset = OrderItemModel.objects.filter(is_active=True).order_by('-pk')
    permission_classes = (IsAuthenticated,)

    filterset_fields = (
        'product',
        'order',
        'quantity'
    )
    filter_backends = (
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    )
    search_fields = (
        'product',
        'order',
        'quantity'
    )

    def perform_create(self, request):
        # Get the product
        product = ProductModel.objects.filter(id=request.data['product']).first()

        # Check if there is an active order for the user
        user = self.request.user
        if user:
            active_order = OrderModel.objects.filter(user=user, is_active=True).first()

            if not active_order:
                # Create a new active order for the user
                active_order = OrderModel.objects.create(
                    user=user,
                    is_active=True,
                    title=f'{user} order at {datetime.now()}',
                )

            # Create and Order Item for the product and add it to the active order
            order_item = OrderItemModel.objects.create(
                product=product,
                quantity=request.data['quantity'],
                order=active_order,
                is_active=True,
            )

            serializer = self.get_serializer(order_item)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


def shopping_cart_view(request):
    return render(request, 'shopping_cart.html')
