from rest_framework.serializers import ModelSerializer
from post.models import Post
from users.api.serializers import UserSerializer
from categories.api.serializers import CategorySerializer

class PostSerializer(ModelSerializer):
    user = UserSerializer() # agrega toda la info del usuario relacionado al post
    category = CategorySerializer()
    
    class Meta:
        model = Post
        fields = ('title', 'content', 'slug', 'image', 'created_at', 'published', 'user', 'category')