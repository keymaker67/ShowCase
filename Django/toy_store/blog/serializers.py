from rest_framework import serializers

from .models import (
    CategoryModel,
    PostModel,
    MediaModel,
    CommentModel,
)


class CategorySerializer(serializers.ModelSerializer, ):
    class Meta:
        model = CategoryModel
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer, ):
    class Meta:
        model = PostModel
        exclude = ('user', )


class MediaSerializer(serializers.ModelSerializer, ):
    class Meta:
        model = MediaModel
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer, ):
    class Meta:
        model = CommentModel
        exclude = ('user', )
