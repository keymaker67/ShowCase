from django.db import models
from django.contrib.auth import get_user_model

from ..user.models import MyBaseModel

User = get_user_model()


# Create content models
class PostModel(MyBaseModel):
    user = models.OneToOneField(User, on_delete=models.PROTECT, blank=False, null=False, related_name='user_posts')
    allow_comments = models.BooleanField(blank=True, default=True, verbose_name='Allow comments')
    show_like = models.BooleanField(blank=True, default=True, verbose_name='Show like')
    close_friends_only = models.BooleanField(blank=True, default=True, verbose_name='Close friends only')
    mentioned_user = models.ManyToManyField(User, related_name='mentioned_users_post', blank=True,
                                            verbose_name='Mentioned User')
    caption = models.CharField(max_length=255, blank=True, verbose_name='Caption')

    @property
    def like_counts(self):
        return self.post_likes.count()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f'{str(self.user)} Created a post at {self.created_date}'
