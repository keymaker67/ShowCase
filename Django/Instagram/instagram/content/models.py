from django.db import models
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError

from user.models import MyBaseModel

User = get_user_model()


# Create content models
class PostModel(MyBaseModel):
    user = models.OneToOneField(User, on_delete=models.PROTECT,
                                blank=False, null=False, related_name='user_posts')
    allow_comments = models.BooleanField(blank=True, default=True,
                                         verbose_name='Allow comments')
    show_like = models.BooleanField(blank=True, default=True,
                                    verbose_name='Show like')
    close_friends_only = models.BooleanField(blank=True, default=True,
                                             verbose_name='Close friends only')
    caption = models.CharField(max_length=500, null=True, blank=True,
                               verbose_name='Caption')

    @property
    def like_counts(self):
        return self.post_likes.count()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f'{str(self.user)} Created a post at {self.created_date}'


# Create story model related to users
class StoryModel(MyBaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='User',
                             related_name='user_stories', null=False, blank=False)
    allow_comments = models.BooleanField(blank=True, default=True,
                                         verbose_name='Allow comments')
    close_friends_only = models.BooleanField(blank=True, default=True,
                                             verbose_name='Close friends only')

    class Meta:
        verbose_name = 'Story'
        verbose_name_plural = 'stories'

    def __str__(self):
        return f'{self.user}'


# Create mention model
class MentionModel(MyBaseModel):
    post = models.ForeignKey(PostModel, on_delete=models.PROTECT, verbose_name='Post',
                             related_name='mentions', null=True, blank=True)
    story = models.ForeignKey(StoryModel, on_delete=models.PROTECT, verbose_name='Story',
                              related_name='mentions', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='User',
                             related_name='mentioned_users', null=False, blank=False)

    class Meta:
        verbose_name = 'Mention'
        verbose_name_plural = 'Mentions'

    def __str__(self):
        return f'{self.post} + {self.user}'

    def clean(self):
        # Ensure that mentions is associated with either a post or a story
        if self.post_id is None and self.story_id is None:
            raise ValidationError('A story or post should be provided for mentioning a user!')


# Create media model related to posts
class MediaModel(MyBaseModel):
    post = models.ForeignKey(PostModel, on_delete=models.PROTECT, verbose_name='Post',
                             related_name='medias', null=True, blank=True)
    story = models.ForeignKey(StoryModel, on_delete=models.PROTECT, verbose_name='Story',
                              related_name='medias', null=True, blank=True)
    media_file = models.FileField(upload_to='%Y/%m', blank=False, null=False,
                                  verbose_name='Media File')
    media_type = models.CharField(max_length=10, blank=False, null=False,
                                  choices=[('image', 'Image'), ('video', 'Video')])

    class Meta:
        verbose_name = 'Media'
        verbose_name_plural = 'Medias'

    def __str__(self):
        return f'{self.media_type}'

    def clean(self):
        # Ensure that mentions is associated with either a post or a story
        if self.post_id is None and self.story_id is None:
            raise ValidationError('A story or post should be provided for mentioning a user!')
