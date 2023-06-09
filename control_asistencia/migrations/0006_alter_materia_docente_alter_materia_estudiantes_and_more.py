# Generated by Django 4.2 on 2023-05-12 00:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('control_asistencia', '0005_remove_estudiante_groups_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia',
            name='docente',
            field=models.ForeignKey(limit_choices_to={'groups__name': 'Grupo_DOCENTES'}, on_delete=django.db.models.deletion.CASCADE, related_name='materiasDocente', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='materia',
            name='estudiantes',
            field=models.ManyToManyField(limit_choices_to={'groups__name': 'Grupo_ESTUDIANTES'}, related_name='materiasEstudiante', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='materia',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asistenciasEstudiante', to=settings.AUTH_USER_MODEL)),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asistenciasMateria', to='control_asistencia.materia')),
            ],
        ),
    ]
