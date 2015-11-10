from django.contrib.auth.models import User
from rest_framework import serializers

from openode.models import Node, Thread


class TagListField(serializers.WritableField):
    def from_native(self, data):
        return data.split()

    def to_native(self, obj):
        if type(obj) is not list:
            return [tag.name for tag in obj.all()]
        return obj

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


class ThreadSerializer(serializers.ModelSerializer):
    tags = TagListField(source='tags')
    description = serializers.CharField(source='description.text')
    author = serializers.CharField(source='description.author')
    summary = serializers.CharField(source='description.summary')
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


class DocumentSerializer(ThreadSerializer):
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
