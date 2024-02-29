from django.db import models
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError

from content.models import PostModel, StoryModel
from user.models import MyBaseModel

User = get_user_model()


# Create user activity models
class CommentModel(MyBaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='User',
                             related_name='comments', blank=False, null=False)
    post = models.ForeignKey(PostModel, on_delete=models.PROTECT, verbose_name='Post',
                             related_name='comments', blank=True, null=True)
    story = models.ForeignKey(StoryModel, on_delete=models.PROTECT, verbose_name='Story',
                              related_name='comments', blank=True, null=True)
    comment = models.TextField(verbose_name='Comment', blank=False, null=False)

    def clean(self):
        # Ensure that at least one of post or comment is set
        if self.post_id is None and self.story_id is None:
            raise ValidationError('A comment must be associated with either a post or a story')

    @property
    def like_count(self):
        return self.comment_likes.count()

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.comment


class LikeModel(MyBaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='User',
                             related_name='likes', blank=False, null=False)
    post = models.ForeignKey(PostModel, on_delete=models.PROTECT, verbose_name='Post',
                             related_name='likes', blank=True, null=True)
    story = models.ForeignKey(StoryModel, on_delete=models.PROTECT, verbose_name='Story',
                              related_name='likes', blank=True, null=True)
    comment = models.ForeignKey(CommentModel, on_delete=models.PROTECT, verbose_name='Comment',
                                related_name='likes', blank=True, null=True)

    def clean(self):
        # Ensure that at least one of post or comment is set
        if self.post_id is None and self.comment_id is None and self.story_id is None:
            raise ValidationError('A like must be associated with a post, a comment, or a story')

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'

    def __str__(self):
        return f'{self.post} + {self.user}'
