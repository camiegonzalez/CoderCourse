from typing import List

from django.shortcuts import redirect, render
from AppCoder.models import Cartera, Maquillaje, Ropa
from AppCoder.forms import CarterasFormulario, RopaFormulario,MaquillajesFormulario, UserRegisterForm
from django.urls import reverse_lazy
#Para el login

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

#Decorador por defecto
from django.contrib.auth.decorators import login_required

# Create your views here.

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView

def inicio(request):
      
      return render(request, "AppCoder/inicio.html")

@login_required
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
      return render(request, "AppCoder/inicio.html", {"respuesta":respuesta})

@login_required
def carteras(request):

      carteras = Cartera.objects.all()

      contexto= {"object_list":carteras} 

      return render(request, "AppCoder/cartera_list.html",contexto)

@login_required
def maquillaje(request):

      maquillajes = Maquillaje.objects.all()

      contexto= {"maquillajes":maquillajes} 

      return render(request, "AppCoder/leerMaquillaje.html",contexto)

@login_required
def ropa(request):

      ropa = Ropa.objects.all()

      contexto= {"ropa":ropa} 

      return render(request, "AppCoder/leerRopa.html",contexto)


@login_required
def agregarMaquillaje(request):

      if request.method == 'POST':

            miFormulario = MaquillajesFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  maquillajes = Maquillaje (tipo=informacion['tipo'], tamanio=informacion['tamanio'], color=informacion['color'], precio=informacion['precio'], water_proof=informacion['water_proof'], nombre=informacion['nombre']) 

                  maquillajes.save()

                  maquillajesGuardados = Maquillaje.objects.all()

                  contexto= {"maquillajes":maquillajesGuardados} 

                  return render(request, "AppCoder/leerMaquillaje.html",contexto)

      else: 

            miFormulario= MaquillajesFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/maquillaje.html", {"miFormulario":miFormulario})

@login_required
def agregarRopa(request):

      if request.method == 'POST':

            miFormulario = RopaFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  ropa = Ropa (tipo=informacion['tipo'], talle=informacion['talle'], color=informacion['color'], precio=informacion['precio'], nombre=informacion['nombre']) 

                  ropa.save()


                  prendasGuardadas = Ropa.objects.all()

                  contexto= {"ropa":prendasGuardadas} 

                  return render(request, "AppCoder/leerRopa.html",contexto)

      else: 

            miFormulario= RopaFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/ropa.html", {"miFormulario":miFormulario})

@login_required
def agregarCartera(request):

      if request.method == 'POST':

            miFormulario = CarterasFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  cartera = Cartera (material=informacion['material'], capacidad=informacion['capacidad'], color=informacion['color'], precio=informacion['precio'], nombre=informacion['nombre']) 

                  cartera.save()

                  return redirect('Carteras')

      else: 

            miFormulario= CarterasFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/cartera.html", {"miFormulario":miFormulario})

@login_required
def eliminarCartera(request, code_cartera):
 
    cartera = Cartera.objects.get(code=code_cartera)
    cartera.delete()
 
    return redirect("Carteras")

@login_required
def editarCartera(request, code_cartera):

    # Recibe el nombre del profesor que vamos a modificar
    cartera = Cartera.objects.get(code=code_cartera)

    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = CarterasFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            cartera.nombre = informacion['nombre']
            cartera.color = informacion['color']
            cartera.material = informacion['material']
            cartera.precio = informacion['precio']
            cartera.capacidad = informacion['capacidad']

            cartera.save()

            # Vuelvo al inicio o a donde quieran
            return redirect("Carteras")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = CarterasFormulario(initial={'nombre': cartera.nombre, 'color': cartera.color,
                                                   'material': cartera.material, 'precio': cartera.precio, 'capacidad': cartera.capacidad})

    # Voy al html que me permite editar
    return render(request, "AppCoder/editarCartera.html", {"miFormulario": miFormulario, "code_cartera": code_cartera})

@login_required
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


class CarteraList(ListView):
      model = Cartera
      template_name = "AppCoder/cartera_list"

class CarteraDetalle(DetailView):
      model = Cartera
      template_name= "/AppCoder/cartera_detalle.html"

class CarteraCreation(CreateView):
      model = Cartera
      success_url="/AppCoder/cartera_list"
      fields= ["nombre", "precio", "capacidad", "material", "color"]

class CarteraUpdate(UpdateView):
      model = Cartera
      success_url="/AppCoder/cartera_list"
      fields= ["nombre", "precio", "capacidad", "material", "color"]

class CarteraDelete(DeleteView):
      model = Cartera
      success_url="/AppCoder/cartera_list"


