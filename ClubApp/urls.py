from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('eventos/', views.eventos, name='eventos'),
    path('eventos/<int:evento_id>/', views.detalle_evento, name='detalle_evento'),
]