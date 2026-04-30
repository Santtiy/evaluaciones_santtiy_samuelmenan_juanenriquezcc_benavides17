# Evaluaciones Santtiy Samuelmenan Juanenriquezcc Benavides17

Proyecto Django para gestión de evaluaciones, autenticación y recuperación de contraseña.

## Requisitos

- Python 3.10 o superior
- Django instalado en un entorno virtual

## Instalación

```bash
python -m venv venv
source venv/Scripts/activate
pip install django
```

## Ejecutar el proyecto

```bash
python manage.py migrate
python manage.py runserver
```

Abre el proyecto en `http://127.0.0.1:8000/`.

## Recuperación de contraseña

- La ruta de inicio de sesión está en `/usuarios/login/`.
- La ruta de recuperación está en `/usuarios/password-reset/`.
- En desarrollo, el correo se imprime en la consola gracias a `EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'`.

## Estructura principal

- `evaluaciones_proyecto/` configuración general de Django
- `usuarios/` autenticación y recuperación de contraseña
- `calificaciones/` módulo académico
- `templates/` vistas HTML compartidas

## Notas

- El entorno virtual `venv/` no debe subirse a GitHub.
- El merge final a `develop` no se realiza desde esta tarea.