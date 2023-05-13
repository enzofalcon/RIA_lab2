from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from ..utils.group_redirect import group_required
from ..models import Asistencia, Materia

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
    return render(request, "control_asistencia/estudiante/marcar_asistencia.html", {"id":id})
