from django.db import models
from django.utils.crypto import get_random_string


class Cartera(models.Model):
    color= models.CharField(max_length=30)
    material= models.CharField(max_length=30)
    precio=models.IntegerField()
    capacidad = models.IntegerField()
    nombre= models.CharField(max_length=30, default="")
    code= models.CharField(max_length=30, default=get_random_string(30).lower(), unique=True)
    
    
    def __str__(self):
        return f"Cartera de: {self.material} - color: {self.color} - capacidad: {self.capacidad}"
    
class Maquillaje(models.Model):
    tipo= models.CharField(max_length=30)
    color= models.CharField(max_length=30)
    tamanio= models.CharField(max_length=30)
    precio=models.IntegerField()
    water_proof = models.BooleanField()
    nombre= models.CharField(max_length=30, default=get_random_string(30).lower())

    def __str__(self):
        return f"Maquillaje: {self.tipo} - color: {self.color} - talle: {self.tamanio} - waterproof: {self.water_proof}"

class Ropa(models.Model):
    tipo= models.CharField(max_length=30)
    color= models.CharField(max_length=30)
    talle= models.CharField(max_length=30)
    precio=models.IntegerField()
    nombre= models.CharField(max_length=30, default=get_random_string(30).lower())

    def __str__(self):
        return f"Ropa: {self.tipo} - color: {self.color} - talle: {self.talle}"