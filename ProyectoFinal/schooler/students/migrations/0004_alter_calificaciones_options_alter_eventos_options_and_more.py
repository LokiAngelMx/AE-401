# Generated by Django 4.2.7 on 2023-11-30 04:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("students", "0003_estudiante_profesores_alter_student_joined_date_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="calificaciones",
            options={"verbose_name_plural": "Calificaciones"},
        ),
        migrations.AlterModelOptions(
            name="eventos",
            options={"verbose_name_plural": "Eventos"},
        ),
        migrations.AlterModelOptions(
            name="inscripciones",
            options={"verbose_name_plural": "Inscripciones"},
        ),
        migrations.AlterModelOptions(
            name="materias",
            options={"verbose_name_plural": "Materias"},
        ),
        migrations.AlterModelOptions(
            name="profesores",
            options={"verbose_name_plural": "Profesores"},
        ),
    ]
