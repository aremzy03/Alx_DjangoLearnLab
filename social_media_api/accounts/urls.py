from django.urls import path
from .views import *

# accounts urls here
urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='user-login'),
    path('logout/', UserLogout.as_view(), name='user-logout'),
    path('profile/',ViewProfile.as_view(), name='profile'),
    path('profile/update/', UpdateProfile.as_view(), name='update-profile'),
    path('create-token/', create_token, name='create-token'),
]
