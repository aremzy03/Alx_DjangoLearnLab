from rest_framework import serializers
from rest_framework.authtoken.models import Token

from django.contrib.auth import get_user_model
from .models import CustomUser

#serilizer classes here
class CustomUserSerilizer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['bio', 'profile_picture', 'followers', 'following']

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        #user = validated_data['user']
        user = get_user_model().objects.create_user(**validated_data)
        token = Token.objects.create(user=user)
        return user