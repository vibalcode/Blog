from rest_framework.routers import DefaultRouter
from comments.api.views import CommentsApiViewSet

router = DefaultRouter()
router.register(r'comments', CommentsApiViewSet, basename='comments')
urlpatterns = router.urls