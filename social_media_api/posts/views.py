from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from .models import Post, Comment
from .serializers import CommentSerializer, PostSerializer


# Create your views here.
#Post CRUD Operations
class PostViews(ModelViewSet, PageNumberPagination):
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
class CommentViews(ModelViewSet, IsAuthenticated):
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