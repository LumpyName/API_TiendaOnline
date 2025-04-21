---

# 🛡️ API de Autenticación

Esta API permite a los usuarios registrarse, iniciar sesión y modificar su información personal de forma segura usando tokens JWT.

---

## 📌 Características

- ✅ **Registro de usuarios**
- 🔐 **Autenticación JWT (access / refresh)**
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

## 🧪 Cómo probar

Puedes usar herramientas como **Postman** o hacer pruebas con `curl` desde la terminal.

**Ejemplo con curl para login:**

```bash
curl -X POST http://localhost:8000/login/ \
     -H "Content-Type: application/json" \
     -d '{"username": "usuario_ejemplo", "password": "contraseña_segura"}'
```

---

## 📷 ¿Se pueden enviar imágenes?

No. Para campos tipo imagen (como `foto_perfil`), se debe usar `multipart/form-data` y no `application/json`. Esto requiere un endpoint preparado para aceptar archivos (endpoint que no fue creado (aun)).

---

## 📖 Licencia

Este proyecto está bajo la licencia [MIT](https://opensource.org/licenses/MIT).

---

¿Querés que también te lo prepare como `README.md` bien formateado para GitHub?
