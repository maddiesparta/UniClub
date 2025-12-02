from django.urls import path
from . import views
from django.views.generic import ListView

urlpatterns = [
    path('', views.index, name='index'),
    path('eventos/', views.EventosListView.as_view(), name='eventos'),
    path('eventos/<int:evento_id>/', views.ActividadesEventoListView.as_view(), name='evento_actividades'),
    path('organizadores/', views.OrganizadoresListView.as_view(), name='organizadores'),
    path('organizadores/<int:organizador_id>/', views.EventosOrganizadorListView.as_view(), name='organizador_eventos'),
    path('actividades/', views.ActividadesListView.as_view(), name='actividades'),
    path('actividades/<int:pk>/', views.ActividadDetailView.as_view(), name='detalle_actividad'),
    path('inscripcion/<int:evento_id>', views.inscripcionForm, name='inscripcion'),
]