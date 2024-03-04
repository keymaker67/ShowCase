from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter

# Import Models and Serializers
from .models import CommentModel, LikeModel
from .serializers import CommentSerializer, LikeSerializer
from content.models import PostModel, StoryModel
from .utils.helpers import like_view

# Import MyBaseViewSet
from content.views import MyBaseViewSet


# Create Views and ViewSets.
class CommentViewSet(MyBaseViewSet):
    serializer_class = CommentSerializer
    model = CommentModel
    filterset_fields = ('user', 'object_id', 'content_type', )
    search_fields = ('user', 'object_id', 'content_type', )


class LikeViewSet(MyBaseViewSet):
    serializer_class = LikeSerializer
    model = LikeModel
    filterset_fields = ('user', 'object_id', 'content_type', )
    search_fields = ('user', 'object_id', 'content_type', )


def like_story_view(request, pk):
    return like_view(request, pk, StoryModel)


def like_post_view(request, pk):
    return like_view(request, pk, PostModel)


def like_comment_view(request, pk):
    return like_view(request, pk, CommentModel)


