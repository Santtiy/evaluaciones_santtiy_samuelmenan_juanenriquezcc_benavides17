from django.apps import AppConfig


class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usuarios'

    def ready(self):
        """
        Crear grupos de usuarios y asignar permisos cuando la app está lista.
        """
        from django.contrib.auth.models import Group, Permission
        from django.contrib.contenttypes.models import ContentType
        
        # Crear grupos
        admin_group, _ = Group.objects.get_or_create(name='Administrador')
        profesor_group, _ = Group.objects.get_or_create(name='Profesor')
        estudiante_group, _ = Group.objects.get_or_create(name='Estudiante')
        
        # Obtener permisos de calificaciones (si existen)
        try:
            from calificaciones.models import Calificacion
            calificacion_ct = ContentType.objects.get_for_model(Calificacion)
            
            # Permisos disponibles
            crear_perm = Permission.objects.get(
                content_type=calificacion_ct,
                codename='add_calificacion'
            )
            ver_perm = Permission.objects.get(
                content_type=calificacion_ct,
                codename='view_calificacion'
            )
            editar_perm = Permission.objects.get(
                content_type=calificacion_ct,
                codename='change_calificacion'
            )
            eliminar_perm = Permission.objects.get(
                content_type=calificacion_ct,
                codename='delete_calificacion'
            )
            
            # Permisos para Administrador (acceso total)
            admin_group.permissions.set([
                crear_perm, ver_perm, editar_perm, eliminar_perm
            ])
            
            # Permisos para Profesor (crear y editar)
            profesor_group.permissions.set([
                crear_perm, ver_perm, editar_perm
            ])
            
            # Permisos para Estudiante (solo ver)
            estudiante_group.permissions.set([ver_perm])
            
        except Exception:
            # Si Calificacion no existe aún, continuar sin error
            pass
