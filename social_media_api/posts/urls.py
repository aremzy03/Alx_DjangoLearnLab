from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# routers
router = DefaultRouter()
router.register(r'posts', PostViews, basename='post-views')
router.register(r'comments', CommentViews, basename='comments')
router.register(r'feed', FollowingPostViews, basename='following-views')

# urls
urlpatterns = [
	path('', include(router.urls), name='list-post'),
    path('posts/<int:pk>/like/', LikeView.as_view(), name='like'),
    path('posts/<int:pk>/unlike/', LikeView.as_view(), name='unlike'),
]
