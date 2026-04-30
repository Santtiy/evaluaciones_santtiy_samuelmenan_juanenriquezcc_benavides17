from django.contrib import admin
from .models import Calificacion


@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    list_display = ('nombre_estudiante', 'identificacion', 'asignatura', 'promedio')
    search_fields = ('nombre_estudiante', 'identificacion', 'asignatura')
from django.contrib import admin

# Register your models here.
