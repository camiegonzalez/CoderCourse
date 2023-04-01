# ProyectoCoder

## Update database

* Al ingresar por primera vez, por las dudas, parado en la carpeta root, correr los siguientes comandos:

```Python
python manage.py make migrations

python manage.py make migrate

```

## Run Server
* Para correr el server, parado en el root, correr el comando:

```Python
python manage.py runserver
```

* El proyecto iniciara en la ruta http://127.0.0.1:8000/, siempre y cuando este disponible el puerto 8000.
* Al iniciar, en la ruta mencionada, usted vera el home de la pagina.

## Navigate the Page

* Sin loguearse en el sistema, usted podra acceder solo a la seccion de About, en donde encontrara informacion de la creadora de la pagina.
* En la parte superior derecha de la pantalla, tendra la opcion de ingresar, para logearse, y registrarse, en caso de no tener un usuario.
* Una vez logeado en el sistema, podra acceder a todas las secciones.

### Blogs

* En esta seccion, usted vera todos los blogs que estan creados en la base de datos. Tendra la posibilidad de crear nuevos blogs, editar los existentes, eliminarlos y ver los detalles de los mismos.

### Editar Perfil

* Usted podra editar los datos de su perfil

### Logout

* Uste podra deslogearse de la app

### Ver Perfil
* Usted podra ver informacion de su perfil

### Messages

* Usted dispondra de un chat en donde podra dejar mensajes y leer los mensajes hechos por otros usuarios.


## Super Usuario / Usuario Administrador

* Usted podra ver el panel de administrador del sitio si ingresa a la ruta /admin.
* Para poder hacer esto, debe crearse primero un super usuario.
* Para ello debe correr el siguiente script

```Python
python manage.py createsuperuser
```

* Le sera solicitado ingresar nombre de usuario, email, y contraseña para el nuevo super usuario. Luego debe apretar enter.
