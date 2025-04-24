"""
Script de vistas para el manejo de autenticación y registro de usuarios en la aplicación 'auth_app'.

Este módulo incluye clases y métodos relacionados con:
- Revocación de tokens JWT mediante inclusión en una lista negra.
- Generación de tokens personalizados utilizando un serializador especializado.
- Registro de nuevos usuarios con validación y activación inicial.

Clases:
- LogoutView: Proporciona funcionalidad para revocar tokens de renovación (refresh tokens).
- CustomTokenObtainPairView: Amplía la funcionalidad para obtener tokens de acceso y renovación personalizados.
- RegistroUsuarioView: Permite el registro de nuevos usuarios con datos validados.

Dependencias:
- Django REST Framework y Simple JWT para autenticación basada en tokens.
- Serializadores personalizados para el manejo de datos y lógica de negocio.
"""

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from auth_app.serializer import UsuarioRegistroSerializer, CustomTokenObtainPairSerializer

# Revocacion de tokens
class LogoutView(APIView):
    """
    Vista para revocar (incluir en lista negra) tokens de renovación para cerrar sesión de usuarios.

    Métodos:
        post(request): Maneja solicitudes POST para revocar un token de renovación dado.

    Uso:
        - Recibe un token de renovación desde el cliente en el cuerpo de la solicitud.
        - Revoca el token incluyéndolo en una lista negra para evitar su uso futuro.
        - Retorna HTTP 205 (Reset Content) en caso de éxito.
        - Retorna HTTP 400 (Bad Request) si el proceso falla.

    Ejemplo de cuerpo de solicitud:
    {
        "refresh": "<refresh_token_string>"
    }
    """


    @staticmethod
    def post(request):
        """
        Revoke a refresh token by blacklisting it.

        Args:
            request (Request): The incoming HTTP request containing the refresh token.

        Returns:
            Response: An HTTP response with status 205 if successful, or 400 if an error occurs.
        """
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print("Error inesperado en 'auth_app/views.py' line '22':", e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

# Clase personalizada para obtener el token de acceso
class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Custom view for obtaining JWT tokens using a custom serializer.

    Attributes:
        serializer_class: Specifies the custom serializer (CustomTokenObtainPairSerializer) to be used.

    Purpose:
        - Extends the default TokenObtainPairView to include additional data or customize token generation.
    """
    serializer_class = CustomTokenObtainPairSerializer


# Clase pesonalizada parar realizar el registro de usuario
class RegistroUsuarioView(APIView):
    """
    View for registering new users.

    Methods:
        post(request): Handles POST requests to create a new user.

    Usage:
        - Receives user registration data in the request body.
        - Validates the data using UsuarioRegistroSerializer.
        - Creates and activates the user if data is valid.
        - Returns a success message or validation errors.

    Example request body:
    {
        "username": "example_user",
        "password": "secure_password",
        "email": "user@example.com",
        ...
    }
    """

    @staticmethod
    def post(request):
        """
        Register a new user with the provided data.

        Args:
            request (Request): The incoming HTTP request containing user registration data.

        Returns:
            Response: An HTTP response with a success message or validation errors (status 400).
        """
        serializer = UsuarioRegistroSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.is_active = True
            user.save()

            return Response({'mensaje': 'Usuario creado correctamente'})

        # En caso de que envie la solicitud incompleto
        return Response(serializer.errors, status=400)
