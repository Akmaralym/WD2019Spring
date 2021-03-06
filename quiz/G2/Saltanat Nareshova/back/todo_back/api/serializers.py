from rest_framework import serializers
from api.models import Contact
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

class ContactSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
       model = Contact
       fields = ('id', 'name', 'phone', 'created_by')
