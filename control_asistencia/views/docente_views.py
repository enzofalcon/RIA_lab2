from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone


"""
/docente

Index del docente.

Lista de materias del docente.
Navega a visualización de asistencias.
Navega a marcar asistencia.
"""
def index(request):
    return ""



"""
/docente/materias/:id

Listar fechas en las cuales cierta materia tiene asistencias
"""
def seleccionar_materia_fecha(request):
    return ""



"""
/docente/materias/:id/:fecha

Listas asistencias para cierta materia en cierta fecha
"""
def asistencias_materia(request):
    return ""



"""
/docente/materias/:id/marcar_asistencia

Generar QR para marcar asistencia en cierta materia en la fecha de hoy
"""
def marcar_asistencia(request):
    return ""