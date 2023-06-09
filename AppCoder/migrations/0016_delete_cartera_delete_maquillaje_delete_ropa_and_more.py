# Generated by Django 4.1.7 on 2023-03-31 04:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppCoder', '0015_blog_alter_cartera_code_alter_maquillaje_nombre_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cartera',
        ),
        migrations.DeleteModel(
            name='Maquillaje',
        ),
        migrations.DeleteModel(
            name='Ropa',
        ),
        migrations.AlterField(
            model_name='avatar',
            name='user',
            field=models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blog',
            name='fecha',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='message',
            name='dateTime',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
