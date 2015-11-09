from django.contrib.auth.models import User
from rest_framework import serializers

from openode.models import Node, Post


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')  # perms, ...


class NodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Node
        fields = ('title', 'parent', 'id')  # TODO


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('post_type', )
