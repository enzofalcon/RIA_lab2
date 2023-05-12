from django.shortcuts import redirect
from django.urls import reverse

def group_required(group_name):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if request.user.groups.filter(name=group_name).exists():
                return view_func(request, *args, **kwargs)
            else:
                if request.user.group.filter(name='Docente').exists():
                    return redirect(reverse('control_asistencia:docente.index'))
                if request.user.group.filter(name='Estudiante').exist():
                    return redirect(reverse('control_asistencia:estudiante.index'));
            return redirect('/admin')
        return wrapper
    return decorator