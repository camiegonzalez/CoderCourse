# Generated by Django 4.1.7 on 2023-03-13 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_alter_avatar_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ropa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=30)),
                ('talle', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
            ],
        ),
    ]
