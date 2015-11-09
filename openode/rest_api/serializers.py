from django.contrib.auth.models import User
from rest_framework import serializers

from openode.models import Node, Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class DetailNodeSerializer(serializers.ModelSerializer):
    """
    Detail serializer with unpacked data
    """
    questions = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True, source='get_questions'
    )

    documents = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True, source='get_documents'
    )

    discussions = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True, source='get_discussions'
    )

    class Meta:
        model = Node


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('post_type', )
