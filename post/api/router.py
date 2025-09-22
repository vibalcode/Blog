from rest_framework.routers import DefaultRouter
from post.api.views import PostApiViewSet

router = DefaultRouter()
router.register(r'posts', PostApiViewSet, basename='posts')
urlpatterns = router.urls