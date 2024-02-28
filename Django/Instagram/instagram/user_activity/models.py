from django.db import models
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError

from ..user.models import MyBaseModel
from ..content.models import PostModel

User = get_user_model()


# Create user activity models
class CommentModel(MyBaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='User',
                             related_name='user_comments', blank=False, null=False)
    post = models.ForeignKey(PostModel, on_delete=models.PROTECT, verbose_name='Post',
                             related_name='post_comments', blank=False, null=False)
    comment = models.TextField(verbose_name='Comment', blank=False, null=False)

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
                             related_name='user_likes', blank=False, null=False)
    post = models.ForeignKey(PostModel, on_delete=models.PROTECT, verbose_name='Post',
                             related_name='post_likes', blank=False, null=False)
    comment = models.ForeignKey(CommentModel, on_delete=models.PROTECT, verbose_name='Comment',
                                related_name='comment_likes', blank=False, null=False)

    def clean(self):
        # Ensure that at least one of post or comment is set
        if self.post_id is None and self.comment_id is None:
            raise ValidationError('A like must be associated with either a post or a comment')

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
