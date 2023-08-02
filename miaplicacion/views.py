from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def index(request):
    return render(request,'miaplicacion/inicio.html')

def hermanos(request):
    return render(request,'miaplicacion/hermanos.html')

def madre(request):
    return render(request,'miaplicacion/madre.html')


def padre(request):
    return render(request,'miaplicacion/padre.html')


def HermanosForm2(request):
    if request.method == "POST":   
        miForm = HermanoForm(request.POST)
        if miForm.is_valid():
            hermanos_nombre = miForm.cleaned_data.get('nombre')
            hermanos_edad = miForm.cleaned_data.get('edad')
            hermanos_fechanacimiento = miForm.cleaned_data.get('fechanacimiento')
            hermanos = Hermana(nombreapellido=hermanos_nombre, edad=hermanos_edad, fechanacimiento=hermanos_fechanacimiento)
            hermanos.save()
            return render(request, "miaplicacion/hermanos.html")
    else:
        miForm = HermanoForm()

    return render(request, "miaplicacion/hermanos.html", {"form":miForm})

def PadreForm2(request):
    if request.method == "POST":   
        miForm = PadreForm(request.POST)
        if miForm.is_valid():
            padre_nombre = miForm.cleaned_data.get('nombre')
            padre_edad = miForm.cleaned_data.get('edad')
            padre_fechanacimiento = miForm.cleaned_data.get('fechanacimiento')
            padre = Padre(nombreapellido=padre_nombre, edad=padre_edad, fechanacimiento=padre_fechanacimiento)
            padre.save()
            return render(request, "miaplicacion/padre.html")
    else:
        miForm = PadreForm()

    return render(request, "miaplicacion/padre.html", {"form":miForm})


def MadreForm2(request):
    if request.method == "POST":   
        miForm = MadreForm(request.POST)
        if miForm.is_valid():
            madre_nombre = miForm.cleaned_data.get('nombre')
            madre_edad = miForm.cleaned_data.get('edad')
            madre_fechanacimiento = miForm.cleaned_data.get('fechanacimiento')
            madre = Madre(nombreapellido=madre_nombre, edad=madre_edad, fechanacimiento=madre_fechanacimiento)
            madre.save()
            return render(request, "miaplicacion/madre.html")
    else:
        miForm = MadreForm()

    return render(request, "miaplicacion/madre.html", {"form":miForm})


def buscarHermano(request):
    return render(request, "miaplicacion/buscarhermano.html")

def buscar2(request):
    if request.GET['nombre']:
        hermano = request.GET['nombre']
        hermana = Hermana.objects.filter(nombreapellido__icontains=hermano)
        return render(request,
                      "miaplicacion/resultadoshermano.html",
                      {'nombre': hermano, "hermanos": hermana})
    return HttpResponse("No se ingresaron datos para buscar!")




