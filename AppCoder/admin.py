from django.contrib import admin
from  .models import * #importamos el archivo models

# Register your models here.
#registramos los modelos

admin.site.register(Avatar)
admin.site.register(Message)
admin.site.register(Blog)


