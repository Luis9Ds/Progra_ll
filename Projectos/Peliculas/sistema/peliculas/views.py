from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def nosotros(request):
    return render(request, "paginas/nosotros.html")

def inicio(request):
    return render(request, "paginas/inicio.html")

def peliculas(request):
    return render(request, "peliculas/index.html")
