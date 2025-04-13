import re

from rest_framework import serializers
from usuarios.models import Usuario
from django.contrib.auth.hashers import make_password

class UsuarioRegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_password(self, value):

        errores = []

        if len(value) < 12:
            errores.append("La contraseña debe tener al menos 12 caracteres.")

        if not re.search(r"[a-z]", value):
            errores.append("La contraseña debe contener al menos una letra minúscula.")

        if not re.search(r"[A-Z]", value):
            errores.append("La contraseña debe contener al menos una letra mayúscula.")

        if not re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", value):
            errores.append("La contraseña debe contener al menos un carácter especial.")

        if errores:
            raise serializers.ValidationError(errores)

        return value


    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])  # Hasheamos
        return super().create(validated_data)
