#from django.http import HttpResponse

# Create your views here.
#def inicio(request):
#    return HttpResponse("Agenda de eventos: ¡la app funciona!")
from django.shortcuts import render

def inicio(request):
    contexto = {
        "titulo": "Próximos eventos",
        "subtitulo": "Lo que pasa en tu ciudad, en un solo lugar.",
    }
    return render(request, "eventos/inicio.html", contexto)

def acerca(request):
    return render(request, "eventos/acerca.html")