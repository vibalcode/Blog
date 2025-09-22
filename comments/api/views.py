from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from comments.models import Comment
from comments.api.serializers import CommentsSerializer

class CommentsApiViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    filter_backends = [OrderingFilter]
    ordering = ['-created_at'] # sirve para ordenar de forma descendente ['-created_at'] y ascendente ['created_at']
    #ordering_fields = ['created_at'] # sirve para ordenar de forma descendente