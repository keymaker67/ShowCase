from rest_framework.serializers import ModelSerializer

from .models import CommentModel, LikeModel


# Create serializer
class CommentSerializer(ModelSerializer):
    class Meta:
        model = CommentModel
        fields = ('user', 'post', 'story', 'comment')


class LikeSerializer(ModelSerializer):
    comment = CommentSerializer(read_only=True)

    class Meta:
        model = LikeModel
        fields = ('user', 'post', 'story', 'comment')
