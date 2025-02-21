from django.urls import path
from .views import list_books, index, LibraryDetailView, RegisterUserView#, Login_view, Logout_view
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path("", index, name="index"),
	path("books/", list_books, name="books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library"),
    path("register/", RegisterUserView.as_view(), name="register"),
    #path("login/", login_view, name="login"),
    path("login/", LoginView.as_view(template_name= "relationship_app/login.html"), name="login"),
    #path("login/", Login_view.as_view(), name="login"),
    #path("logout/", logout_view, name="logout"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
]
