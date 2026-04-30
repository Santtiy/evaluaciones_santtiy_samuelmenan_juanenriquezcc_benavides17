from django.contrib.auth.decorators import user_passes_test, login_required
from functools import wraps


def es_profesor_o_admin(user):
    """Verifica si el usuario es Profesor o Administrador."""
    return user.groups.filter(
        name__in=['Profesor', 'Administrador']
    ).exists()


def es_admin(user):
    """Verifica si el usuario es Administrador."""
    return user.groups.filter(name='Administrador').exists()


def es_estudiante(user):
    """Verifica si el usuario es Estudiante."""
    return user.groups.filter(name='Estudiante').exists()


def profesor_o_admin_requerido(view_func):
    """
    Decorador que requiere que el usuario sea Profesor o Administrador.
    
    Uso:
        @profesor_o_admin_requerido
        def mi_vista(request):
            pass
    """
    @login_required
    @user_passes_test(es_profesor_o_admin)
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        return view_func(request, *args, **kwargs)
    return wrapper


def admin_requerido(view_func):
    """
    Decorador que requiere que el usuario sea Administrador.
    
    Uso:
        @admin_requerido
        def mi_vista(request):
            pass
    """
    @login_required
    @user_passes_test(es_admin)
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        return view_func(request, *args, **kwargs)
    return wrapper


def estudiante_requerido(view_func):
    """
    Decorador que requiere que el usuario sea Estudiante.
    
    Uso:
        @estudiante_requerido
        def mi_vista(request):
            pass
    """
    @login_required
    @user_passes_test(es_estudiante)
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        return view_func(request, *args, **kwargs)
    return wrapper
