from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password
from django.core.exceptions import FieldError
from usuarios.models import Usuario

# Modificar un usuario
@api_view(['PUT'])
def prueba_privada(request):
    return Response({'mensaje': 'Vista protegida'}, status=200)

# Eleminar un usuario
@api_view(['PUT'])
def prueba_privada(request):
    return Response({'mensaje': 'Vista protegida'}, status=200)
