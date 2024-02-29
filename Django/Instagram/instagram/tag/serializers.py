from rest_framework.serializers import ModelSerializer

from .models import TagModel


# Create model serializer
class TagSerializer(ModelSerializer):
    class Meta:
        model = TagModel
        fields = ('title', 'user', 'post', 'story', )
