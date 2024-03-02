from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated

# Import Models and Serializers.
from .models import TagModel
from .serializers import TagSerializer

# Import MyBaseViewSet
from content.views import MyBaseViewSet


# Create ViewSets.
class TagViewSet(MyBaseViewSet):
    serializer_class = TagSerializer
    model = TagModel
    filterset_fields = ('title', 'object_id', 'content_type', )
    search_fields = ('title', 'object_id', 'content_type', )
