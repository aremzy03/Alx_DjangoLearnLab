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
    path('follow/<int:user_id>', Follow.as_view(), name='follow'),
    path('unfollow/<int:user_id>', UnFollow.as_view(), name='unfollow'),
]
