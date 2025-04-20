from django.urls import path
from .views import prueba_privada, ModificarUsuarioView

urlpatterns = [
    path('prueba/', ModificarUsuarioView.as_view(), name='prueba'),
    path('xd/', prueba_privada)
]
