from django.urls import path
from .views import list_books, index, LibraryDetailView, RegisterUserView, admin_view, librarian_view, create_book, change_book, delete_book #, Login_view, Logout_view
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", index, name="index"),
	path("books/", list_books, name="books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library"),
    path("register/", RegisterUserView.as_view(), name="views.register"),
    #path("login/", login_view, name="login"),
    path("login/", LoginView.as_view(template_name= "relationship_app/login.html"), name="login"),
    #path("login/", Login_view.as_view(), name="login"),
    #path("logout/", logout_view, name="logout"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("admin/", admin_view, name="admin" ),
    path("librarian", librarian_view, name="librarian"),
    path("create_book/", create_book, name="create_book"),
    path("edit_book/", change_book, name="edit_book"),
    path("delete_book/", delete_book, name="delete_book"),
    ]
