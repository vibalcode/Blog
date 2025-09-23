from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from comments.models import Comment
from comments.api.serializers import CommentsSerializer

class CommentsApiViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering = ['-created_at'] # sirve para ordenar de forma descendente ['-created_at'] y ascendente ['created_at']
    #ordering_fields = ['created_at'] # sirve para ordenar de forma descendente
    filterset_fields = ['post'] # sirve para filtrar por post y user ejemplo: http://127.0.0.1:8000/api/comments/?post=2