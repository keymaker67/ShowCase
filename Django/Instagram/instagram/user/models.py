from django.db import models
from django.db.models import Case, Q, When
from django.db.models.functions import Concat
from django.contrib.contenttypes.fields import GenericRelation

from django.contrib.auth import get_user_model

# Get user
User = get_user_model()


# Create Custom Base Model
class MyBaseModel(models.Model):
    is_active = models.BooleanField(default=True, verbose_name='Is Active')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Updated At')

    class Meta:
        abstract = True
        ordering = ('pk',)

    def __str__(self):
        raise NotImplementedError('Implement __str__ method')


# Create profile for users
class UserProfileModel(MyBaseModel):
    user = models.OneToOneField(
        User, on_delete=models.PROTECT, verbose_name='User',
        related_name='profiles')  # Make relation to login user
    public = models.BooleanField(null=False, blank=False, default=False, verbose_name='Public')
    profile_picture = models.ImageField(upload_to='%Y/%m', null=True, blank=True, verbose_name='Profile picture')
    bio = models.TextField(max_length=500, null=True, blank=True, verbose_name='Bio')
    location = models.CharField(max_length=100, null=True, blank=True, verbose_name='Location')
    log = GenericRelation("log.PreviewModel", related_name='profile')

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'Users Profile'

    def __str__(self):
        return str(self.user)


class UserRelationModel(MyBaseModel):
    RELATION_CHOICES = [('follower', 'Follower'), ('following', 'Following'), ('blocked', 'Blocked'), ]
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name='User',
        related_name='user_relations')  # Make relation to login user
    related_with = models.ForeignKey(
        User, on_delete=models.PROTECT, null=False, blank=False,
        verbose_name='Relate with', related_name='related_relations', )
    relation_type = models.CharField(
        max_length=15, choices=RELATION_CHOICES, null=False, blank=False,
        verbose_name='Relation type', )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Define cases for different relation types
        match self.relation_type :
            # If the relation type is 'follower', add a 'following' relation for the related user
            case 'follower':
                UserRelationModel.objects.get_or_create(
                    user=self.related_with,
                    related_with=self.user,
                    relation_type='following'
                )
            # If the relation type is 'following', add a 'follower' relation for the related user
            case 'following':
                UserRelationModel.objects.get_or_create(
                    user=self.related_with,
                    related_with=self.user,
                    relation_type='follower'
                )

    class Meta:
        verbose_name = 'User Relation'
        verbose_name_plural = 'User Relations'
        unique_together = ('user', 'related_with', 'relation_type')

    def __str__(self):
        return f'{self.user} is added {self.related_with} as {self.relation_type}'


class CloseFriendModel(MyBaseModel):
    close_friend = models.ForeignKey(
        UserRelationModel, on_delete=models.PROTECT, verbose_name='Close friend',
        related_name='close_friends_relations')

    class Meta:
        verbose_name = 'Close friend'
        verbose_name_plural = 'Close friend'

    def __str__(self):
        return str(self.close_friend)
