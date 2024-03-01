from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

# Import models and serializers
from .models import DirectMessageModel
from .serializers import DirectMessageSerializer

# Import MyBaseViewSet
from content.views import MyBaseViewSet


# Create ViewSets
class DirectMessageViewSet(MyBaseViewSet):
    serializer_class = DirectMessageSerializer
    model = DirectMessageModel
    filterset_fields = ('text_message', 'sending_user', 'receiving_user', )
    search_fields = ('text_message', 'sending_user', 'receiving_user', )

    def perform_create(self, serializer):
        serializer.save(sending_user=self.request.user)
