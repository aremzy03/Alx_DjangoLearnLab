from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# routers
router = DefaultRouter()
router.register(r'posts', PostViews, basename='post-views')
router.register(r'comments', CommentViews, basename='comments')

# urls
urlpatterns = [
	path('', include(router.urls), name='list-post'),
]
