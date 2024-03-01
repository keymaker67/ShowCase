from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

from .models import UserProfile

User = get_user_model()


# Create serializer
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserProfileSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ('user', 'public', 'profile_picture', 'bio', 'location')

