from django import forms 
from .forms import *

class HermanoForm(forms.Form):
    nombre = forms.CharField(label="Nombre Completo", max_length=50, required=True)
    edad = forms.IntegerField(label="Edad", required=True)
    fechanacimiento= forms.DateField(label= 'Fecha de Nacimiento', required=True)

class PadreForm(forms.Form):
    nombre = forms.CharField(label="Nombre Completo", max_length=50, required=True)
    edad = forms.IntegerField(label="Edad", required=True)
    fechanacimiento= forms.DateField(label= 'Fecha de Nacimiento', required=True)

class MadreForm(forms.Form):
    nombre = forms.CharField(label="Nombre Completo", max_length=50, required=True)
    edad = forms.IntegerField(label="Edad", required=True)
    fechanacimiento= forms.DateField(label= 'Fecha de Nacimiento', required=True)