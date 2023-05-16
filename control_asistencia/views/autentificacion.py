from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from ..utils.group_redirect import group_required
from django.contrib.auth.decorators import login_required

def inicioSesion (request):
    if request.method == "GET":
        return render(request, "control_asistencia/inicio_sesion.html")

    if request.method == "POST":
        username = request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.groups.filter(name = 'Grupo_DOCENTES').exists():
                return HttpResponseRedirect(reverse("control_asistencia:docente.index"))
            if user.groups.filter(name = "Grupo_ESTUDIANTES").exists():
                return HttpResponseRedirect(reverse("control_asistencia:estudiante.index"))
            if user.groups.filter(name = "Grupo_BEDELIAS").exists():
                return HttpResponseRedirect('/admin')
        else:
            return render(request,"control_asistencia/inicio_sesion.html",{
                "message":"Invalid Credentials"
            })
    
def cerrarSesion(request):
    logout(request)
    return HttpResponseRedirect(reverse("control_asistencia:inicioSesion"))

"""
Cerrarsesión
"""
@login_required
@group_required('Grupo_DOCENTES')
def cerrar_Sesion(request):
    user = request.user
    materias = user.materiasDocente.all()
    return render(request, "control_asistencia/cerrar_Sesion.html", {"usuario":user, "materias":materias})
