from typing import List

from django.shortcuts import redirect, render
from AppCoder.models import Cartera, Maquillaje, Ropa
from AppCoder.forms import CarterasFormulario, RopaFormulario,MaquillajesFormulario, UserRegisterForm

#Para el login

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

#Decorador por defecto
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def inicio(request):
      
      return render(request, "AppCoder/inicio.html")

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
