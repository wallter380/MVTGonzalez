from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField()
    parentezco = models.CharField(max_length=40)
    dni = models.IntegerField()
