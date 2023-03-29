# Generated by Django 4.1.7 on 2023-03-29 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0009_alter_cartera_nombre_alter_maquillaje_nombre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartera',
            name='code',
            field=models.CharField(default='4274fuldud8ztm0fgx3kedyxwmzqil', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='cartera',
            name='nombre',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='maquillaje',
            name='nombre',
            field=models.CharField(default='ejfwztxw0r0zzhmsljz4tw4tlnzhil', max_length=30),
        ),
        migrations.AlterField(
            model_name='ropa',
            name='nombre',
            field=models.CharField(default='hc4o3e71jmhcmug5mlfhh5mxf5ajaa', max_length=30),
        ),
    ]