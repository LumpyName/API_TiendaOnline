from django.urls import path
from .views import prueba_privada

urlpatterns = [
    path('xd/', prueba_privada)
]
