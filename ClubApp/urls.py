from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('eventos/', views.eventos, name='eventos'),
    path('eventos/<int:evento_id>/', views.detalle_evento, name='detalle_evento'),
    path('organizadores/', views.organizadores, name='organizadores'),
    path('organizadores/<int:organizador_id>/', views.detalle_organizador, name='detalle_organizador'),
    path('actividades/', views.actividades, name='actividades'),
    path('actividades/<int:actividad_id>/', views.detalle_actividad, name='detalle_actividad'),
]