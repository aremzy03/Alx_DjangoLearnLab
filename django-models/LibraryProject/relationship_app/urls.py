from django.urls import path
from .views import *
urlpatterns = [
    path("", index, name="index"),
	path("books/", display_books, name="books"),
    path("library/<int:pk>/", Librarybook.as_view(), name="library")
]
