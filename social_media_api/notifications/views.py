from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from .serializers import NotificationSerializer
from .models import Notification

# Create your views here.
class ViewNotifications(generics.ListAPIView):
    authentication_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationSerializer
    
    def get_queryset(self):
        query_set = Notification.objects.filter(recipient=self.request.user).order_by("-timestamp")
        return query_set