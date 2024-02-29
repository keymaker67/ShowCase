from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated


from .models import (
    CategoryModel,
    ProductModel,
    MediaModel,
    CommentModel,
)
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    MediaSerializer,
    CommentSerializer,
)


# Create your views here.
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = CategoryModel.objects.filter(is_active=True).order_by('-pk')
    permission_classes = (IsAuthenticated,)

    filter_backends = (
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    )
    filterset_fields = (
        'title',
        'description',
    )
    search_fields = (
        'title',
        'description',
    )


class MediaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MediaSerializer
    queryset = MediaModel.objects.filter(is_active=True).order_by('-pk')
    permission_classes = (IsAuthenticated,)

    filter_backends = (
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    )
    filterset_fields = (
        'id',
        'title',
        'description',
        'media_type',
        'product',
    )
    search_fields = (
        'title',
        'description',
    )


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.filter(is_active=True).order_by('-pk')
    permission_classes = (IsAuthenticated,)

    filter_backends = (
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    )
    filterset_fields = (
        'id',
        'title',
        'description',
        'category',
    )
    search_fields = (
        'title',
        'description',
        'category',
    )


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = CommentModel.objects.filter(is_active=True).order_by('-pk')
    permission_classes = (IsAuthenticated,)

    filter_backends = (
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    )
    filterset_fields = (
        'id',
        'title',
        'user',
        'product',
        'comment_body',
    )
    search_fields = (
        'title',
        'product',
        'user',
    )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@login_required(login_url='/user/login')
def shop_view(request):
    return render(request, 'home.html')


@login_required(login_url='/user/login')
def shop_test_view(request):
    return render(request, 'shop.html')
