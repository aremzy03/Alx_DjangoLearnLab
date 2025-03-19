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
    path('post/', ListPost.as_view(), name='posts'),
    path('post/create/', CreatePost.as_view(), name='create-post'),
    path('post/<int:pk>/', DetailPost.as_view(), name='detail-post'),
    path('post/<int:pk>/edit', UpdatePost.as_view(), name='edit-post'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='delete-post')
]
