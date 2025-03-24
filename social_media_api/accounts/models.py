from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(models.Model, AbstractUser):
    name = models.CharField(max_length=255)
    bio = models.TimeField()
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    followers = models.ManyToManyField('self', symmetrical=False)

    def __str__(self):
        return self.name
