from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from ..utils.group_redirect import group_required

"""
/docente

Index del docente.

Lista de materias del docente.
Navega a visualización de asistencias.
Navega a marcar asistencia.
"""
@login_required
@group_required('Docente')
def index(request):
    return render(request, "control_asistencia/docente/index.html")



"""
/docente/materias/:id

Listar fechas en las cuales cierta materia tiene asistencias
"""
@login_required
def seleccionar_materia_fecha(request, id):
    return render(request, "control_asistencia/docente/seleccionar_materia_fecha.html", {"id":id})



"""
/docente/materias/:id/:fecha

Listas asistencias para cierta materia en cierta fecha
"""
@login_required
def asistencias_materia(request, id, fecha):
    return render(request, "control_asistencia/docente/asistencias.html", {"id":id, "fecha":fecha})




"""
/docente/materias/:id/qr_asistencia

Generar QR para marcar asistencia en cierta materia en la fecha de hoy
"""
@login_required
def qr_asistencia(request, id):
    return render(request, "control_asistencia/docente/qr_asistencia.html", {"id":id})
