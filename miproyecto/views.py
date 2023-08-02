from django.http import HttpResponse
from django.template import Template, Context, loader
import datetime
from miaplicacion.models import Hermana, Madre, Padre

def saludoinicial(request, nombre):
    saludo = f'Bienvenido {nombre}!'
    return HttpResponse(saludo)

def pruebaTemplate(request):
    
    plantilla = loader.get_template('index.html')
    
    datos={
        'Bienvenida': 'Bienvenido/a a esta pagina web',
        'fechahoy': datetime.datetime.now(),
        
    }

   
    documento = plantilla.render(datos)
    return HttpResponse(documento)

def hermana(self):
     hermana = Hermana(nombreapellido= 'Sofia Pillajo', edad=25, fechanacimiento= '1997-10-26')
     hermana.save()
     texto= f'Nombre: {hermana.nombreapellido} Edad:{hermana.edad} Fecha de nacimiento: {hermana.fechanacimiento}'
     return HttpResponse(texto)

def padre(self):
     padre = Padre(nombreapellido= 'Mauricio Pillajo', edad=49, fechanacimiento= '1974-07-18')
     padre.save()
     texto= f'Nombre: {padre.nombreapellido} Edad:{padre.edad} Fecha de nacimiento: {padre.fechanacimiento}'
     return HttpResponse(texto)

def madre(self):
     madre = Madre(nombreapellido= 'Consuelo Conchambay', edad=53, fechanacimiento= '1969-12-13')
     madre.save()
     texto= f'Nombre: {madre.nombreapellido} Edad:{madre.edad} Fecha de nacimiento: {madre.fechanacimiento}'
     return HttpResponse(texto)