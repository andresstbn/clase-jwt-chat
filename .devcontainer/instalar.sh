#!/usr/bin/env bash
set -e

cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py cargar_datos

cd ../frontend
npm install
# En un Codespace el backend no está en localhost sino en la URL pública del puerto 8000.
if [ -n "$CODESPACE_NAME" ]; then
  echo "VITE_API_URL=https://${CODESPACE_NAME}-8000.${GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN:-app.github.dev}" > .env.local
fi
