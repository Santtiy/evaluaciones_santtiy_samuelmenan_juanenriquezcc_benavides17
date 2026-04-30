from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


@receiver(post_migrate)
def crear_grupos_y_permisos(sender, **kwargs):
    """
    Signal que se ejecuta después de las migraciones para crear grupos y asignar permisos.
    """
    if sender.name == 'usuarios':
        # Crear grupos
        admin_group, _ = Group.objects.get_or_create(name='Administrador')
        profesor_group, _ = Group.objects.get_or_create(name='Profesor')
        estudiante_group, _ = Group.objects.get_or_create(name='Estudiante')
        
        # Obtener permisos de calificaciones (si existen)
        try:
            from calificaciones.models import Calificacion
            calificacion_ct = ContentType.objects.get_for_model(Calificacion)
            
            # Permisos disponibles
            permisos_disponibles = Permission.objects.filter(
                content_type=calificacion_ct
            )
            
            if permisos_disponibles.exists():
                # Mapear permisos
                crear_perm = Permission.objects.filter(
                    content_type=calificacion_ct,
                    codename='add_calificacion'
                ).first()
                ver_perm = Permission.objects.filter(
                    content_type=calificacion_ct,
                    codename='view_calificacion'
                ).first()
                editar_perm = Permission.objects.filter(
                    content_type=calificacion_ct,
                    codename='change_calificacion'
                ).first()
                eliminar_perm = Permission.objects.filter(
                    content_type=calificacion_ct,
                    codename='delete_calificacion'
                ).first()
                
                permisos_admin = []
                permisos_profesor = []
                permisos_estudiante = []
                
                if crear_perm:
                    permisos_admin.append(crear_perm)
                    permisos_profesor.append(crear_perm)
                
                if ver_perm:
                    permisos_admin.append(ver_perm)
                    permisos_profesor.append(ver_perm)
                    permisos_estudiante.append(ver_perm)
                
                if editar_perm:
                    permisos_admin.append(editar_perm)
                    permisos_profesor.append(editar_perm)
                
                if eliminar_perm:
                    permisos_admin.append(eliminar_perm)
                
                # Asignar permisos a grupos
                admin_group.permissions.set(permisos_admin)
                profesor_group.permissions.set(permisos_profesor)
                estudiante_group.permissions.set(permisos_estudiante)
                
        except Exception:
            # Si Calificacion no existe aún, continuar sin error
            pass
