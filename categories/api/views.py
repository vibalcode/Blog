from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from categories.models import Category
from categories.api.serializers import CategorySerializer
from categories.api.permisions import IsAdminOrReadOnly

class CategoryApiViewSet(ModelViewSet):
  permission_classes = [IsAdminOrReadOnly]
  queryset = Category.objects.all() # nos traera todas las categorias sin filtro
  #queryset = Category.objects.filter(published=True) # solo las categorias publicadas
  serializer_class = CategorySerializer
  lookup_field = 'slug' # para buscar por slug en vez de id
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['published'] # para filtrar por el campo published