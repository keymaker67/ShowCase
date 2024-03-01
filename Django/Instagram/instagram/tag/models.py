from django.db import models
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model

from user.models import MyBaseModel
from content.models import PostModel, StoryModel

User = get_user_model()


# Create tag model
class TagModel(MyBaseModel):
    title = models.CharField(max_length=100,
                             null=False, blank=False, verbose_name='Title')
    post = models.ForeignKey(
        PostModel, null=True, blank=True,
        verbose_name='Post', related_name='tags',
        on_delete=models.PROTECT
    )
    story = models.ForeignKey(
        StoryModel, null=True, blank=True,
        verbose_name='Story', related_name='tags',
        on_delete=models.PROTECT
    )

    # Define necessıty of post or story
    def clean(self):
        # Ensure that mentions is associated with either a post or a story
        if self.post_id is None and self.story_id is None:
            raise ValidationError('A story or post should be provided for creating a tag!')

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return f'{self.title}'
