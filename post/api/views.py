from rest_framework.viewsets import ModelViewSet
from post.models import Post
from post.api.serializers import PostSerializer
from post.api.permissions import IsAdminOrReadOnly

class PostApiViewSet(ModelViewSet):
    #queryset = Post.objects.all()
    queryset = Post.objects.filter(published=True)
    serializer_class = PostSerializer
    permission_classes = [IsAdminOrReadOnly]
    # lookup_field = 'slug' # para buscar por slug en vez de id