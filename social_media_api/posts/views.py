from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType
from rest_framework import generics
from rest_framework import permissions
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import CustomUser
from .models import Post, Comment, Like
from .serializers import CommentSerializer, PostSerializer
from notifications.models import Notification


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

#Like and Unlike View
class LikeView(APIView):
    authentication_classes = [permissions.IsAuthenticated]
    
    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            like.delete()
            return Response({'message':"Post unliked"}, status.HTTP_200_OK)
        else:
            #Create Notification
            Notification.objects.create(
            recipient = post.author,
            actor = request.user,
            verb = f"{request.user} just liked your post '{post.title}'",
            content_type = ContentType.objects.get_for_model(Post),
            object_id = post.id
            )
            return Response({'message':"Post unliked "}, status.HTTP_200_OK)