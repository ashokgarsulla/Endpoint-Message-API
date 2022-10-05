from django.shortcuts import render

from .serializers import UserSerializer, MessageSerializer
from rest_framework import viewsets
from .models import User, Message
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle




class UserViewSet(viewsets.ModelViewSet):
 queryset = User.objects.all()
 serializer_class = UserSerializer


class MessageViewSet(viewsets.ModelViewSet):
 queryset = Message.objects.all()
 serializer_class = MessageSerializer
 authentication_classes=[TokenAuthentication]
 permission_classes=[IsAuthenticated]
 throttle_classes=[UserRateThrottle]