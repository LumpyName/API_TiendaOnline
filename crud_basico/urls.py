from django.urls import path
from .views import ModificarUsuarioView

urlpatterns = [
    path('modify_user/', ModificarUsuarioView.as_view(), name='modify_user'),
]
