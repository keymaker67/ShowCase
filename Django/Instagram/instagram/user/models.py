from django.db import models

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
        ordering = ('pk', )

    def __str__(self):
        raise NotImplementedError('Implement __str__ method')


# Create profile for users
class UserProfile(MyBaseModel):
    user = models.OneToOneField(User, on_delete=models.PROTECT)                         # Make relation to login user
    id_user = models.IntegerField(null=True, blank=True)
    public = models.BooleanField(null=False, blank=False, default=False)
    profile_picture = models.ImageField(upload_to='%Y/%m', null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'Users Profile'

    def __str__(self):
        return self.user

