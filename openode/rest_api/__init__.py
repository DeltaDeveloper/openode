
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from openode.models import Node, Post

################################################################################
# USER
################################################################################

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')  # perms, ...


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



################################################################################
# Node
################################################################################

class NodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Node
        fields = ('title', 'parent', )  # TODO

class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer

################################################################################
# Question
###############################################################################

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('post_type', )

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()  # TODO
    serializer_class = QuestionSerializer

################################################################################

class DocumentViewSet(viewsets.ModelViewSet):
    pass

class AnswerViewSet(viewsets.ModelViewSet):
    pass

class CommentViewSet(viewsets.ModelViewSet):
    pass

# TODO

################################################################################

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'nodes', NodeViewSet)
router.register(r'questions', QuestionViewSet)
# TODO
