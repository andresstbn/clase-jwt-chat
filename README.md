# clase-jwt-chat

Base para la demo de JWT de Programación Web: un chat por canales con Django REST Framework en `backend/` y React en `frontend/`.

Leer canales y mensajes no pide login. Crear canales y enviar, editar o borrar mensajes sí. El formulario de `/login` está sin conectar: eso se hace en clase.

## Backend

Necesitas Python 3.13.

```bash
cd backend
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py cargar_datos
python manage.py runserver
```

Queda en http://localhost:8000. La documentación de la API está en http://localhost:8000/api/docs/.

Puedes volver a correr `cargar_datos` cuando quieras dejar los canales de prueba como al principio.

## Frontend

En otra terminal:

```bash
cd frontend
npm install
npm run dev
```

Queda en http://localhost:5173. La URL del backend sale de `VITE_API_URL`, en `frontend/.env`.

## Usuarios de prueba

| Usuario | Contraseña       |                                  |
| ------- | ---------------- | -------------------------------- |
| `ana`   | `clave-ana-123`  |                                  |
| `beto`  | `clave-beto-123` |                                  |
| `admin` | `admin123`       | superusuario, entra a `/admin/`  |

Para pedir un token:

```bash
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "ana", "password": "clave-ana-123"}'
```

## En Codespaces

El contenedor instala todo, migra y carga los datos al crearse. Solo tienes que levantar los dos servidores (`python manage.py runserver` y `npm run dev`) y, en la pestaña **Ports**, poner el puerto 8000 como **Public**: si queda privado, el navegador no puede llamar a la API desde el frontend.
