from rest_framework.serializers import ModelSerializer

from .models import PreviewModel


class PreviewSerializer(ModelSerializer):
    class Meta:
        model = PreviewModel
        fields = ('user', 'profile', 'story', 'post', )
