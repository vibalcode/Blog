
pip install django djangorestframework drf-yasg
django-admin startproject blog
python manage.py startapp users

# Crear el modelo
### models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

### admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User

# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass

# crear los estaticos en caso de que no se vea la documentación de swagger
python manage.py collectstatic

# login con jwt
pip install djangorestframework-simplejwt

# peticiones con filtros
pip install django-filter