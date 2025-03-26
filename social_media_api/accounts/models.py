from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following_users', blank=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers_users', blank=True)
    
    groups = models.ManyToManyField('auth.Group', related_name='customuser_set', blank=True)
    
    user_permissions = models.ManyToManyField('auth.Permission', related_name='customuser_permission', blank=True)

    def __str__(self):
        return self.username

