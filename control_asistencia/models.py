from django.db import models

class Asistencia(models.Model):
    nombre = models.CharField(max_length=255)
    fecha = models.DateField("date published")
    cedula = models.CharField(max_length=8)

    def __str__(self):
        return self.fecha.strftime("%d/%m/%y") + " - " + self.cedula + " - " + self.nombre

