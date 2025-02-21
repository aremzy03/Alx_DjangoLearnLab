from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *
urlpatterns = [
    path("", index, name="index"),
	path("books/", display_books, name="books"),
    path("library/<int:pk>/", Librarybook.as_view(), name="library"),
    path("register/", RegisterUserView.as_view(), name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]
