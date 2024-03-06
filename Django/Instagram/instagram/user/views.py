from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter

# Import Models and Serializers
from .forms import UserProfileForm, UserEditForm
from .models import (UserProfileModel, CloseFriendModel, UserRelationModel)
from .serializers import (
    UserProfileSerializer,
    UserRelationSerializer,
    CloseFriendSerializer
)

# Import MyBaseViewSet
from content.views import MyBaseViewSet
from content.utils.helpers import (
    get_following_users,
    get_followers,
    trigger_preview,
    get_follow_requests,
    get_public_users,
)
from content.models import PostModel, StoryModel

User = get_user_model()


# Create user views
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            UserProfileModel.objects.create(user=request.user)
            return redirect('home')
        else:
            messages.info(request, 'something went wrong, please try again')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def user_profile_view(request):
    current_user_profile, created = UserProfileModel.objects.get_or_create(user=request.user)
    current_user = request.user

    follow_requests = get_follow_requests(current_user)[0]

    followers = get_followers(current_user)[0]

    followings = get_following_users(current_user)[0]

    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        if current_user_profile:
            profile_form = UserProfileForm(request.POST, request.FILES, instance=current_user_profile)
        else:
            profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        profile_form = UserProfileForm(instance=current_user_profile)
        user_form = current_user
    return render(
        request,
        'user_profile.html',
        {
            'user_form': user_form,
            'profile_form': profile_form,
            'follow_requests_count': len(follow_requests),
            'following_users_count': len(followings),
            'followers_count': len(followers),
            'followings': followings,
            'followers': followers,
            'follow_requests': follow_requests,
        })


@login_required
def user_content_view(request, pk):
    content = list()
    current_user = User.objects.filter(id=pk).first()
    current_user_profile = UserProfileModel.objects.filter(user=current_user).first()
    if current_user_profile:
        trigger_preview(request, current_user_profile)

    public_users, public_user_ids = get_public_users()

    follow_requests, follow_request_ids = get_follow_requests(current_user)
    requested = True if request.user.id in follow_request_ids else False

    followers, follower_user_ids = get_followers(current_user)
    already_follower = True if request.user.id in follower_user_ids else False

    followings, following_user_ids = get_following_users(current_user)

    if request.user.id == pk or request.user.id in follower_user_ids or pk in public_user_ids:
        posts = PostModel.objects.filter(user=current_user).order_by('-created_date')
        for post in posts:
            medias = post.media.all()
            content.append({'post': post, 'medias': medias})

    return render(
        request,
        'user_content.html',
        {
            'follow_requests_count': len(follow_requests),
            'following_users_count': len(followings),
            'followers_count': len(followers),
            'followings': followings,
            'followers': followers,
            'follow_requests': follow_requests,
            'content': content,
            'current_user': current_user,
            'requested': requested,
            'already_follower': already_follower
        })


@login_required
def follow_request_view(request, pk):
    requesting_user = User.objects.filter(id=pk).first()
    UserRelationModel.objects.get_or_create(
        user=requesting_user,
        related_with=request.user,
        relation_type='follower',
        is_active=False
    )
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def handle_follow_request_view(request, pk):
    requesting_user = User.objects.filter(id=pk).first()
    if request.method == 'POST':
        follow_request = UserRelationModel.objects.get(
            user=request.user,
            related_with=requesting_user,
            relation_type='follower'
        )
        action = request.POST.get('action')
        if action == 'accept':
            follow_request.is_active = True
            follow_request.save()
        if action == 'reject':
            follow_request.delete()
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect(request.META.get('HTTP_REFERER'))


# Create ViewSets
class UserProfileViewSet(MyBaseViewSet):
    serializer_class = UserProfileSerializer
    model = UserProfileModel
    filterset_filters = ('user', 'public', 'bio', 'location')
    search_filters = ('user', 'public', 'bio', 'location')


class UserRelationViewSet(MyBaseViewSet):
    serializer_class = UserRelationSerializer
    model = UserRelationModel
    filterset_filters = ('user', 'related_with', 'relation_type')
    search_filters = ('user', 'related_with', 'relation_type')


class CloseFriendViewSet(MyBaseViewSet):
    serializer_class = CloseFriendSerializer
    model = CloseFriendModel
    filterset_filters = ('user_relate', 'close_friend')
    search_filters = ('user_relate', 'close_friend')
