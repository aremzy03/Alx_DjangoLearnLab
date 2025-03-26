from django.urls import path
from .views import *

urlpatterns = [
	path('posts/', ListPost.as_view(), name='list-post'),
    path('posts/create/', CreatePost.as_view(), name='create-post'),
    path('posts/<int:pk>/', DetailPost.as_view(), name='detail-post'),
    path('posts/<int:pk>/delete', DeletePost.as_view(), name='delete-post'),
    path('posts/<int:pk>/update', UpdatePost.as_view(), name='update-post'),
]
