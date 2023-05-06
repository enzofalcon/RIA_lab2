from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("asistencias_por_fecha/<str:fecha>",views.asistencias_por_fecha, name="asistencias_por_fecha"),
    path("formulario_asistencia", views.formulario_asistencia, name="formulario_asistencia"),
    path("marcar_asistencia", views.marcar_asistencia, name="marcar_asistencia")
]