from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer,UserSerializer as BaseUserSerializer , TokenCreateSerializer as BaseTokenCreateSerializer ,CurrentPasswordSerializer as BaseCurrentPasswordSerializer,UserDeleteSerializer as BaseUserDeleteSerializer
from django.contrib.auth import authenticate, login
from .models import User
from rest_framework import status
from django.urls import reverse



class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['email','username','password','first_name','last_name']

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['email','username','first_name','last_name']


# class TokenCreateSerializer(BaseTokenCreateSerializer):
#     pass
# class CurrentPasswordSerializer(BaseCurrentPasswordSerializer):
#     pass