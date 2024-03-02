from rest_framework.serializers import ModelSerializer

from .models import PreviewModel
from content.fields import GenericRelatedField


class PreviewSerializer(ModelSerializer):
    content_object = GenericRelatedField()

    class Meta:
        model = PreviewModel
        fields = ('content_object', 'object_id', 'content_type', )
