from django.contrib import admin
from  .models import * #importamos el archivo models

# Register your models here.
#registramos los modelos

admin.site.register(Ropa)
admin.site.register(Maquillaje)
admin.site.register(Cartera)


