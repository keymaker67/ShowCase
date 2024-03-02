from rest_framework.serializers import ModelSerializer

from .models import DirectMessageModel


# Create serializer
class DirectMessageSerializer(ModelSerializer):
    class Meta:
        model = DirectMessageModel
        fields = (
            'text_message', 'sender', 'receiver', 'media_file', 'media_type',
        )
