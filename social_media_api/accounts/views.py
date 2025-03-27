from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import viewsets
from .models import CustomUser
from .serializers import CustomUserSerilizer, UserRegisterSerializer
from notifications.models import Notification

# Create your views here.

class RegisterUser(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)  # Generate Token
            return Response({"message": "User registered successfully", "token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def create_token(request):
    token = Token.objects.create(user=request.user)
    return HttpResponse(request, f'this is you token:{token.key}')


class UserLogin(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
	


class UserLogout(APIView):
    def post(self, request):
        try:
            request.user.auth_token.delete()
        except Exception:
            pass
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)



class UpdateProfile(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerilizer


class ViewProfile(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerilizer

# Follow Management Views
class CustomPermission(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        return request.user == obj.user

class Follow(generics.GenericAPIView):
    permission_classes = [CustomPermission]
    
    def post(self, request, user_id):
        follow = get_object_or_404(CustomUser, id=user_id)
        user = request.user
        if user == follow:
            return Response({'error':"You can't follow your self"}, status=status.HTTP_400_BAD_REQUEST)
        
        user.following.add(follow)
        follow.followers.add(user)
        
        #Create Notification
        Notification.objects.create(
            recipient = follow,
            actor = user,
            verb = f"{user} just followed you",
            content_type = ContentType.objects.get_for_model(CustomUser),
            object_id = follow.id
        )
        return Response({'message':f"you're now following {follow.first_name}"}, status=status.HTTP_200_OK)

class UnFollow(generics.GenericAPIView):
    permission_classes = [CustomPermission]
    
    
    def post(self, request, user_id):
        user = request.user
        following = get_object_or_404(CustomUser, id=user_id)
        if user == following:
            return Response({'error':"You can't unfollow your self"}, status=status.HTTP_400_BAD_REQUEST)
        user.following.remove(following)
        following.followers.remove(user)
        return Response({'message':f"you're now unfollowing {following.first_name}"}, status=status.HTTP_200_OK)
    