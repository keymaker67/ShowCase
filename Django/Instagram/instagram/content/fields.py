from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers


class GenericRelatedField(serializers.Field):
    def to_representation(self, value):
        # Serialize the related object
        return {
            'id': value.pk,
            'type': ContentType.objects.get_for_model(value).model
        }

    def to_internal_value(self, data):
        # Deserialize the related object
        try:
            # Perform lookup based on data
            content_type = ContentType.objects.get(model=data['type'])
            model_class = content_type.model_class()
            instance = model_class.objects.get(pk=data['id'])
            return instance
        except (KeyError, ObjectDoesNotExist):
            raise serializers.ValidationError("Invalid data for generic foreign key")
