from rest_framework.serializers import ModelSerializer

from .models import CommentModel, LikeModel
from content.fields import GenericRelatedField


# Create serializer
class LikeSerializer(ModelSerializer):
    content_object = GenericRelatedField()

    class Meta:
        model = LikeModel
        fields = ('user', 'content_object', 'object_id', 'content_type', )


class CommentSerializer(ModelSerializer):
    content_object = GenericRelatedField()
    comment = LikeSerializer(many=True)  # Assuming 'media' is a related field

    class Meta:
        model = CommentModel
        fields = ('user', 'content_object', 'object_id', 'content_type', 'comment')
