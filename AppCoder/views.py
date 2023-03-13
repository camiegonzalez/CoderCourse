from typing import List

from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Cartera, Maquillaje, Curso, Profesor, Avatar, Ropa
from AppCoder.forms import CarterasFormulario, RopaFormulario,MaquillajesFormulario, CursoFormulario, ProfesorFormulario, UserRegisterForm,UserEditForm,AvatarFormulario

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User


#Para la prueba unitaria
import string
import random


#Para el login

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

#Decorador por defecto
from django.contrib.auth.decorators import login_required

from django.views.generic.base import TemplateView







# Create your views here.

def curso(request):

      curso =  Curso(nombre="Desarrollo web", camada="19881")
      curso.save()
      documentoDeTexto = f"--->Curso: {curso.nombre}   Camada: {curso.camada}"


      return HttpResponse(documentoDeTexto)

@login_required
def inicio(request):

      avatares = Avatar.objects.filter(user=request.user.id)
      
      return render(request, "AppCoder/inicio.html")



def estudiantes(request):

      return render(request, "AppCoder/estudiantes.html")


def entregables(request):

      return render(request, "AppCoder/entregables.html")


def cursos(request):

      if request.method == 'POST':

            miFormulario = CursoFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  curso = Curso (nombre=informacion['curso'], camada=informacion['camada']) 

                  curso.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= CursoFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/cursos.html", {"miFormulario":miFormulario})




def profesores(request):

      if request.method == 'POST':

            miFormulario = ProfesorFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data
                  """
                  #CASO DE PRUEBA
                  KEY_LEN = 20
                  keylistNombre = [random.choice((string.ascii_letters + string.digits)) for i in range(KEY_LEN)]
                  nombrePrueba = "".join(keylistNombre)

                  print(f"---->Pueba con: {nombrePrueba} ")
                  """
                  profesor = Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email'], profesion=informacion['profesion']) 

                  profesor.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= ProfesorFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/profesores.html", {"miFormulario":miFormulario})






def buscar(request):

      if  request.GET["color"] and request.GET["material"]:
            color = request.GET['color'] 
            material = request.GET['material'] 
            carteras = Cartera.objects.filter(color__icontains=color, material__icontains=material)
            return render(request, "AppCoder/inicio.html", {"carteras":carteras, "color":color, "material": material})
      elif  request.GET["color"] and not request.GET["material"]:
            color = request.GET['color'] 
            carteras = Cartera.objects.filter(color__icontains=color)
            return render(request, "AppCoder/inicio.html", {"carteras":carteras, "color":color, "material": "todos"})
      elif  not request.GET["color"] and request.GET["material"]:
            material = request.GET['material'] 
            carteras = Cartera.objects.filter(material__icontains=material)
            return render(request, "AppCoder/inicio.html", {"carteras":carteras, "color":"todos", "material": material})

      else: 

	      respuesta = "No enviaste datos"

      #No olvidar from django.http import HttpResponse
      #return HttpResponse(respuesta)
      return render(request, "AppCoder/inicio.html", {"respuesta":respuesta})



def leerProfesores(request):

      profesores = Profesor.objects.all() #trae todos los profesores

      contexto= {"profesores":profesores} 

      return render(request, "AppCoder/leerProfesores.html",contexto)

def carteras(request):

      carteras = Cartera.objects.all()

      contexto= {"carteras":carteras} 

      return render(request, "AppCoder/leerCarteras.html",contexto)

def maquillaje(request):

      maquillajes = Maquillaje.objects.all()

      contexto= {"maquillajes":maquillajes} 

      return render(request, "AppCoder/leerMaquillaje.html",contexto)

def ropa(request):

      ropa = Ropa.objects.all()

      contexto= {"ropa":ropa} 

      return render(request, "AppCoder/leerRopa.html",contexto)



def agregarMaquillaje(request):

      if request.method == 'POST':

            miFormulario = MaquillajesFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  maquillajes = Maquillaje (tipo=informacion['tipo'], tamanio=informacion['tamanio'], color=informacion['color'], precio=informacion['precio'], water_proof=informacion['water_proof']) 

                  maquillajes.save()

                  maquillajesGuardados = Maquillaje.objects.all()

                  contexto= {"maquillajes":maquillajesGuardados} 

                  return render(request, "AppCoder/leerMaquillaje.html",contexto)

      else: 

            miFormulario= MaquillajesFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/maquillaje.html", {"miFormulario":miFormulario})

