from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone


"""
/estudiante

Index del estudiante.

Listar materias del estudiante.
"""
def index(request):
    return render(request, "control_asistencia/estudiante/index.html")



"""
/estudiante/materias/:id

Dada una materia, ver las asistencias del estudiante.
"""
def asistencias_de_materia(request, id):
    return render(request, "control_asistencia/estudiante/asistencias.html", {"id":id})


"""
/estudiante/marcar_asistencia/:id

Dado un link, introducir asistencia
"""
def marcar_asistencia(request, id):
    return render(request, "control_asistencia/estudiante/marcar_asistencia.html", {"id":id})
