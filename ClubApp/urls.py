from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('eventos/', views.eventos, name='eventos'),
    path('eventos/<int:evento_id>/', views.evento_actividades, name='evento_actividades'),
    path('organizadores/', views.organizadores, name='organizadores'),
    path('organizadores/<int:organizador_id>/', views.organizador_eventos, name='organizador_eventos'),
    path('actividades/', views.actividades, name='actividades'),
    path('actividades/<int:actividad_id>/', views.detalle_actividad, name='detalle_actividad'),
    path('contacto/', views.contacto, name='contacto'),
]