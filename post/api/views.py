from rest_framework.viewsets import ModelViewSet
from post.models import Post
from post.api.serializers import PostSerializer
from post.api.permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class PostApiViewSet(ModelViewSet):
    #queryset = Post.objects.all()
    queryset = Post.objects.filter(published=True)
    serializer_class = PostSerializer
    permission_classes = [IsAdminOrReadOnly]
    # lookup_field = 'slug' # para buscar por slug en vez de id
    filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['category'] # filtrar por la id de categoria del post http://127.0.0.1:8000/api/posts/?category=1
    filterset_fields = ['category','category__slug'] # filtrar por el slug de categoria del post http://127.0.0.1:8000/api/posts/?category__slug=react
    