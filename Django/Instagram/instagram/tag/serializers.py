from rest_framework.serializers import ModelSerializer

from .models import TagModel
from content.fields import GenericRelatedField


# Create model serializer
class TagSerializer(ModelSerializer):
    content_object = GenericRelatedField()

    class Meta:
        model = TagModel
        fields = ('title', 'content_object', 'object_id', 'content_type', )
