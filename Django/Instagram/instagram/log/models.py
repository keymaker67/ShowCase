from django.db import models
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError

from user.models import MyBaseModel, UserProfileModel
from content.models import PostModel, StoryModel

User = get_user_model()


# Create previewed model for loging of users
class PreviewModel(MyBaseModel):
    user = models.ForeignKey(User, null=False, blank=False,
                             on_delete=models.PROTECT, verbose_name='User')
    profile = models.ForeignKey(
        UserProfileModel, null=True, blank=True,
        verbose_name='Profile', related_name='previews',
        on_delete=models.PROTECT
    )
    story = models.ForeignKey(
        StoryModel, null=True, blank=True,
        verbose_name='Story', related_name='previews',
        on_delete=models.PROTECT
    )
    post = models.ForeignKey(
        PostModel, null=True, blank=True,
        verbose_name='Post', related_name='previews',
        on_delete=models.PROTECT
    )

    def clean(self):
        # At least one option should be provided
        if self.post_id is None and self.story_id is None and self.profile_id is None:
            raise ValidationError('At least one option from post, story, or profile should be provided.')

    class Meta:
        verbose_name = 'Preview'
        verbose_name_plural = 'Previews'

    def __str__(self):
        return f'{self.user} previewed something'
