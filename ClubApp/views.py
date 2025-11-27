from django.shortcuts import render, get_object_or_404
from .models import Evento, Actividad, Organizador
from datetime import date, datetime

# Create your views here.

def index(request):
    eventos_ordenados = sorted(Evento.objects.all(), key=obtener_fecha)
    hoy = date.today()
    proximos = [
        e for e in eventos_ordenados
        if datetime.strptime(e.fecha, "%d/%m/%Y").date() >= hoy
    ]
    proximos3 = proximos[:3]
    return render(request, 'index.html', {"proximos_eventos":proximos3, "eventos": eventos_ordenados})

def obtener_fecha(evento):
    return datetime.strptime(evento.fecha, "%d/%m/%Y").date()

def eventos(request): 
    eventos = Evento.objects.all()
    context = {'eventos': eventos}
    return render(request, 'eventos/eventos.html', context)

def actividades(request):
    actividades=Actividad.objects.all()
    context={'actividades': actividades}
    return render(request, 'actividades/actividades.html', context)

def evento_actividades(request, evento_id):
    actividades = Actividad.objects.all()
    context = {'actividades': actividades, 'evento': get_object_or_404(Evento, id=evento_id)}
    return render(request, 'eventos/evento_actividades.html', context)

def organizadores(request):
    organizadores = Organizador.objects.all()
    context= {'organizadores': organizadores}
    return render(request,'organizadores/organizadores.html', context)

def organizador_eventos(request, organizador_id):
    eventos = Evento.objects.all()
    context={'eventos':eventos, 'organizador': get_object_or_404(Organizador, id=organizador_id)} 
    return render(request, 'organizadores/organizador_eventos.html', context)

def detalle_actividad(request, actividad_id):
    actividad = get_object_or_404(Actividad, id = actividad_id)
    context = {'actividad' : actividad}
    return render(request,'actividades/detalle_actividad.html',context)
    
def contacto(request):
    return render(request, 'contacto/contacto.html')