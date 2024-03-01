from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

# Import Models and Serializers
from .models import PreviewModel
from .serializers import PreviewSerializer


# Create viewSets
class PreviewViewSet(ModelViewSet):
    serializer_class = PreviewSerializer
    queryset = PreviewModel.objects.filter(is_active=True).order_by('-pk')
    permission_classes = (IsAuthenticated, )

    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    )

    filterset_filters = ('user', 'profile', 'story', 'post')
    search_filters = ('user', 'profile', 'story', 'post')

    def creat_perform(self, serializer):
        serializer.save(user=self.request.user)
