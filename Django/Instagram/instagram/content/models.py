from django.db import models
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

from user.models import MyBaseModel

User = get_user_model()


# Create content models
class PostModel(MyBaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT,
                             blank=False, null=False, related_name='user_posts')
    allow_comments = models.BooleanField(blank=True, default=True,
                                         verbose_name='Allow comments')
    show_like = models.BooleanField(blank=True, default=True,
                                    verbose_name='Show like')
    close_friends_only = models.BooleanField(blank=True, default=False,
                                             verbose_name='Close friends only')
    caption = models.CharField(max_length=500, null=True, blank=True,
                               verbose_name='Caption')
    mention = GenericRelation("MentionModel", related_name='post', )
    media = GenericRelation("MediaModel", related_name='post')
    tag = GenericRelation("tag.TagModel", related_name='post')
    comment = GenericRelation("user_activity.CommentModel", related_name='post')
    like = GenericRelation("user_activity.LikeModel", related_name='post')
    log = GenericRelation("log.PreviewModel", related_name='post')

    @property
    def like_count(self):
        return self.like.count()

    @property
    def comment_count(self):
        return self.comment.count()

    @property
    def tag_count(self):
        return self.tag.count()

    @property
    def mention_count(self):
        return self.mention.count()

    @property
    def media_count(self):
        return self.media.count()

    @property
    def log_count(self):
        return self.log.count()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f'{str(self.user)}'


# Create story model related to users
class StoryModel(MyBaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='User',
                             related_name='user_stories', null=False, blank=False)
    allow_comments = models.BooleanField(blank=True, default=True,
                                         verbose_name='Allow comments')
    close_friends_only = models.BooleanField(blank=True, default=False,
                                             verbose_name='Close friends only')
    mention = GenericRelation("MentionModel", related_name='story')
    media = GenericRelation("MediaModel", related_name='story')
    tag = GenericRelation("tag.TagModel", related_name='story')
    comment = GenericRelation("user_activity.CommentModel", related_name='story')
    like = GenericRelation("user_activity.likeModel", related_name='story')
    log = GenericRelation("log.PreviewModel", related_name='story')

    @property
    def like_count(self):
        return self.like.count()

    @property
    def comment_count(self):
        return self.comment.count()

    @property
    def tag_count(self):
        return self.tag.count()

    @property
    def mention_count(self):
        return self.mention.count()

    @property
    def media_count(self):
        return self.media.count()

    @property
    def log_count(self):
        return self.log.count()

    class Meta:
        verbose_name = 'Story'
        verbose_name_plural = 'stories'

    def __str__(self):
        return f'{self.created_date}'


# Create mention model
class MentionModel(MyBaseModel):
    content_type = models.ForeignKey(
        ContentType, on_delete=models.PROTECT, related_name='mention', blank=False, null=False,
        limit_choices_to=(
                models.Q(app_label='content', model='postmodel') |
                models.Q(app_label='content', model='storymodel')
        ), verbose_name='Content type',
    )
    object_id = models.PositiveSmallIntegerField(verbose_name='Object ID')
    content_object = GenericForeignKey('content_type', 'object_id')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='User',
                             related_name='mentioned_users', null=False, blank=False)

    class Meta:
        verbose_name = 'Mention'
        verbose_name_plural = 'Mentions'
        unique_together = ('content_type', 'object_id', 'user')

    def __str__(self):
        return f'{self.content_type}'


# Create media model related to posts
class MediaModel(MyBaseModel):
    content_type = models.ForeignKey(
        ContentType, on_delete=models.PROTECT, related_name='media', blank=False, null=False,
        limit_choices_to=(
                models.Q(app_label='content', model='postmodel') |
                models.Q(app_label='content', model='storymodel')
        ),
    )
    object_id = models.PositiveSmallIntegerField(verbose_name='Object ID', blank=False, null=False)
    content_object = GenericForeignKey('content_type', 'object_id')
    media_file = models.FileField(upload_to='%Y/%m', blank=False, null=False,
                                  verbose_name='Media File')
    media_type = models.CharField(max_length=10, blank=False, null=False,
                                  choices=[('image', 'Image'), ('video', 'Video')])

    class Meta:
        verbose_name = 'Media'
        verbose_name_plural = 'Medias'
        unique_together = ('content_type', 'object_id', 'media_file')

    def __str__(self):
        return f'{self.media_type} - {self.content_type}'
