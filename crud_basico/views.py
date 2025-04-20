from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.views import APIView
from rest_framework import status

USER = get_user_model()

# Modifica los datos del usuario en base al PUT que se iso a la API
class ModificarUsuarioView(APIView):
    @staticmethod
    def _validar_y_extraer_payload(access_token: str):
        try:
            token = AccessToken(access_token)
            return token.payload

        except TokenError as e:
            # Token inválido por cualquier motivo (expirado, manipulado, etc)
            return Response({'error': f'Token inválido: {str(e)}'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception:
            # Cualquier otro error inesperado
            return Response({'error': 'Ocurrió un error inesperado.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    def _verificar_usuario_existente(request, user_id): # Soy muy malo poniendo nombres XD, nooooooo (asjsjsjsjsj)
        # Buscar al usuario por ID
        try:
            usuario = USER.objects.get(id=user_id)

        except USER.DoesNotExist:
            return Response({'error': 'Usuario no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        data = request.data
        if not data:
            return Response(
                {'error': 'Debe enviar al menos un campo para modificar.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        return {
            'data': data,
            'user' : usuario
        }


    def put(self, request):
        try:
            # Verifica que el token de acceso sea válido y si lo es, extrae y devuelve su payload.
            token_decodificado_o_error = self._validar_y_extraer_payload(request.data["access_token"])

            if isinstance(token_decodificado_o_error, Response):
                return token_decodificado_o_error

            verificacion_usuario = self._verificar_usuario_existente(
                request, token_decodificado_o_error['user_id']
            )

            if isinstance(verificacion_usuario, Response):
                return verificacion_usuario

            usuario = verificacion_usuario['user']
            data = verificacion_usuario['data']

            campos_modificados = {}

            for campo, valor in data.items():
                if hasattr(usuario, campo):
                    setattr(usuario, campo, valor)
                    campos_modificados[campo] = f"Se modificó exitosamente a '{valor}'"

            if not campos_modificados:
                return Response(
                    {'error': 'Ningún campo proporcionado es válido.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            usuario.save()

            return Response(
                {
                    'mensaje': 'Modificaciones realizadas correctamente.',
                    'modificaciones': campos_modificados
                },
                status=status.HTTP_200_OK
            )

        except TokenError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print("Error al decodificar token:", e)
            return Response({'error': 'Error inesperado.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

