from django.db import models

class Familia(models.Model):
    nombre_completo = models.CharField(max_length=128)
    edad = models.IntegerField()
    fecha_de_nacimiento = models.DateField()
    

    
