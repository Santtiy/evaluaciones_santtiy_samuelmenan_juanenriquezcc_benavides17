from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='usuarios:login')
def lista_calificaciones(request):
    """Vista temporal de calificaciones - será completada por el equipo de calificaciones"""
    context = {
        'message': 'Módulo de calificaciones en desarrollo',
    }
    return render(request, 'calificaciones/lista.html', context)

