from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

# Import models and serializers
from .models import DirectMessageModel
from .serializers import DirectMessageSerializer

# Import MyBaseViewSet
from content.views import MyBaseViewSet
from content.utils.helpers import (
    get_followers,
    get_following_users,
    get_public_users,
)

User = get_user_model()


# Create ViewSets
class DirectMessageViewSet(MyBaseViewSet):
    serializer_class = DirectMessageSerializer
    model = DirectMessageModel
    filterset_fields = ('text_message', 'sender', 'receiver', )
    search_fields = ('text_message', 'sender', 'receiver', )

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


# Create template related views
@login_required
def direct_view(request):
    user_list = list()
    current_user = request.user

    followers = get_followers(current_user)[1]
    followers = User.objects.filter(id__in=followers).values_list('username', flat=True)
    user_list.extend(followers)

    following_users = get_following_users(current_user)[1]
    following_users = User.objects.filter(id__in=following_users).values_list('username', flat=True)
    user_list.extend(following_users)

    public_users = get_public_users()[1]
    public_users = User.objects.filter(id__in=public_users).values_list('username', flat=True)
    user_list.extend(public_users)
    user_list = set(user_list)

    return render(request, 'direct.html', {'user_list': user_list})
