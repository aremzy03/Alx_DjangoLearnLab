from django.urls import path
from .views import *


# urls here

urlpatterns = [
    # Home View
    path('', home, name='home'),

    # Authenticaton urls
    path('register/', UserRegister.as_view(), name='register'),
    path('login/', UserLogin.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', UserLogout.as_view(template_name='blog/logout.html'), name='logout'),
    path('profile/update', UpdateProfile.as_view(), name='profile'),
    path('profile/', viewprofile, name='viewprofile'),
    path('profile/create', CreateProfile.as_view(), name='create-profile'),

    # Posts CRUD urls
    path('posts/', ListPost.as_view(), name='posts'),
    path('posts/new/', CreatePost.as_view(), name='create-post'),
    path('posts/<int:pk>/', DetailPost.as_view(), name='detail-post'),
    path('posts/<int:pk>/edit', UpdatePost.as_view(), name='edit-post'),
    path('posts/<int:pk>/delete', PostDeleteView.as_view(), name='delete-post')
]
