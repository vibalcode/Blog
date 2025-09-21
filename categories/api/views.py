from rest_framework.viewsets import ModelViewSet
from categories.models import Category
from categories.api.serializers import CategorySerializer
from categories.api.permisions import IsAdminOrReadOnly

class CategoryApiViewSet(ModelViewSet):
  permission_classes = [IsAdminOrReadOnly]
  queryset = Category.objects.all()
  serializer_class = CategorySerializer