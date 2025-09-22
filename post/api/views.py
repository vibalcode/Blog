from rest_framework.viewsets import ModelViewSet
from post.models import Post
from post.api.serializers import PostSerializer

class PostApiViewSet(ModelViewSet):
    #queryset = Post.objects.all()
    queryset = Post.objects.filter(published=True)
    serializer_class = PostSerializer