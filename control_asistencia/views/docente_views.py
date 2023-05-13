from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from ..utils.group_redirect import group_required
from ..models import Materia, Asistencia, QR

"""
/docente

Index del docente.

Lista de materias del docente.
Navega a visualización de asistencias.
Navega a marcar asistencia.
"""
@login_required
@group_required('Grupo_DOCENTES')
def index(request):
    materias = Materia.objects.filter(docente_id = request.user.id)
    return render(request, "control_asistencia/docente/index.html", {"materias":materias})



"""
/docente/materias/:id

Listar fechas en las cuales cierta materia tiene asistencias
"""
@login_required
@group_required('Grupo_DOCENTES')
def seleccionar_materia_fecha(request, id):
    materia = Materia.objects.filter(uid = id).first()
    fechas = Asistencia.objects.filter(materia_id = id).order_by("fecha").values_list('fecha', flat=True).distinct()
    return render(request, "control_asistencia/docente/seleccionar_materia_fecha.html", {"materia":materia, "fechas": fechas})



"""
/docente/materias/:id/:fecha

Listas asistencias para cierta materia en cierta fecha
"""
@login_required
@group_required('Grupo_DOCENTES')
def asistencias_materia(request, id, fecha):
    materia = Materia.objects.filter(uid = id).first()
    asistencias = Asistencia.objects.filter(materia_id = id, fecha=fecha)    
    return render(request, "control_asistencia/docente/asistencias.html", {"materia":materia, "fecha":fecha, "asistencias":asistencias})




"""
/docente/materias/:id/qr_asistencia

Generar QR para marcar asistencia en cierta materia en la fecha de hoy
"""
@login_required
@group_required('Grupo_DOCENTES')
def qr_asistencia(request, id):
    materia = Materia.objects.filter(uid=id).first()
    qr = QR(fecha = timezone.now().strftime("%Y-%m-%d"), materia_id = id)
    qr.save()
    return render(request, "control_asistencia/docente/qr_asistencia.html", {"materia":materia, "qr":qr})
