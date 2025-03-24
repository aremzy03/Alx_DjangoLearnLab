from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from rest_framework.mixins import UpdateModelMixin
from rest_framework.generics import UpdateAPIView, RetrieveAPIView
from rest_framework.authtoken.models import Token
from .models import CustomUser
from .serializers import CustomUserSerilizer

# Create your views here.


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = ''
    success_url = reverse_lazy('create-profile')


def create_token(request):
    token = Token.objects.create(user=request.user)
    return HttpResponse(request, f'this is you token:{token.key}')


class UserLogin(LoginView):
    template_name = ''
    success_url = reverse_lazy('profile')


class UserLogout(LogoutView):
    template_name = ''
    next_page = reverse_lazy('home')


class UpdateProfile(UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerilizer


class ViewProfile(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerilizer
