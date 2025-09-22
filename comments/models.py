from django.db import models
from users.models import User
from post.models import Post

# Create your models here.
class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', null=True) # la propiedad related_name sirve para hacer consultas inversas ejemplo user.comments.all() para obtener todos los comentarios de un usuario
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=True) # la propiedad related_name sirve para hacer consultas inversas ejemplo post.comments.all() para obtener todos los comentarios de un post

    def __str__(self):
        return self.content[:20]  # Return the first 20 characters of the comment