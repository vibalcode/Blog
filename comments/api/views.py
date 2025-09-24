from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from comments.models import Comment
from comments.api.serializers import CommentsSerializer
from comments.api.permissions import IsAuthorOrReadOnly

class CommentsApiViewSet(ModelViewSet):
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    # OrderingFilter 
    filter_backends = [OrderingFilter, DjangoFilterBackend] # OrderingFilter permite ordenar los resultados y DjangoFilterBackend permite filtrar los resultados
    ordering = ['-created_at'] # sirve para ordenar de forma descendente ['-created_at'] y ascendente ['created_at']
    #ordering_fields = ['created_at'] # sirve para ordenar de forma descendente
    filterset_fields = ['post', 'user'] # sirve para filtrar por post y user ejemplo: http://127.0.0.1:8000/api/comments/?post=2