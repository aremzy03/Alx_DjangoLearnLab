from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import permissions
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from accounts.models import CustomUser
from .models import Post, Comment
from .serializers import CommentSerializer, PostSerializer


# Create your views here.
#Post CRUD Operations
class PostViews(viewsets.ModelViewSet, PageNumberPagination):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'content', 'author']
    page_size = 5
    page_size_query_param = 'size'
    max_page_size = 100

class FollowingPostViews(viewsets.ModelViewSet, PageNumberPagination):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'content', 'author']
    page_size = 5
    page_size_query_param = 'size'
    max_page_size = 100
    
    def get_queryset(self):
        user = self.request.user
        profile = CustomUser.objects.get(user=user)
        following_users = profile.following.all()
        return Post.objects.filter(author__in=following_users).order_by("created_at")


class CreatePost(generics.CreateAPIView, permissions.IsAuthenticated):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class DetailPost(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class DeletePost(generics.DestroyAPIView):
    permission_classes = [ permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user

class UpdatePost(generics.UpdateAPIView):
    permission_classes = [ permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user

#Comment 
class CommentViews(viewsets.ModelViewSet):
    permission_classes = [ permissions.IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = PostSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ListComment(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class UpdateComment(generics.UpdateAPIView):
    permission_classes = [ permissions.IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user

class DeleteComment(generics.DestroyAPIView):
    permission_classes = [ permissions.IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user