from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
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

    followers = get_followers(current_user)[0]
    followers = list(followers.values_list(flat=True))
    user_list.extend(followers)

    following_users = get_following_users(current_user)[0]
    following_users = list(following_users.values_list(flat=True))
    user_list.extend(following_users)
    print(user_list)

    following_users = list(item for item in following_users)

    public_users = get_public_users()[0]
    public_users = list(public_users.values_list('user_id', flat=True))
    print(public_users)

    return render(request, 'direct.html', {'user_list': user_list})
