from rest_framework.viewsets import ModelViewSet
from categories.models import Category
from categories.api.serializers import CategorySerializer

class CategoryApiViewSet(ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer