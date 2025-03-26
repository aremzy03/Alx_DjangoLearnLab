from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from .models import CustomUser, Post, Comment
from .serializers import CustomUserSerilizer, UserRegisterSerializer, CommentSerializer, PostSerializer

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

#Post CRUD Operations
class ListPost(generics.ListAPIView, PageNumberPagination):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'content', 'author']
    page_size = 5
    page_size_query_param = 'size'
    max_page_size = 100

class CreatePost(generics.CreateAPIView, IsAuthenticated):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class DetailPost(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class DeletePost(generics.DestroyAPIView, IsAuthenticated):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user

class UpdatePost(generics.UpdateAPIView, IsAuthenticated):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user

#Comment 
class CreateComment(generics.CreateAPIView, IsAuthenticated):
    queryset = Comment.objects.all()
    serializer_class = PostSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ListComment(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class UpdateComment(generics.UpdateAPIView, IsAuthenticated):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user

class DeleteComment(generics.DestroyAPIView, IsAuthenticated):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user