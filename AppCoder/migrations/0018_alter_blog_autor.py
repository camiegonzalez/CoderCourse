# Generated by Django 4.1.7 on 2023-04-17 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0017_alter_blog_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='autor',
            field=models.CharField(max_length=300),
        ),
    ]
