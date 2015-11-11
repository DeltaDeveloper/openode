from django.contrib.auth.models import User
from rest_framework import serializers

from openode.models.post import Post
from openode.models.thread import (
    ThreadCategory, AttachmentFileNode, AttachmentFileThread)
from openode.models import Node, Thread, Tag
from openode.document.models import Document, DocumentRevision


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', )


class AttachmentFileNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttachmentFileNode
        fields = ('file_data', )


class DetailNodeSerializer(serializers.ModelSerializer):
    """
    Detailed serializer with unpacked data
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

    attachements = AttachmentFileNodeSerializer(source='attachment_files')

    class Meta:
        model = Node


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class AttachmentThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttachmentFileThread
        fields = ('file_data', )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer()
    class Meta:
        model = Post


class FileDocumentRevisionSerializer(serializers.ModelSerializer):
    url = serializers.URLField(source='file_data.url')
    icon = serializers.URLField(source='get_icon')

    class Meta:
        model = DocumentRevision


class FileDocumentSerializer(serializers.ModelSerializer):
    url = serializers.URLField(source='get_file_url')
    name = serializers.URLField(source='get_file_name')

    revisions = FileDocumentRevisionSerializer(source='revisions')

    class Meta:
        model = Document


class ThreadSerializer(serializers.ModelSerializer):
    tags = TagSerializer()
    main_post = PostSerializer(source='_main_post')
    title = serializers.CharField(source='get_title')
    attachements = AttachmentThreadSerializer(source='attachment_files')
    file_documents = FileDocumentSerializer(source='documents')


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

