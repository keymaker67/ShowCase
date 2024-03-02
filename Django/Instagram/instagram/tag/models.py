from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from rest_framework.exceptions import ValidationError

from user.models import MyBaseModel
from content.models import PostModel, StoryModel

User = get_user_model()


# Create tag model
class TagModel(MyBaseModel):
    title = models.CharField(max_length=100,
                             null=False, blank=False, verbose_name='Title')
    content_type = models.ForeignKey(
        ContentType, on_delete=models.PROTECT, related_name='tag', blank=False, null=False,
        limit_choices_to={'content': ['post', 'story']},
    )
    object_id = models.PositiveSmallIntegerField(verbose_name='Object ID', blank=False, null=False)
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        unique_together = ('content_type', 'object_id', 'title')

    def __str__(self):
        return f'{self.title}'
