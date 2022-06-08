from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("acerca-de", views.acerca_de, name="acerca_de")
]