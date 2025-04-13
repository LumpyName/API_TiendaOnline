from django.urls import path
from .views import register_usuario, login_usuario

urlpatterns = [
    path('register/', register_usuario, name="register"),
    path('login/', login_usuario, name="login"),
]
