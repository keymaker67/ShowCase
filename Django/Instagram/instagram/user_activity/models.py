from django.db import models
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

from content.models import PostModel, StoryModel
from user.models import MyBaseModel

User = get_user_model()


# Create user activity models
class CommentModel(MyBaseModel):
    comment = models.CharField(max_length=255, null=False, blank=False, verbose_name='Comment')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='User',
                             related_name='comments', blank=False, null=False)
    content_type = models.ForeignKey(
        ContentType, on_delete=models.PROTECT, related_name='comment', blank=False, null=False,
        limit_choices_to=(
            models.Q(app_label='content', model='postmodel') |
            models.Q(app_label='content', model='storymodel')
        ), verbose_name='Content type',
    )
    object_id = models.PositiveSmallIntegerField(verbose_name='Object ID')
    content_object = GenericForeignKey('content_type', 'object_id')
    like = GenericRelation("LikeModel", related_name='comment')

    def get_like_count(self):
        return self.like.count()

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.comment


class LikeModel(MyBaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='User',
                             related_name='likes', blank=False, null=False)
    content_type = models.ForeignKey(
        ContentType, on_delete=models.PROTECT, related_name='like', blank=False, null=False,
        limit_choices_to=(
            models.Q(app_label='content', model='postmodel') |
            models.Q(app_label='content', model='storymodel') |
            models.Q(app_label='user_activity', model='commentmodel')
        ), verbose_name='Content type',
    )
    object_id = models.PositiveSmallIntegerField(verbose_name='Object ID')
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
        unique_together = ('content_type', 'object_id', 'user')

    def __str__(self):
        return f'{self.post} + {self.user}'
