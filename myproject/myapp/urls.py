from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("acerca-de", views.acerca_de, name="acerca_de"),
    path("cursos", views.cursos, name="cursos"),
    path("cotizacion-dolar", views.cotizacion_dolar, name="cotizacion_dolar"),
    path("aeropuertos", views.aeropuertos, name="aeropuertos"),
]