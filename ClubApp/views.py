from django.shortcuts import render, get_object_or_404
from .models import Evento, Actividad, Organizador

# Create your views here.

def index(request):
    return render(request, 'index.html')

def eventos(request):
    eventos = Evento.objects.all()
    context = {'eventos': eventos}
    return render(request, 'eventos.html', context)

def detalle_evento(request, evento_id):
    actividades = Actividad.objects.all()
    context = {'actividades': actividades,
               'evento_id': evento_id}
    return render(request, 'lista_actividades.html', context)
