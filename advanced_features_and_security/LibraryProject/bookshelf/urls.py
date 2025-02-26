from django.urls import path
from .views import *

urlpatterns = [
    path("view_book/", view_book, name="view_book"),
    path("create_book/", create_book, name="create_book"),
    path("edit_book/", edit_book, name="edit_book"),
    path("delete_book/", delete_book, name="delete_book"),
    path("assign_permissions/", assign_permissions, name="assign_permissions"),
]
