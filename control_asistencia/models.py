from django.db import models
from django.contrib.auth.models import AbstractUser, Group, User
import uuid

class Materia(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    nombre = models.CharField(max_length=255)
    icono = models.CharField(max_length=255)

    docente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='materiasDocente', limit_choices_to={'groups__name': 'Grupo_DOCENTES'})
    estudiantes = models.ManyToManyField(User, related_name='materiasEstudiante',limit_choices_to={'groups__name': 'Grupo_ESTUDIANTES'})
    
    def __str__(self):
        return self.nombre

class Asistencia(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    fecha = models.DateField()
    estudiante = models.ForeignKey(User, on_delete=models.CASCADE, related_name='asistenciasEstudiante')
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='asistenciasMateria')

    def __str__(self):
        return self.fecha.strftime(format="%Y-%m-%d") + " - " + self.materia.nombre + " - " + self.estudiante.username

class QR(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    fecha = models.DateField()
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='qrs')

