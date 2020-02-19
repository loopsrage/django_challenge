from rest_framework import routers
from experts.views import ExpertViewSet
from content.views import ContentViewSet, ContentHeaderViewSet

router = routers.DefaultRouter()
router.register(r'experts', ExpertViewSet)
router.register(r'content', ContentViewSet)
router.register(r'contentheader', ContentHeaderViewSet)

urlpatterns = router.urls
