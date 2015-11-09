from django.contrib.auth.models import User
from rest_framework import viewsets

from openode.models import Node, Post
from openode.rest_api import serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = serializers.NodeSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()  # TODO
    serializer_class = serializers.QuestionSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    pass

class AnswerViewSet(viewsets.ModelViewSet):
    pass

class CommentViewSet(viewsets.ModelViewSet):
    pass