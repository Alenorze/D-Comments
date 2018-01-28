from django.contrib.auth.models import User, Group

from rest_framework import serializers

from .models import Comment


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta(object):
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta(object):
        model = Group
        fields = ('url', 'name')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta(object):
        model = Comment
        fields = ('id', 'url', 'username', 'email', 'groups', 'tone', 'tone_is_positive')
