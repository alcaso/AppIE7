from apps.alumna.models import Alumna
from django.shortcuts import render
from django.http import HttpResponse

#from .models import Question


# Create your views here.

def index(request):
    return HttpResponse("SISTEMA DE INFORMACION INSAJO")


def docente(request):
    grado = Alumna.objects.all
    datos = {
        'Lista Alumnas': grado,
    }
    return HttpResponse(render(request, "alumna.html",datos))


def estudiante(request):
    grado = Alumna.objects.all
    datos = {
        'Lista Alumnas': grado,
    }
    return HttpResponse(render(request, "estudiante.html",datos))