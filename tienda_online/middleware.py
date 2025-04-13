from django.http import JsonResponse
from django.conf import settings
from django.urls import resolve, Resolver404

class AppendSlashMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            # Intentamos resolver la ruta actual
            resolve(request.path_info)
        except Resolver404:
            # Si APPEND_SLASH está activado y no hay slash final
            if settings.APPEND_SLASH and not request.path_info.endswith('/'):
                corrected_path = request.path_info + '/'
                try:
                    resolve(corrected_path)
                    return JsonResponse({
                        'error': 'La URL está mal formada. Agrega una "/" al final.',
                        'sugerencia': f'Usa {corrected_path} en su lugar.'
                    }, status=400)
                except Resolver404:
                    pass  # tampoco existe con slash, sigue al error real

        # Si no hay error, sigue normalmente
        return self.get_response(request)
