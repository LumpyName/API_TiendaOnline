---

# 🛡️ API de Autenticación

Esta API permite a los usuarios registrarse, iniciar sesión y modificar su información personal de forma segura usando tokens JWT.

---

## 📌 Características

- ✅ **Registro de usuarios**
- 🔐 **Autenticación JWT (access / refresh)**
- 💥 **Destruccion de tokens JWT**
- 🔄 **Modificación de datos del usuario autenticado**

---

## 🚀 Instalación

Clona el repositorio y configura el entorno:

```bash
git clone <URL_DEL_REPOSITORIO>
cd <nombre_del_proyecto>
pip install -r requirements.txt
```

Configura tu archivo `.env` si es necesario y ejecuta:

```bash
python manage.py migrate
python manage.py runserver
```

---

## 🔗 Endpoints

### 1️⃣ Registro de usuario

**URL:** `auth/register/`  
**Método:** `POST`  
**Descripción:** Crea un nuevo usuario.

**Body de la solicitud:**

```json
{
  "username": "usuario_ejemplo",
  "password": "contraseña_segura",
  "first_name": "Juan",
  "last_name": "Pérez",
  "email": "juan@example.com"
}
```
Los unicos campos obligatorios son "username" y "passowrd"

**Respuesta exitosa (200 OK):**

```json
{
  "mensaje": "Usuario creado correctamente"
}
```

---

### 2️⃣ Login (obtener tokens)

**URL:** `auth/login/`  
**Método:** `POST`  
**Descripción:** Autentica al usuario y devuelve tokens JWT.

**Body de la solicitud:**

```json
{
  "username": "usuario_ejemplo",
  "password": "contraseña_segura"
}
```

**Respuesta exitosa (200 OK):**

```json
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR...",
  "access": "eyJ0eXAiOiJKV1QiLCJh..."
}
```

---

### 3️⃣ Modificación de usuario

**URL:** `/crud/modify_user`  
**Método:** `PUT`  
**Descripción:** Permite modificar los datos del usuario autenticado.

**Body de la solicitud:**

```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJh...",
  "first_name": "NuevoNombre",
  "last_name": "NuevoApellido"
}
```
O el campo en el que esta, excepto el de la imagen (endpoint aun no creado)

**Respuesta exitosa (200 OK):**

```json
{
  "mensaje": "Modificaciones realizadas correctamente.",
  "modificaciones": {
    "first_name": "Se modificó exitosamente a 'NuevoNombre'",
    "last_name": "Se modificó exitosamente a 'NuevoApellido'"
  }
}
```

---
### 4️⃣ Cierre de sesión de usuario

**URL:** `/auth/revocar_token`  
**Método:** `POST`  
**Descripción:** Permite revocar un token de renovación (`refresh_token`), cerrando la sesión del usuario. Esto evita que el token sea reutilizado.

**Body de la solicitud:**

```json
{
  "refresh": "<refresh_token_string>"
}
```

**Respuesta exitosa (205 Reset Content):**

```json
{
  "mensaje": "Sesión cerrada correctamente. El token de renovación ha sido revocado."
}
```

**Respuesta de error (400 Bad Request):**

```json
{
  "error": "Token inválido o ya revocado. No se pudo cerrar sesión."
}
```

---
## 🧪 Cómo probar

Puedes usar herramientas como **Postman** o hacer pruebas con `curl` desde la terminal.

**Ejemplo con curl para login:**

```bash
curl -X POST http://localhost:8000/login/ \
     -H "Content-Type: application/json" \
     -d '{"username": "usuario_ejemplo", "password": "contraseña_segura"}'
```

---

# 🗄️ Base de Datos (BBDD) que usa la API Generado por Django

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
| `last_activity`  | `DateTimeField`   | Última actividad del usuario. Se inicia con la fecha actual por defecto.    |


## 🗃️ Sobre la Base de Datos

Actualmente, el proyecto **no usa una base de datos profesional como PostgreSQL o MySQL**.  
En su lugar, se utiliza **SQLite**, que viene por defecto con Django.

### ⚠️ Producción

Si querés llevar este proyecto a producción, se recomienda migrar a una base de datos más robusta como **PostgreSQL** para mayor rendimiento, escalabilidad y seguridad.


--- 

## 📷 ¿Se pueden enviar imágenes?

No. Para campos tipo imagen (como `foto_perfil`), se debe usar `multipart/form-data` y no `application/json`. Esto requiere un endpoint preparado para aceptar archivos (endpoint que no fue creado (aun)).

---

## 📖 Licencia

Este proyecto está bajo la licencia [MIT](https://opensource.org/licenses/MIT).

---
