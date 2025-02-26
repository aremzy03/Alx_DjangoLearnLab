from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    
    class Meta:
        permissions = [
            ("can_view", "Can view"),
            ("can_create", "Can create"),
            ("can_edit", "Can edit"),
            ("can_delete", "Can delete"),
        ]
    
    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have a username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password=None):
        user = self.create_user(username, password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    
    def __str__(self):
        return self.username

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to="profile_photos", null=True, blank=True)
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.username
