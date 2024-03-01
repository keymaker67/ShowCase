from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated

# Import Models and ViewSets
from .models import (
    MediaModel, MentionModel, PostModel, StoryModel
)
from .serializers import (
    MediaSerializer, MentionSerializer, PostSerializer, StorySerializer
)


# Create content view
# Create a base ViewSet
class MyBaseViewSet(ModelViewSet, serializer, model):
    serializer_class = serilizer
    queryset = model.objects.filter(is_active=True).order_by('-pk')
    permission_classes = (IsAuthenticated, )

    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
        SearchFilter
    )


# Create ViewSets for serializers
class MediaViewSet(MyBaseViewSet, MentionSerializer, MediaModel):
    filterset_fields = ('post', 'story', )
    search_fields = ('post', 'story', )


class MentionViewSet(MyBaseViewSet, MentionSerializer, MentionModel):
    filterset_fields = ('post', 'story', 'user', )
    search_fields = ('post', 'story', 'user', )


class PostViewSet(ModelViewSet, PostSerializer, PostModel):
    filterset_fields = ('user', 'allow_comments', 'show_like', 'close_friends_only', )
    search_fields = ('user', )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class StoryViewSet(ModelViewSet, StorySerializer, StoryModel):
    filterset_fields = ('user', 'allow_comments', 'close_friends_only', )
    search_fields = ('user', )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Create main view
def post_view(request):
    return render(request, 'main/index.html')