def agregarRopa(request):

      if request.method == 'POST':

            miFormulario = RopaFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  ropa = Ropa (tipo=informacion['tipo'], talle=informacion['talle'], color=informacion['color'], precio=informacion['precio']) 

                  ropa.save()


                  prendasGuardadas = Ropa.objects.all()

                  contexto= {"ropa":prendasGuardadas} 

                  return render(request, "AppCoder/leerRopa.html",contexto)

      else: 

            miFormulario= RopaFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/ropa.html", {"miFormulario":miFormulario})

def agregarCartera(request):

      if request.method == 'POST':

            miFormulario = CarterasFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  cartera = Cartera (material=informacion['material'], capacidad=informacion['capacidad'], color=informacion['color'], precio=informacion['precio']) 

                  cartera.save()

                  carterasGuardadas = Cartera.objects.all()

                  contexto= {"carteras":carterasGuardadas} 

                  return render(request, "AppCoder/leerCarteras.html",contexto)

      else: 

            miFormulario= CarterasFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/cartera.html", {"miFormulario":miFormulario})


def eliminarProfesor(request, profesor_nombre):

      profesor = Profesor.objects.get(nombre=profesor_nombre)
      profesor.delete()
      
      #vuelvo al menú
      profesores = Profesor.objects.all() #trae todos los profesores

      contexto= {"profesores":profesores} 

      return render(request, "AppCoder/leerProfesores.html",contexto)



def editarProfesor(request, profesor_nombre):

      #Recibe el nombre del profesor que vamos a modificar
      profesor = Profesor.objects.get(nombre=profesor_nombre)

      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':

            miFormulario = ProfesorFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  profesor.nombre = informacion['nombre']
                  profesor.apellido = informacion['apellido']
                  profesor.email = informacion['email']
                  profesor.profesion = informacion['profesion']

                  profesor.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= ProfesorFormulario(initial={'nombre': profesor.nombre, 'apellido':profesor.apellido , 
            'email':profesor.email, 'profesion':profesor.profesion}) 

      #Voy al html que me permite editar
      return render(request, "AppCoder/editarProfesor.html", {"miFormulario":miFormulario, "profesor_nombre":profesor_nombre})




class CursoList(ListView):

      model = Curso 
      template_name = "AppCoder/cursos_list.html"



class CursoDetalle(DetailView):

      model = Curso
      template_name = "AppCoder/curso_detalle.html"



class CursoCreacion(CreateView):

      model = Curso
      success_url = "/AppCoder/curso/list"
      fields = ['nombre', 'camada']


class CursoUpdate(UpdateView):

      model = Curso
      success_url = "/AppCoder/curso/list"
      fields  = ['nombre', 'camada']


class CursoDelete(DeleteView):

      model = Curso
      success_url = "/AppCoder/curso/list"




def logout_request(request):
      logout(request)
     
      return redirect("inicio")
     

def login_request(request):


      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')

                  user = authenticate(username=usuario, password=contra)

            
                  if user is not None:
                        login(request, user)
                       
                        return render(request,"AppCoder/inicio.html",  {"mensaje":f"Bienvenido {usuario}"} )
                  else:
                        
                        return render(request,"AppCoder/inicio.html", {"mensaje":"Error, datos incorrectos"} )

            else:
                        
                        return render(request,"AppCoder/inicio.html" ,  {"mensaje":"Error, formulario erroneo"})

      form = AuthenticationForm()

      return render(request,"AppCoder/login.html", {'form':form} )



def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppCoder/inicio.html" ,  {"mensaje":"Usuario Creado :)"})


      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"AppCoder/registro.html" ,  {"form":form})



@login_required
def editarPerfil(request):

      #Instancia del login
      usuario = request.user
     
      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST) 
            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data
            
                  #Datos que se modificarán
                  usuario.email = informacion['email']
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password1']
                  usuario.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= UserEditForm(initial={ 'email':usuario.email}) 

      #Voy al html que me permite editar
      return render(request, "AppCoder/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})



@login_required
def agregarAvatar(request):
      if request.method == 'POST':

            miFormulario = AvatarFormulario(request.POST, request.FILES) #aquí mellega toda la información del html

            if miFormulario.is_valid:   #Si pasó la validación de Django


                  u = User.objects.get(username=request.user)
                
                  avatar = Avatar (user=u, imagen=miFormulario.cleaned_data['imagen']) 
      
                  avatar.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= AvatarFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/agregarAvatar.html", {"miFormulario":miFormulario})


def urlImagen():

      return "/media/avatares/logo.png"