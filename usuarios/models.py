"""
Módulo: models.py

Descripción:
Este módulo define los modelos de datos para la aplicación, incluyendo una implementación personalizada
del modelo de usuario (`Usuario`). Extiende la funcionalidad del modelo de usuario predeterminado de Django (`AbstractUser`)
para incorporar campos adicionales.

Modelos:
- Usuario:
  - Hereda de `AbstractUser` y agrega dos campos adicionales:
    1. `foto_perfil`: Un campo para almacenar imágenes de perfil de usuario. Opcional.
    2. `last_activity`: Un campo de fecha y hora para rastrear la última actividad del usuario.

Uso:
- Este módulo es utilizado principalmente por el sistema de autenticación y cualquier funcionalidad
  relacionada con usuarios que requiera personalización.

Campos Personalizados:
- `foto_perfil`: Almacena imágenes subidas por los usuarios en la carpeta `fotos_perfil/`.
- `last_activity`: Inicializado automáticamente al momento de la creación del usuario.

Notas:
- El método `__str__` devuelve una representación legible del usuario en el formato:
  `[<ID>] <username> - <first_name>`.

Dependencias:
- `django.utils.timezone`: Proporciona compatibilidad con zonas horarias para el campo `last_activity`.
- `django.contrib.auth.models.AbstractUser`: Modelo base de usuario de Django.
- `django.db.models`: Usado para definir modelos personalizados.
"""


from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', null=True, blank=True)
    last_activity = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"[{self.pk}] {self.username} - {self.first_name}"
