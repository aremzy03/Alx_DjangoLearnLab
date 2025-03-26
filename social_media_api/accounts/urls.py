from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

# # routers here
# router = DefaultRouter()
# router.register(r'pofile')
# accounts urls here
urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='user-login'),
    path('logout/', UserLogout.as_view(), name='user-logout'),
    path('profile/',ViewProfile.as_view(), name='profile'),
    path('profile/update/', UpdateProfile.as_view(), name='update-profile'),
    path('create-token/', create_token, name='create-token'),
    path('posts/', ListPost.as_view(), name='list-post'),
    path('posts/create/', CreatePost.as_view(), name='create-post'),
    path('posts/<int:pk>/', DetailPost.as_view(), name='detail-post'),
    path('posts/<int:pk>/delete', DeletePost.as_view(), name='delete-post'),
    path('posts/<int:pk>/update', UpdatePost.as_view(), name='update-post'),
]
