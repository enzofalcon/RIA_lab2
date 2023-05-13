from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from ..utils.group_redirect import group_required
from ..models import Asistencia, Materia,  QR

"""
/estudiante

Index del estudiante.

Listar materias del estudiante.
"""
@login_required
@group_required('Grupo_ESTUDIANTES')
def index(request):
    user = request.user
    materias = user.materiasEstudiante.all()
    return render(request, "control_asistencia/estudiante/index.html", {"usuario":user, "materias":materias})



"""
/estudiante/:id

Dada una materia, ver las asistencias del estudiante.
"""
@login_required
@group_required('Grupo_ESTUDIANTES')
def asistencias_de_materia(request, id):
    materia = Materia.objects.filter(uid=id).first()
    asistencias = Asistencia.objects.filter(estudiante_id=request.user.id, materia_id=materia.uid)
    return render(request, "control_asistencia/estudiante/asistencias.html", {"materia": materia, "asistencias":asistencias})


"""
/estudiante/:id

Dado un link, introducir asistencia
"""
@login_required
@group_required('Grupo_ESTUDIANTES')
def marcar_asistencia(request, id):
    qr = QR.objects.filter(uid = id).first()
    materia = qr.materia
    mensaje = None

    #Marcar asistencia solo si ya no existe una asistencia para esta fecha, materia y estudiante.
    if Asistencia.objects.filter(estudiante_id = request.user.id, materia_id = materia.uid, fecha = timezone.now().strftime("%Y-%m-%d")).exists():
        mensaje = 'Ya has registrado tu asistencia'
    else:
        Asistencia(fecha = timezone.now().strftime("%Y-%m-%d"), estudiante_id = request.user.id, materia_id = materia.uid).save()
        mensaje = 'Has registrado tu asistencia correctamente'

    return render(request, "control_asistencia/estudiante/marcar_asistencia.html", {"materia":materia, "mensaje":mensaje})
