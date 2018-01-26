from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from sku.serializers import UserSerializer, GroupSerializer, CommentSerializer
from .models import Comment


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created')
    serializer_class = CommentSerializer  
