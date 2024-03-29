from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib import messages
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated

# Import Models and ViewSets and Forms
from .models import (
    MediaModel, MentionModel, PostModel, StoryModel
)
from .serializers import (
    MediaSerializer, MentionSerializer, PostSerializer, StorySerializer
)
from .forms import PostForm, StoryForm
from tag.models import TagModel
from .utils.helpers import (
    get_followers,
    post_story_form_validator,
    get_following_users,
    get_public_users,
    add_posts_stories,
    content_view,
    trigger_preview,
)
from user_activity.forms import CommentForm
from user_activity.models import CommentModel

User = get_user_model()


# Create content view
# Create a base ViewSet
class MyBaseViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, )

    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
        SearchFilter
    )

    def get_serializer_class(self):
        return self.serializer_class

    def get_queryset(self):
        return self.model.objects.filter(is_active=True).order_by('-pk')


class MediaViewSet(MyBaseViewSet):
    serializer_class = MediaSerializer
    model = MediaModel
    filterset_fields = ('media_type', 'object_id', 'content_type', )
    search_fields = ('media_type', 'object_id', 'content_type')


# Create ViewSets for serializers
class MentionViewSet(MyBaseViewSet):
    serializer_class = MentionSerializer
    model = MentionModel
    filterset_fields = ('user', 'object_id', 'content_type', )
    search_fields = ('content_type', 'object_id', 'content_object', 'user', )


class PostViewSet(MyBaseViewSet):
    serializer_class = PostSerializer
    model = PostModel
    filterset_fields = ('user', 'allow_comments', 'show_like', 'close_friends_only', )
    search_fields = ('user', )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class StoryViewSet(MyBaseViewSet):
    serializer_class = StorySerializer
    model = StoryModel
    filterset_fields = ('user', 'allow_comments', 'close_friends_only', )
    search_fields = ('user', )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


def post_detail_view(request, pk):
    template = 'main/post_detail.html'
    return content_view(request, pk, PostModel, template)


def story_detail_view(request, pk):
    template = 'main/story_detail.html'
    return content_view(request, pk, StoryModel, template)


# Create main view
def post_view(request):
    posts = list()
    stories = list()

    if request.user.is_authenticated:
        current_user = request.user
        following_users = get_following_users(current_user)[0]

        if following_users:
            add_posts_stories(following_users, posts, stories)

    public_users = get_public_users()[0]
    if public_users:
        add_posts_stories(public_users, posts, stories)

    return render(request, 'main/index.html', {'posts': posts, 'stories': stories})


@login_required()
def drf_view(request):
    return render(request, 'main/drf.html')


@login_required()
def add_post_view(request):
    # Create an instance of current user
    current_user = request.user

    # Create a list of followers
    followers = get_followers(current_user)[0]

    # Check for post method
    if request.method == 'POST':
        form = PostForm(request.POST)
        post_story_form_validator(request, form)
    else:
        # Populate required field
        initial_data = {'user': request.user.id}
        # Pass initial data to the form
        form = PostForm(initial=initial_data)

    return render(request, 'main/add_post.html', {'form': form, 'followers': followers})


@login_required()
def add_story_view(request):
    # Create an instance of current user
    current_user = request.user

    # Create a list of followers
    followers = get_followers(current_user)

    # Check for post method
    if request.method == 'POST':
        form = StoryForm(request.POST)
        post_story_form_validator(request, form)
    else:
        # Populate required field
        initial_data = {'user': request.user.id}
        # Pass initial data to the form
        form = PostForm(initial=initial_data)

    return render(request, 'main/add_story.html', {'form': form, 'followers': followers})
