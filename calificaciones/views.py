from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from .models import Calificacion
from .forms import CalificacionForm


@login_required
def listar(request):
	calificaciones = Calificacion.objects.all()
	return render(request, 'calificaciones/listar.html', {'calificaciones': calificaciones})


@login_required
def crear(request):
	form = CalificacionForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('listar')
	return render(request, 'calificaciones/crear.html', {'form': form})


@login_required
def editar(request, pk):
	obj = get_object_or_404(Calificacion, pk=pk)
	form = CalificacionForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
		return redirect('listar')
	return render(request, 'calificaciones/editar.html', {'form': form})


@login_required
def eliminar(request, pk):
	obj = get_object_or_404(Calificacion, pk=pk)
	if request.method == 'POST':
		obj.delete()
		return redirect('listar')
	return render(request, 'calificaciones/eliminar.html', {'obj': obj})


@login_required
def promedio_general(request):
	resultado = Calificacion.objects.all().aggregate(Avg('promedio'))
	promedio = resultado.get('promedio__avg')
	return render(request, 'calificaciones/promedio_general.html', {'promedio_general': promedio})
