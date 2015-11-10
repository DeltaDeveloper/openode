from django.contrib.auth.models import User
from rest_framework import viewsets

from openode.models import Node, Thread
from openode import const
from openode.rest_api import serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class NodeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DetailNodeSerializer
    model = Node

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Thread.objects.filter(
        is_deleted=False,
        thread_type=const.THREAD_TYPE_QUESTION)
    serializer_class = serializers.QuestionSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Thread.objects.filter(
        is_deleted=False,
        thread_type=const.THREAD_TYPE_DOCUMENT)
    serializer_class = serializers.DocumentSerializer


class DiscussionViewSet(viewsets.ModelViewSet):
    queryset = Thread.objects.filter(
        is_deleted=False,
        thread_type=const.THREAD_TYPE_DISCUSSION)
    serializer_class = serializers.DiscussionSerializer


class CommentViewSet(viewsets.ModelViewSet):
    pass