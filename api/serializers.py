from django.contrib.auth.models import User
from .models import  Message
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
 class Meta:
  model = User
  fields = ['id', 'username', 'email']

class MessageSerializer(serializers.ModelSerializer):
 created_by = UserSerializer(read_only =True, many = False)
 class Meta:
  model = Message
  fields = ['id', 'message', 'created_on','updated_on','created_by']