from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
class AdminModel(UserAdmin):
    list_display= ("username","first_name","last_name","date_of_birth", "profile_photo")

admin.site.register(CustomUser, AdminModel)