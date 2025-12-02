from django.contrib import admin
from .models import Evento, Actividad, Organizador, Inscripcion
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Evento)
admin.site.register(Actividad)
admin.site.register(Inscripcion)

class OrganizadorAdmin(UserAdmin):
    model = Organizador
    list_display = ('username', 'email', 'is_staff', 'foto_perfil', 'dni')

admin.site.register(Organizador, OrganizadorAdmin)