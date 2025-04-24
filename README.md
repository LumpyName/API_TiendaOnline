Tranqui lump, acá te dejo esa sección completa y mejorada para que puedas copiarla directo a tu `README.md`, incluyendo **los campos por defecto de Django** + **los que agregaste** tú en el modelo `Usuario`. Así quien vea tu proyecto va a entender bien qué datos maneja la API y cómo está estructurado tu modelo de usuarios.

---

## 🧱 Modelo de Usuario Personalizado

Este proyecto utiliza un modelo personalizado llamado `Usuario`, el cual **hereda de `AbstractUser`**.  
Esto significa que incluye **todos los campos por defecto** que Django proporciona para la autenticación, además de **campos personalizados**.

### 🧩 Campos por defecto incluidos por `AbstractUser`

| Campo             | Tipo              | Descripción                                  |
|------------------|-------------------|----------------------------------------------|
| `id`             | `AutoField`       | Identificador único (clave primaria).        |
| `username`       | `CharField`       | Nombre de usuario único.                     |
| `first_name`     | `CharField`       | Nombre del usuario.                          |
| `last_name`      | `CharField`       | Apellido del usuario.                        |
| `email`          | `EmailField`      | Correo electrónico.                          |
| `password`       | `CharField`       | Contraseña hasheada.                         |
| `is_staff`       | `BooleanField`    | Si puede acceder al admin de Django.         |
| `is_active`      | `BooleanField`    | Si la cuenta está activa.                    |
| `is_superuser`   | `BooleanField`    | Tiene todos los permisos.                    |
| `last_login`     | `DateTimeField`   | Última vez que inició sesión.                |
| `date_joined`    | `DateTimeField`   | Fecha en que se registró.                    |

### ✍️ Campos personalizados agregados

| Campo             | Tipo              | Descripción                                                                 |
|------------------|-------------------|-----------------------------------------------------------------------------|
| `foto_perfil`    | `ImageField`      | Imagen de perfil. Se guarda en la carpeta `media/fotos_perfil/`. Opcional. |
| `fecha_creacion` | `DateTimeField`   | Fecha de creación automática del usuario.                                   |
| `last_activity`  | `DateTimeField`   | Última actividad del usuario. Se inicia con la fecha actual por defecto.    |

---

## 🧪 Ejemplo de envío de imagen de perfil (`foto_perfil`)

Podés usar `Postman` o `curl` para enviar una imagen al campo `foto_perfil`. Asegurate de usar el método `PUT` con `multipart/form-data` y enviar el token en el header:

### 🔧 Headers:
```
Authorization: Token <TU_TOKEN>
Content-Type: multipart/form-data
```

### 🔧 Body (en Postman):
- **Key**: `foto_perfil`
- **Type**: File
- **Value**: (Seleccioná una imagen)
- También podés enviar otros campos como `first_name`, `last_name`, etc.

---

## 🗃️ Sobre la Base de Datos

Actualmente, el proyecto **no usa una base de datos profesional como PostgreSQL o MySQL**.  
En su lugar, se utiliza **SQLite**, que viene por defecto con Django.

### ⚙️ ¿Por qué usar SQLite?

- Ideal para desarrollo y pruebas locales.
- No requiere instalación adicional.
- Simple de portar (es solo un archivo `.sqlite3`).

### ⚠️ Producción

Si querés llevar este proyecto a producción, se recomienda migrar a una base de datos más robusta como **PostgreSQL** para mayor rendimiento, escalabilidad y seguridad.

---

¿Querés que te prepare un ejemplo con `curl` también?