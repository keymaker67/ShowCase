from rest_framework import serializers
from .fields import GenericRelatedField

from .models import (
    PostModel, StoryModel, MediaModel, MentionModel
)
from user.serializers import UserSerializer
from tag.serializers import TagSerializer
from user_activity.serializers import CommentSerializer, LikeSerializer


# Create serializers
class MentionSerializer(serializers.ModelSerializer):
    content_object = GenericRelatedField()

    class Meta:
        model = MentionModel
        fields = ('user', 'content_object', 'object_id', 'content_type', )


class MediaSerializer(serializers.ModelSerializer):
    content_object = GenericRelatedField()

    class Meta:
        model = MediaModel
        fields = ('media_file', 'media_type', 'content_object', 'object_id', 'content_type')


class PostSerializer(serializers.ModelSerializer):
    media = MediaSerializer(many=True)  # Assuming 'media' is a related field
    mention = MentionSerializer(many=True)  # Assuming 'mention' is a related field
    tag = TagSerializer(many=True)  # Assuming 'tag' is a related field
    like = LikeSerializer(many=True)  # Assuming 'like' is a related field
    Comment = CommentSerializer(many=True)  # Assuming 'Comment' is a related field

    class Meta:
        model = PostModel
        fields = (
            'user', 'allow_comments', 'show_like', 'like', 'comment',
            'close_friends_only', 'media', 'mention', 'tag',
        )


class StorySerializer(serializers.ModelSerializer):
    media = MediaSerializer(many=True)  # Assuming 'media' is a related field
    mention = MentionSerializer(many=True)  # Assuming 'mention' is a related field
    tag = TagSerializer(many=True)  # Assuming 'tag' is a related field
    like = LikeSerializer(many=True)  # Assuming 'like' is a related field
    Comment = CommentSerializer(many=True)  # Assuming 'Comment' is a related field

    class Meta:
        model = StoryModel
        fields = (
            'user', 'allow_comments', 'close_friends_only',
            'media', 'mention', 'tag', 'like', 'comment',
        )
