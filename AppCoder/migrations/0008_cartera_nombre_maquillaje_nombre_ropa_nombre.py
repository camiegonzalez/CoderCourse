# Generated by Django 4.1.7 on 2023-03-29 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0007_remove_avatar_user_delete_curso_delete_entregable_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartera',
            name='nombre',
            field=models.CharField(default='spo5ab6ba3gwq95iziuugpb15ufwqa', max_length=30, unique=True),
        ),
        migrations.AddField(
            model_name='maquillaje',
            name='nombre',
            field=models.CharField(default='84wtruqigtzei0gfyfra6mtx287rkz', max_length=30),
        ),
        migrations.AddField(
            model_name='ropa',
            name='nombre',
            field=models.CharField(default='sxezq656f8rs4bqkxtfqwlfbxr5of5', max_length=30),
        ),
    ]
