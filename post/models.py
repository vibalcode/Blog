from django.db import models
from users.models import User
from categories.models import Category

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255) # charfield sirve para textos cortos
    content = models.TextField() #textfield sirve para textos largos
    slug = models.SlugField(max_length=255, unique=True) # slugfield sirve para urls amigables
    image = models.ImageField(upload_to='post/images/', null=True, blank=True) # imagefield sirve para imagenes
    published = models.BooleanField(default=False) # booleanfield sirve para valores booleanos
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add se usa para que se guarde la fecha y hora en la que se crea el objeto
    updated_at = models.DateTimeField(auto_now=True) # auto_now se usa para que se guarde la fecha y hora en la que se actualiza el objeto
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # foreignkey se usa para relaciones uno a muchos
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True) # foreignkey se usa para relaciones uno a muchos

    def __str__(self):
        return self.title