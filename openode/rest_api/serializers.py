from django.contrib.auth.models import User
from rest_framework import serializers

from openode.models import Node, Thread, Tag
from openode.models.post import Post
from openode.models.thread import ThreadCategory


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', )


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


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id','name')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer()
    class Meta:
        model = Post


class ThreadSerializer(serializers.ModelSerializer):
    tags = TagSerializer()
    main_post = PostSerializer(source='_main_post')
    title = serializers.CharField(source='get_title')

    class Meta:
        model = Thread
        exclude = (
            'tagnames'
            'category',
            'question_flow_state',
            'question_flow_responsible_user',
            'question_flow_interviewee_user',
            'approved',
            'accepted_answer',
            'answer_accepted_at',
            'added_at',
            'points',
            'external_access'
        )


class QuestionSerializer(ThreadSerializer):
    answers = PostSerializer(source='get_answers')

    class Meta:
        model = Thread
        exclude = (
            'category',
            'tagnames',
            'approved',
            'accepted_answer',
            'answer_accepted_at',
            'points',
            'external_access'
        )


class DiscussionSerializer(ThreadSerializer):
    class Meta:
        model = Thread
        exclude = (
            'question_flow_state',
            'question_flow_responsible_user',
            'question_flow_interviewee_user',
            'approved',
            'accepted_answer',
            'answer_accepted_at',
            'added_at',
            'points',
            'external_access'
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreadCategory


class DocumentSerializer(ThreadSerializer):
    category = CategorySerializer()
    class Meta:
        model = Thread
        exclude = (
            'question_flow_state',
            'question_flow_responsible_user',
            'question_flow_interviewee_user',
            'approved',
            'accepted_answer',
            'answer_accepted_at',
            'added_at',
            'points',
        )

