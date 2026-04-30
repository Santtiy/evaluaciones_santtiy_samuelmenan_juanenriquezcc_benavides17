from django.urls import path
from . import views

app_name = 'calificaciones'

urlpatterns = [
    path('', views.listar, name='listar'),
    path('crear/', views.crear, name='crear'),
    path('editar/<int:pk>/', views.editar, name='editar'),
    path('eliminar/<int:pk>/', views.eliminar, name='eliminar'),
    path('promedio/', views.promedio_general, name='promedio_general'),
]
