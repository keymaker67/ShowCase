from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from .models import (
    MediaModel, MentionModel, PostModel, StoryModel
)
from .serializers import (
    MediaSerializer, MentionSerializer, PostSerializer, StorySerializer
)


# Create content view
# Create ViewSets for serializers
class MediaViewSet(ModelViewSet):
    serializer_class = MediaSerializer
    queryset = MediaModel.objects.filter(is_active=True).order_by('-pk')
    permission_classes = (IsAuthenticated, )

    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
        SearchFilter
    )
    filterset_fields = ('post', 'story', )
    search_fields = ('post', 'story', )


class MentionViewSet(MediaViewSet):
    serializer_class = MentionSerializer
    queryset = MentionModel.objects.filter(is_active=True).order_by('-pk')
    permission_classes = (IsAuthenticated, )

    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
        SearchFilter,
    )
    filterset_fields = ('post', 'story', 'user', )
    search_fields = ('post', 'story', 'user', )


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = PostModel.objects.filter(is_active=True).order_by('-pk')
    permission_classes = (IsAuthenticated, )

    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    )

    filterset_fields = ('user', 'allow_comments', 'show_like', 'close_friends_only', )
    search_fields = ('user', )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class StoryViewSet(ModelViewSet):
    serializer_class = StorySerializer
    queryset = StoryModel.objects.filter(is_active=True).order_by('-pk')
    permission_classes = (IsAuthenticated, )

    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    )

    filterset_fields = ('user', 'allow_comments', 'close_friends_only', )
    search_fields = ('user', )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Create main view
def post_view(request):
    return render(request, 'main/index.html')
