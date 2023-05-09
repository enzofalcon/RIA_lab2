from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone


"""
/estudiante

Index del estudiante.

Listar materias del estudiante.
"""
def index(request):
    return ""



"""
/estudiante/materias/:id

Dada una materia, ver las asistencias del estudiante.
"""
def asistencias_de_materia(request):
    return ""


"""
/estudiante/marcar_asistencia/:id

Dado un link, introducir asistencia
"""
def marcarAsistencia(request):
    return ""
