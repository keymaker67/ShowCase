from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter

# Import Models and Serializers
from .models import CommentModel, LikeModel
from .serializers import CommentSerializer, LikeSerializer


# Create Views and ViewSets.
class BaseActionViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, )
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    )
    filterset_fields = ('user', 'post', 'story', 'comment')
    search_fields = ('user', 'post', 'story', 'comment')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentViewSet(BaseActionViewSet):
    serializer_class = CommentSerializer
    queryset = CommentModel.objects.filter(is_active=True).order_by('-pk')


class LikeViewSet(BaseActionViewSet):
    serializer_class = LikeSerializer
    queryset = LikeModel.objects.filter(is_active=True).order_by('-pk')
