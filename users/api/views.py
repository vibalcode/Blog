from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User
from users.api.serializers import UserRegisterSerializer, UserSerializer, UserUpdateSerializer
from rest_framework.permissions import IsAuthenticated

class RegisterView(APIView):
    def post(self, request):
      serializer = UserRegisterSerializer(data=request.data) # a request.data le pasas los datos que vienen en el request
      if serializer.is_valid(raise_exception=True):
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class UserView(APIView):
    permission_classes = [IsAuthenticated] # para que solo usuarios autenticados puedan acceder a esta vista
    
    def get(self, request):
        user = request.user # obtenemos el usuario autenticado
        serializer = UserSerializer(user) # serializamos el usuario
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request):
        user = User.objects.get(id=request.user.id) # obtenemos el usuario autenticado
        serializer = UserUpdateSerializer(user, data=request.data, partial=True) # partial=True para que no sea obligatorio enviar todos los campos
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)