from rest_framework import routers
from openode.rest_api import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'nodes', views.NodeViewSet)
router.register(r'nodeusers', views.NodeUserViewSet)
router.register(r'questions', views.QuestionViewSet)
router.register(r'discussions', views.DiscussionViewSet)
router.register(r'documents', views.DocumentViewSet)
router.register(r'categories', views.CategoryViewSet)
