from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pic', blank='True', null='True', verbose_name='Profile Pic')
    bio = models.TextField(max_length=500, blank='True', null='True')

    def __str__(self):
        return str(self.username)
