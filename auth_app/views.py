from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from auth_app.serializer import UsuarioRegistroSerializer, CustomTokenObtainPairSerializer

# Revocacion de tokens
class LogoutView(APIView):

    @staticmethod
    def post(request):
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
    serializer_class = CustomTokenObtainPairSerializer


# Clase pesonalizada parar realizar el registro de usuario
class RegistroUsuarioView(APIView):

    @staticmethod
    def post(request):
        serializer = UsuarioRegistroSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.is_active = True
            user.save()

            return Response({'mensaje': 'Usuario creado correctamente'})

        # En caso de que envie la solicitud incompleto
        return Response(serializer.errors, status=400)
