from django.urls import path, include
from .views import *

urlpatterns = [
    path('',index, name='inicio'),
    path('madre/', madre, name = 'madre'),
    path('hermanos/', hermanos, name = 'hermanos'),
    path('padre/', padre, name = 'padre'),

    
    path('hermanos_form2/', HermanosForm2, name="hermanos_form2"),
    path('padre_form2/', PadreForm2, name="padre_form2"),
    path('madre_form2/', MadreForm2, name="madre_form2"),


    path('buscar_hermano/', buscarHermano, name="buscar_hermano"),
    path('buscar2/', buscar2, name="buscar2"),


]