from rest_framework.serializers import ModelSerializer

from .models import (
    PostModel, StoryModel, MediaModel, MentionModel
)
from user.serializers import UserSerializer


# Create serializers
class MediaSerializer(ModelSerializer):
    class Meta:
        model = MediaModel
        fields = ('post', 'story', 'media_file', 'media_type', )


class MentionSerializer(ModelSerializer):
    class Meta:
        model = MentionModel
        fields = ('post', 'story', 'user', )


class PostSerializer(ModelSerializer):
    media = MediaSerializer(read_only=True)
    mention = MentionSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = PostModel
        fields = (
            'user', 'allow_comments', 'show_like',
            'close_friends_only', 'caption', 'media',
            'mention'
        )


class StorySerializer(ModelSerializer):
    media = MediaSerializer(read_only=True)
    mention = MentionSerializer(read_only=True)

    class Meta:
        model = StoryModel
        fields = (
            'user', 'allow_comments', 'close_friends_only',
            'media', 'mention'
        )
