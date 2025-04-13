from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password
from django.core.exceptions import FieldError
from .serializer import UsuarioRegistroSerializer
from usuarios.models import Usuario

# vdjango.contrib.auth.hashers
# rest_framework.authtoken.models

@api_view(['POST'])
@permission_classes([AllowAny])  # Público
def register_usuario(request):
    serializer = UsuarioRegistroSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'mensaje': 'Usuario creado correctamente'})
    return Response(serializer.errors, status=400)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_usuario(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Faltan datos'}, status=400)

    try:
        usuario = Usuario.objects.get(username=username)

    except Usuario.DoesNotExist:
        return Response({'error': 'Usuario no encontrado'}, status=404)

    except FieldError as error:
        return Response(
            {'error': error},
            status=400
        )

    if not check_password(password, usuario.password):
        return Response({'error': 'Contraseña incorrecta'}, status=401)

    # Obtener o crear token
    token, created = Token.objects.get_or_create(user=usuario)

    return Response({'token': token.key})