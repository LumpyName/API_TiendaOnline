from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView  # Aquí es donde importamos TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import timedelta
from django.utils import timezone

from auth_app.serializer import UsuarioRegistroSerializer
from usuarios.models import Usuario

# Clase personalizada para obtener el token de acceso
class CustomTokenObtainPairView(TokenObtainPairView):
    # Aquí puedes agregar personalización si la necesitas
    pass


# Clase para refrescar el token si el usuario ha sido activo
class TokenRefreshViewWithActivity(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        last_activity = user.last_activity  # Usamos la última actividad registrada

        # Verificar si el token no ha expirado y hubo actividad en la última hora
        if last_activity and timezone.now() - last_activity < timedelta(hours=1):
            # Generar un nuevo token de acceso
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token)
            })

        # Si la actividad fue hace más de 1 hora, el token expiró
        return Response({
            'detail': 'El token expiró, por favor inicie sesión nuevamente.'
        })


# Clase para actualizar la fecha de última actividad
class ActualizarUltimaActividadView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Actualizar la última actividad del usuario
        request.user.last_login = timezone.now()  # Aquí registramos la actividad actual
        request.user.save()
        return Response({"detail": "Última actividad registrada correctamente."})


# Clase para refrescar el token manualmente
class RefreshTokenManuallyView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        refresh = RefreshToken.for_user(user)
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        })


class RegistroUsuarioView(APIView):
    def post(self, request):
        serializer = UsuarioRegistroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje': 'Usuario creado correctamente'})

        # En caso de que envie la solicitud incompleto
        return Response(serializer.errors, status=400)
