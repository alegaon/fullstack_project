from django.http import HttpResponse

def index(request):
    return HttpResponse("¡Hola, mundo!")

def acerca_de(request):
    return HttpResponse("¡Curso de Python y Django!")