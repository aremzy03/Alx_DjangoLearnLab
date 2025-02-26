from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)
class AdminModel(UserAdmin):
    list_display= ("username","first_name","last_name","date_of_birth", "profile_photo")

admin.site.register(Book)
admin.site.register(CustomUser, AdminModel)