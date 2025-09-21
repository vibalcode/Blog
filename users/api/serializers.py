from rest_framework import serializers
from users.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}} # para que la contraseña no se devuelva en las respuestas

    def create(self, validated_data):
        # Usamos el método create_user para crear un usuario con la contraseña hasheada
        # Validar que la contraseña tenga al menos 8 caracteres
        # quitar los espacios en blanco del inicio y final de la contraseña
        validated_data['password'] = validated_data['password'].strip().replace(" ", "")
        if len(validated_data['password']) < 8:
            raise serializers.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name')
