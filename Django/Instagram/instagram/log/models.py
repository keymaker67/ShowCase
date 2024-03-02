from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from rest_framework.exceptions import ValidationError

from user.models import MyBaseModel, UserProfileModel
from content.models import PostModel, StoryModel

User = get_user_model()


# Create previewed model for loging of users
class PreviewModel(MyBaseModel):
    user = models.ForeignKey(User, null=False, blank=False,
                             on_delete=models.PROTECT, verbose_name='User')
    content_type = models.ForeignKey(
        ContentType, on_delete=models.PROTECT, related_name='previews', blank=False, null=False,
        limit_choices_to=(
            models.Q(app_label='content', model='postmodel') |
            models.Q(app_label='content', model='storymodel') |
            models.Q(app_label='user', model='userprofilemodel')
        )
    )
    object_id = models.PositiveSmallIntegerField(verbose_name='Object ID', blank=False, null=False)
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = 'Preview'
        verbose_name_plural = 'Previews'

    def __str__(self):
        return f'{self.user} previewed {self.content_type}'
