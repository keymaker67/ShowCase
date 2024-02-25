from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import (
    CategoryModel,
    PostModel,
    MediaModel,
    CommentModel,
)
from .serializers import (
    CategorySerializer,
    PostSerializer,
    MediaSerializer,
    CommentSerializer,
)


# Create your views here.
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [
        SessionAuthentication,
        BasicAuthentication,
        JWTAuthentication
    ]
    serializer_class = CategorySerializer
    queryset = CategoryModel.objects.filter(is_active=True).order_by('-pk')

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
        'user',
    )


class MediaViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [
        SessionAuthentication,
        BasicAuthentication,
        JWTAuthentication
    ]
    serializer_class = MediaSerializer
    queryset = MediaModel.objects.filter(is_active=True).order_by('-pk')

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
        'post',
    )
    search_fields = (
        'title',
        'description',
    )


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [
        SessionAuthentication,
        BasicAuthentication,
        JWTAuthentication
    ]
    serializer_class = PostSerializer
    queryset = PostModel.objects.filter(is_active=True).order_by('-pk')

    filter_backends = (
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    )
    filterset_fields = (
        'id',
        'title',
        'category',
    )
    search_fields = (
        'title',
        'category',
    )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [
        SessionAuthentication,
        BasicAuthentication,
        JWTAuthentication
    ]
    serializer_class = CommentSerializer
    queryset = CommentModel.objects.filter(is_active=True).order_by('-pk')

    filter_backends = (
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    )
    filterset_fields = (
        'id',
        'title',
        'user',
        'post',
        'comment_body',
    )
    search_fields = (
        'title',
        'post',
        'user',
    )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


def blog_view(request):
    return render(request, 'blog.html')
