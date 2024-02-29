from rest_framework import viewsets, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import PaymentModel
from .serializers import PaymentSerializer
from shopping_cart.models import OrderModel, OrderItemModel
from shop.models import ProductModel


# Create your views here.
class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = PaymentModel.objects.filter(is_active=False).order_by('-pk')
    permission_classes = (IsAuthenticated,)

    filterset_fields = (
        'user',
        'order',
        'payment',
    )
    filter_backends = (
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    )
    search_fields = (
        'user',
        'order',
        'payment',
    )

    def perform_create(self, serializer):
        user = self.request.user
        active_order = OrderModel.objects.filter(is_active=True, user=user).first()

        # Check for active order
        if active_order:
            # Calculate the total amount of products in the active order
            ordered_items = OrderItemModel.objects.filter(order=active_order)
            total_price = list()
            for item in ordered_items:
                quantity = item.quantity
                price = ProductModel.objects.filter(id=item.product_id).first().price
                total_price.append(price.amount * int(quantity))

                # Update Ordered Item Is_active to False
                OrderItemModel.objects.filter(id=item.id).update(is_active=False)

            total_price = sum(total_price)

            # Make new payment
            new_payment = PaymentModel.objects.create(
                user=user,
                order=active_order,
                payment=total_price,
                is_active=False,
            )

            # Update active order is_active to False
            OrderModel.objects.filter(is_active=True, user=user).update(is_active=False)

            serializer = self.get_serializer(new_payment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
