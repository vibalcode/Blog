
# generar permiso personalizado para que solo el autor del comentario pueda editar o eliminar su comentario y los demas usuarios solo puedan ver los comentarios y crear nuevos comentarios
from rest_framework.permissions import BasePermission, SAFE_METHODS
from comments.models import Comment
class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # los metodos seguros (GET, HEAD, OPTIONS) son permitidos para cualquier usuario
        if request.method in SAFE_METHODS:
            return True
        # los metodos no seguros (POST, PUT, DELETE) solo son permitidos para el autor del comentario
        return obj.user == request.user

# Cualquier usuario autenticado puede crear comentarios, siempre que la vista lo permita. El permiso IsAuthorOrReadOnly solo restringe la edición y eliminación a los autores, pero no impide la creación de nuevos comentarios por otros usuarios. Normalmente, la creación (POST) se controla en la vista y el serializer, no en este permiso.