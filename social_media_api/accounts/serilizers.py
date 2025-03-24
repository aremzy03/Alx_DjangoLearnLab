from rest_framework import serializers
from .models import CustomUser

#serilizer classes here
class CustomUserSerilizer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['name', 'bio', 'profile_picture', 'followers']
