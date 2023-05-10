from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

from .models import Asistencia

def index(request):
    fechas = Asistencia.objects.order_by("fecha").values_list('fecha', flat=True).distinct()
    context = {"fechas": fechas}
    return render(request, "control_asistencia/index.html", context)

def asistencias_por_fecha(request, fecha):
    asistencias = Asistencia.objects.filter(fecha=fecha)
    context = {"fecha":fecha, "asistencias":asistencias}
    return render(request, "control_asistencia/asistencias_por_fecha.html", context)

def formulario_asistencia(request):
    context = {"fecha": timezone.now().strftime("%d/%m/%y")}
    return render(request, "control_asistencia/formulario_asistencia.html", context)

def marcar_asistencia(request):
    asistencia = Asistencia(nombre=request.POST["nombre"], fecha = timezone.now().strftime("%Y-%m-%d"), cedula = request.POST["cedula"])
    asistencia.save()
    return render(request, "control_asistencia/formulario_ok.html")