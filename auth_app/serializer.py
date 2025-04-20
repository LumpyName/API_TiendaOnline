import re

from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken



class UsuarioRegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }


    @staticmethod
    def validate_password(value):

        errores = []

        if len(value) < 12:
            errores.append("La contraseña debe tener al menos 12 caracteres.")

        if not re.search(r"[a-z]", value):
            errores.append("La contraseña debe contener al menos una letra minúscula.")

        if not re.search(r"[A-Z]", value):
            errores.append("La contraseña debe contener al menos una letra mayúscula.")

        if not re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]", value):
            errores.append("La contraseña debe contener al menos un carácter especial.")

        if errores:
            raise serializers.ValidationError(errores)

        return value


    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])  # Hasheamos
        return super().create(validated_data)


# Clase para que el usuario logee
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        user = get_user_model()

        try:
            user = user.objects.get(username=username)
        except user.DoesNotExist:
            raise AuthenticationFailed("Usuario no encontrado.")

        if not user.check_password(password):
            raise AuthenticationFailed("Contraseña incorrecta.")

        # Generamos los tokens
        refresh = RefreshToken.for_user(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
