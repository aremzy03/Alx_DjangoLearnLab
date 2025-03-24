from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import CustomUser

#serilizer classes here
class CustomUserSerilizer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['name', 'bio', 'profile_picture', 'followers']

class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(max_length=150, write_only=True)
    token = serializers.CharField(read_only=True)
    
    def validate(self, attrs):
        
        user = authenticate(username=attrs['username'], password=attrs['password'])
        if not user:
            raise serializers.ValidationError('Invalid Credentials')
        attrs['user'] = user
        return attrs
    
    def create(self, validated_data):
        user = validated_data['user']
        token,_ = Token.objects.get_or_create(user=user)
        return {'token': token.key}
    #get_user_model().objects.create_user Token.objects.create