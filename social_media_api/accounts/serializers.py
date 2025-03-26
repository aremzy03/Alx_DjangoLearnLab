from rest_framework import serializers
from rest_framework.authtoken.models import Token

from django.contrib.auth import get_user_model
from .models import CustomUser, Post, Comment

#serilizer classes here
class CustomUserSerilizer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['bio', 'profile_picture', 'followers']

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

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__' 


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'