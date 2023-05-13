from django.urls import path
from .views import docente_views
from .views import estudiante_views
from .views import autentificacion

app_name = 'control_asistencia'

urlpatterns = [
    path("", autentificacion.inicioSesion, name="inicioSesion"),
    path("logout", autentificacion.cerrarSesion, name="cerrarSesion"),

    path("estudiante", estudiante_views.index, name="estudiante.index"),
    path("estudiante/<str:id>", estudiante_views.asistencias_de_materia, name="estudiante.asistencias_de_materia"),
    path("estudiante/marcar_asistencia/<str:id>", estudiante_views.marcar_asistencia, name="estudiante.marcar_asistencia"),

    path("docente", docente_views.index, name="docente.index"),
    path("docente/<int:id>/asistencias", docente_views.seleccionar_materia_fecha, name="docente.seleccionar_opcion"),
    path("docente/<int:id>/qr_asistencia", docente_views.qr_asistencia, name="docente.qr_asistencia"),
    path("docente/<int:id>/<str:fecha>", docente_views.asistencias_materia, name="docente.asistencias_materia"),
]