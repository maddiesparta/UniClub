from django.shortcuts import render, get_object_or_404
from .models import Evento, Actividad, Organizador
from datetime import date, datetime
from django.views.generic import ListView
from django.views.generic import DetailView

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

class EventosListView(ListView):
    model = Evento
    template_name = "eventos/eventos.html"
    context_object_name = "eventos"

class ActividadesListView(ListView):
    model = Actividad
    template_name = "actividades/actividades.html"
    context_object_name = "actividades"

class ActividadesEventoListView(ListView):
        model = Actividad
        context_object_name = "actividades"
        template_name = "eventos/evento_actividades.html"

        def get_context_data(self, **kwargs):
            # Cargar el contexto base
            context = super().get_context_data(**kwargs)
            evento_id = self.kwargs['evento_id']
            # Añadir un listado de departamentos
            context['evento'] = get_object_or_404(Organizador, id=evento_id)
            return context

class OrganizadoresListView(ListView):
    model = Organizador
    template_name = "organizadores/organizadores.html"
    context_object_name = "organizadores"

class EventosOrganizadorListView(ListView):
        model = Evento
        context_object_name = "eventos"
        template_name = "organizadores/organizador_eventos.html"

        def get_context_data(self, **kwargs):
            # Cargar el contexto base
            context = super().get_context_data(**kwargs)
            organizador_id = self.kwargs['organizador_id']
            # Añadir un listado de departamentos
            context['organizador'] = get_object_or_404(Organizador, id=organizador_id)
            return context

class ActividadDetailView(DetailView):
    model = Actividad
    template_name = "actividades/detalle_actividad.html"
    
def contacto(request):
    return render(request, 'contacto/contacto.html')