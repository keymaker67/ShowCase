from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

from .models import UserProfileModel, UserRelationModel, CloseFriendModel

User = get_user_model()


# Create serializer
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'is_active'
        )


class UserProfileSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfileModel
        fields = ('user', 'public', 'profile_picture', 'bio', 'location')


class UserRelationSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserRelationModel
        fields = ('user', 'related_with', 'relation_type')


class CloseFriendSerializer(ModelSerializer):
    close_friend = UserRelationSerializer(read_only=True)
    # close_friend = UserSerializer(read_only=True)

    class Meta:
        model = CloseFriendModel
        fields = ('close_friend', )

