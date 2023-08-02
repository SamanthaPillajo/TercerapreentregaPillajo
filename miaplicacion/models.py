from django.db import models


class Padre(models.Model):

    nombreapellido = models.CharField(max_length=50)

    edad = models.IntegerField()

    fechanacimiento = models.DateField()

 

class Madre(models.Model):

    nombreapellido = models.CharField(max_length=50)

    edad = models.IntegerField()

    fechanacimiento = models.DateField()
    

 

class Hermana(models.Model):

    nombreapellido = models.CharField(max_length=50)

    edad = models.IntegerField()

    fechanacimiento = models.DateField()

   

 

