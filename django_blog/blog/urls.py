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
    path('profile/update', UpdateProfile.as_view(), name='update-profile'),
    path('profile/', viewprofile, name='view-profile'),
    path('profile/create', CreateProfile.as_view(), name='create-profile'),

    # Posts CRUD urls
    path('posts/', ListPost.as_view(), name='posts'),
    path('post/new/', createpost, name='create-post'),
    path('post/<int:pk>/', DetailPost.as_view(), name='detail-post'),
    path('post/<int:pk>/update/', UpdatePost.as_view(), name='edit-post'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete-post'),

    # search and tags filter
    path('tags/<str:tag>/', TagListPost.as_view(), name='tag-list'),
    path('search/', SearchPostList.as_view(), name='search-post'),

    # Comments CRUD urls
    path('post/<int:pk>/comments/new/', commentform, name='create-comment'),
    path('post/comment/<int:pk>/delete/',
         CommentDeleteView.as_view(), name='delete-comment'),
    path('post/comment/<int:pk>/update/',
         CommentUpdateView.as_view(), name='edit-comment'),
]
