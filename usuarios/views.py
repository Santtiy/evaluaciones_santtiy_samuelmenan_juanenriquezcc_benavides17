from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import RegistroForm


def home(request):
    """Vista de inicio - redirige a login si no está autenticado."""
    if request.user.is_authenticated:
        return render(request, 'home.html')
    return redirect('usuarios:login')


def registro(request):
    """Vista de registro de usuarios con asignación de roles."""
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            # Guardar usuario
            user = form.save()
            
            # Obtener rol seleccionado
            rol = form.cleaned_data.get('rol')
            
            # Crear o buscar el grupo
            grupo, _ = Group.objects.get_or_create(name=rol)
            
            # Asignar usuario al grupo
            user.groups.add(grupo)
            
            # Redirigir al login
            return redirect('usuarios:login')
    else:
        form = RegistroForm()

    return render(request, 'usuarios/registro.html', {'form': form})


# Funciones de validación para decoradores

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
