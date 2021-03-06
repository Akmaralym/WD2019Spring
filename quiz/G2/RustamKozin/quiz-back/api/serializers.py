from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Contact
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.authentication import TokenAuthentication


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


class ContactSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    phone = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Contact
        fields = '__all__'
