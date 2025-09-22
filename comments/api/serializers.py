from rest_framework import serializers
from comments.models import Comment

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content', 'created_at', 'updated_at', 'user', 'post']
        read_only_fields = ['id', 'created_at', 'updated_at']