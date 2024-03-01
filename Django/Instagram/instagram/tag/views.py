from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated

# Import Models and Serializers.
from .models import TagModel
from .serializers import TagSerializer


# Create ViewSets.
class TagViewSet(ModelViewSet):
    serializer_class = TagSerializer
    queryset = TagModel.objects.filter(is_active=True).oreder_by('-pk')
    permission_classes = (IsAuthenticated, )

    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    )

    filterset_fields = ('title', 'post', 'story', )
    search_fields = ('title', 'post', 'story', )
