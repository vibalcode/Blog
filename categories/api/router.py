from rest_framework.routers import DefaultRouter
from categories.api.views import CategoryApiViewSet

router = DefaultRouter()
router.register(prefix='categories', viewset=CategoryApiViewSet, basename='categories')
urlpatterns = router.urls
