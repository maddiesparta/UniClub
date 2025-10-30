from django.contrib import admin
from .models import Evento, Actividad, Organizador

# Register your models here.
admin.site.register(Evento)
admin.site.register(Actividad)
admin.site.register(Organizador)
