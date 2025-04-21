from django.urls import path
from .views import ModificarUsuarioView

urlpatterns = [
    path('prueba/', ModificarUsuarioView.as_view(), name='prueba'),
]
