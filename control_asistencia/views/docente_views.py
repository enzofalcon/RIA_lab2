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
    return render(request, "control_asistencia/docente/index.html")



"""
/docente/materias/:id

Listar fechas en las cuales cierta materia tiene asistencias
"""
def seleccionar_materia_fecha(request, id):
    return render(request, "control_asistencia/docente/seleccionar_materia_fecha.html", {"id":id})



"""
/docente/materias/:id/:fecha

Listas asistencias para cierta materia en cierta fecha
"""
def asistencias_materia(request, id, fecha):
    return render(request, "control_asistencia/docente/asistencias.html", {"id":id, "fecha":fecha})




"""
/docente/materias/:id/qr_asistencia

Generar QR para marcar asistencia en cierta materia en la fecha de hoy
"""
def qr_asistencia(request, id):
    return render(request, "control_asistencia/docente/qr_asistencia.html", {"id":id})
