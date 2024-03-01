from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter

# Import Models and Serializers
from .models import CommentModel, LikeModel
from .serializers import CommentSerializer, LikeSerializer

# Import MyBaseViewSet
from content.views import MyBaseViewSet


# Create Views and ViewSets.
class CommentViewSet(
    MyBaseViewSet, CommentSerializer, CommentModel
):
    filterset_fields = ('user', 'post', 'story', 'comment')
    search_fields = ('user', 'post', 'story', 'comment')


class LikeViewSet(
    MyBaseViewSet, LikeSerializer, LikeModel
):
    filterset_fields = ('user', 'post', 'story', 'comment')
    search_fields = ('user', 'post', 'story', 'comment')
