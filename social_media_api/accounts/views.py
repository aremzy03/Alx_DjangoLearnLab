from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from rest_framework.mixins import UpdateModelMixin
from rest_framework.generics import UpdateAPIView, RetrieveAPIView
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import CustomUserSerilizer, UserLoginSerializer

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

@api_view(['POST'])
def login(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogout(LogoutView):
    template_name = ''
    next_page = reverse_lazy('home')


class UpdateProfile(UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerilizer


class ViewProfile(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerilizer
