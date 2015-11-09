from django.contrib.auth.models import User
from rest_framework import serializers

from openode.models import Node, Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')  # perms, ...


class ListNodeSerializer(serializers.ModelSerializer):
    """
    This serializer is used only for listing
    """
    class Meta:
        model = Node
        fields = ('title', 'parent', 'id')


class DetailNodeSerializer(serializers.ModelSerializer):
    """
    Detail serializer with unpacked data
    """
    class Meta:
        model = Node


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('post_type', )
