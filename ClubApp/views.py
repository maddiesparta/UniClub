from django.shortcuts import render, get_object_or_404
from .models import Evento, Actividad, Organizador

# Create your views here.

def index(request):
    return render(request, 'index.html')

def eventos(request):
    eventos = Evento.objects.all()
    context = {'eventos': eventos}
    return render(request, 'eventos.html', context)

def actividades(request):
    actividades=Actividad.objects.all()
    context={'actividades': actividades}
    return render(request, 'actividades.html', context)

def detalle_evento(request, evento_id):
    actividades = Actividad.objects.all()
    context = {'actividades': actividades,
               'evento_id': evento_id}
    return render(request, 'lista_actividades.html', context)

def organizadores(request):
    organizadores = Organizador.objects.all()
    context= {'organizadores': organizadores}
    return render(request,'organizadores.html', context)

def detalle_organizador(request, organizador_id):
    eventos = Evento.objects.all()
    context={'eventos':eventos,
             'organizador': get_object_or_404(Organizador, id=organizador_id)} 
    return render(request, 'lista_organizadores.html', context)

def detalle_actividad(request, actividad_id):
    actividad = get_object_or_404(Actividad, id = actividad_id)
    context = {'actividad' : actividad}
    return render(request,'detalle_actividad.html',context)
    

