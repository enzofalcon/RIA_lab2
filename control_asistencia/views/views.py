from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

def inicioSesion (request):
    return render(request, "control_asistencia/inicio_sesion.html")