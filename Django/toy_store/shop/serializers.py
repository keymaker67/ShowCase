from rest_framework import serializers

from .models import (
    CategoryModel,
    ProductModel,
    MediaModel,
    CommentModel,
)


class CategorySerializer(serializers.ModelSerializer, ):
    class Meta:
        model = CategoryModel
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer, ):

    class Meta:
        model = ProductModel
        fields = '__all__'


class MediaSerializer(serializers.ModelSerializer, ):
    class Meta:
        model = MediaModel
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer, ):
    class Meta:
        model = CommentModel
        exclude = ('user', )
