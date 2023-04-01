from django.utils import timezone

from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
import os
from django.dispatch import receiver
from django.db.models.signals import post_delete
from django.conf import settings

class Blog(models.Model):
    titulo= models.CharField(max_length=30)
    subtitulo= models.CharField(max_length=30)
    cuerpo=models.CharField(max_length=300)
    autor = models.CharField(max_length=30)
    fecha = models.DateTimeField(default=timezone.now, blank=True)
    imagen = models.ImageField(upload_to='blogs', null=True, blank = True)
    
    def __str__(self):
        return f"Blog {self.titulo} de {self.autor} con fecha {self.fecha}"
    
    def delete(self, *args, **kwargs):
        # Call the parent method to delete the object
        super().delete(*args, **kwargs)
        
        # Esto es para eliminar la imagen cuando elimino el blog
        if self.imagen:
            path = os.path.join(settings.MEDIA_ROOT, self.imagen.name)
            if os.path.exists(path):
                os.remove(path)

# Connect a signal to the post_delete event to delete the image file after the object is deleted
@receiver(post_delete, sender=Blog)
def delete_image(sender, instance, **kwargs):
    if instance.imagen:
        path = os.path.join(settings.MEDIA_ROOT, instance.imagen.name)
        if os.path.exists(path):
            os.remove(path)

class Avatar(models.Model):
   
    user = models.ForeignKey(User, on_delete=models.CASCADE, max_length=100)
    
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
 
    def __str__(self):
        return f"{self.user} - {self.imagen}"


class Message(models.Model):
    user = models.CharField(max_length=30)
    dateTime = models.DateTimeField(default=timezone.now, blank=True)
    message = models.CharField(max_length=200)
