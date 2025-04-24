import re

from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken



class UsuarioRegistroSerializer(serializers.ModelSerializer):
    """
        Serializador para la creación y validación de nuevos usuarios.

        Este serializador se utiliza para registrar usuarios, asegurando que los datos de entrada
        cumplan con los requisitos de la aplicación. Incluye validación personalizada para el campo
        de contraseña, exigiendo una longitud mínima y la presencia de distintos tipos de caracteres
        (mayúsculas, minúsculas y caracteres especiales). Además, se encarga de hashear la contraseña
        antes de guardar el usuario en la base de datos.

        Funcionalidades:
            - Validación estricta de la contraseña según los criterios de seguridad definidos.
            - Excluye campos de solo lectura como 'date_joined' del proceso de creación.
            - Utiliza el modelo de usuario personalizado si está definido en el proyecto.

        Campos:
            - Todos los campos del modelo de usuario, excluyendo 'date_joined' como solo lectura.
        """

    class Meta:
        model = get_user_model()
        fields = '__all__'
        read_only_fields = ['date_joined']
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
    """
        Serializador personalizado para la autenticación de usuarios y la obtención de tokens JWT.

        Este serializador reemplaza la validación estándar de credenciales, permitiendo personalizar
        los mensajes de error para usuario no encontrado o contraseña incorrecta. Si la autenticación
        es exitosa, genera y retorna un par de tokens JWT (`refresh` y `access`) asociados al usuario.

        Funcionalidades:
            - Verifica que el usuario exista según el nombre de usuario proporcionado.
            - Comprueba que la contraseña ingresada sea correcta.
            - Devuelve mensajes de error específicos en caso de fallo.
            - Genera y retorna los tokens de autenticación JWT en caso de éxito.
        """

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
