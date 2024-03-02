from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter

# Import Models and Serializers
from .forms import UserProfileForm
from .models import (
    UserProfileModel, CloseFriendModel, UserRelationModel
)
from .serializers import (
    UserProfileSerializer, UserRelationSerializer, CloseFriendSerializer
)

# Import MyBaseViewSet
from content.views import MyBaseViewSet

User = get_user_model()


# Create user views
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
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
    return render(request, 'user_profile.html')


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
