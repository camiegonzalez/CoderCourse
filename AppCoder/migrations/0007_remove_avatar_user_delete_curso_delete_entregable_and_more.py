# Generated by Django 4.1.7 on 2023-03-13 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0006_cartera'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avatar',
            name='user',
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Entregable',
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
        migrations.DeleteModel(
            name='Avatar',
        ),
    ]
