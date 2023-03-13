from django.db import models


class Cartera(models.Model):
    color= models.CharField(max_length=30)
    material= models.CharField(max_length=30)
    precio=models.IntegerField()
    capacidad = models.IntegerField()
    
    def __str__(self):
        return f"Cartera de: {self.material} - color: {self.color} - capacidad: {self.capacidad}"
    
class Maquillaje(models.Model):
    tipo= models.CharField(max_length=30)
    color= models.CharField(max_length=30)
    tamanio= models.CharField(max_length=30)
    precio=models.IntegerField()
    water_proof = models.BooleanField()

    def __str__(self):
        return f"Maquillaje: {self.tipo} - color: {self.color} - talle: {self.tamanio} - waterproof: {self.water_proof}"

class Ropa(models.Model):
    tipo= models.CharField(max_length=30)
    color= models.CharField(max_length=30)
    talle= models.CharField(max_length=30)
    precio=models.IntegerField()

    def __str__(self):
        return f"Ropa: {self.tipo} - color: {self.color} - talle: {self.talle}"