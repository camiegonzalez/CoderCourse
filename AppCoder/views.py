from typing import List
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import redirect, render
from AppCoder.models import Blog, Avatar, Message
from AppCoder.forms import UserEditForm, UserRegisterForm, MessageForm
from django.urls import reverse_lazy
# Para el login
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Decorador por defecto
from django.contrib.auth.decorators import login_required

# Create your views here.

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView


def about(request):
    avatar = ""
    if request.user.id:
        avatar = Avatar.objects.filter(user=request.user.id)[0].imagen.url
    return render(request, "AppCoder/about.html", {"url": avatar, "user": request.user})


def inicio(request):
    avatar = ""
    mensaje = f"Bienvenido"

    if request.user.id:
        avatar = Avatar.objects.filter(user=request.user.id)[0].imagen.url
        mensaje = f"Bienvenido {request.user}"
    return render(request, "AppCoder/inicio.html", {"user": request.user, "url": avatar, "mensaje": mensaje})


@login_required
def verPerfil(request):
   avatar = ""
   mensaje = f"Bienvenido"

   if request.user.id:
      avatar = Avatar.objects.filter(user=request.user.id)[0].imagen.url
      mensaje = f"Bienvenido {request.user}"
      return render(request, "AppCoder/verPerfil.html", {"user": request.user, "url": avatar, "mensaje": mensaje })


@login_required
def buscar(request):
    avatar = ""
    if request.user.id:
        avatar = Avatar.objects.filter(user= request.user.id)[0].imagen.url

    if request.GET["titulo"] and request.GET["autor"]:
        autor = request.GET['autor']
        titulo = request.GET['titulo']
        blogs = Blog.objects.filter(autor__icontains=autor, titulo__icontains=titulo)
        return render(request, "AppCoder/inicio.html", {"user": request.user, "url": avatar, "blogs":blogs, "autor":autor, "titulo": titulo })
    elif request.GET["autor"] and not request.GET["titulo"]:
        autor = request.GET['autor']
        blogs = Blog.objects.filter(autor__icontains=autor)
        return render(request, "AppCoder/inicio.html", {"user": request.user, "url": avatar, "blogs":blogs, "autor":autor, "titulo": "Cualquiera"})
    elif not request.GET["autor"] and request.GET["titulo"]:
        titulo = request.GET['titulo']
        blogs = Blog.objects.filter(titulo__icontains=titulo)
        return render(request, "AppCoder/inicio.html", {"user": request.user, "url": avatar, "blogs":blogs, "autor": "Cualquiera", "titulo": titulo})
    else:
        respuesta = "No enviaste datos"
    return render(request, "AppCoder/inicio.html", {"user": request.user, "url": avatar, "respuesta":respuesta})


@login_required
def messages(request):
    if request.method == 'POST':

        miFormulario = MessageForm(request.POST)  # aquí mellega toda la información del html

        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django

            messageInfo = miFormulario.cleaned_data

            message = Message (user=request.user.username, message = messageInfo['message'])

            message.save()

            return redirect('Messages')

    else:
        messages = Message.objects.all()
        print(messages[0].dateTime)

        miFormulario = MessageForm() #Formulario vacio para construir el html
    avatar = ""
    if request.user.id:
        avatar = Avatar.objects.filter(user= request.user.id)[0].imagen.url
    return render(request, "AppCoder/message_list.html", {"url": avatar, "messages": messages, "miFormulario": miFormulario, "user": request.user})


@login_required
def logout_request(request):
    logout(request)

    return redirect("Inicio")


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data= request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                return redirect('Inicio')

                # avatar = Avatar.objects.filter(user = request.user.id)[0].imagen.url
                # return render(request,"AppCoder/inicio.html",  {"url": avatar,"mensaje":f"Bienvenido {usuario}"} )
            else:

                return render(request, "AppCoder/login.html", {'form':form, "mensaje":"Error, formulario erroneo"})

        else:

            return render(request, "AppCoder/login.html", {'form':form, "mensaje":"Error, formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "AppCoder/login.html", {'form':form} )


@login_required
def editarPerfil(request):
    print(request.user, '-----')
    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()
            avatar = Avatar.objects.filter(user= request.user.id)[0].imagen.url

            return render(request, "AppCoder/inicio.html", {"url": avatar, "mensaje": f"Bienvenido {usuario}", "user":usuario})

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "AppCoder/editarPerfil.html", {"miFormulario": miFormulario, "user": usuario})


def register(request):

    if request.method == 'POST':

        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()
            print(request.FILES, '+++++++++++++++++', form.cleaned_data)

            u = User.objects.get(username=form.cleaned_data['username'])
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen_avatar'])
            avatar.save()

            return render(request, "AppCoder/inicio.html" ,  {"mensaje":"Usuario Creado :)"})

    else:
        #form = UserCreationForm()
        form = UserRegisterForm()

    return render(request, "AppCoder/registro.html" ,  {"form":form})


class BlogList(LoginRequiredMixin, ListView):
    model = Blog
    template_name = "AppCoder/blog_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        avatar = ""
        if self.request.user.id:
            avatar = Avatar.objects.filter(user= self.request.user.id)[0].imagen.url
            print(avatar)
        context['url'] = avatar
        return context


class BlogDetalle(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = "AppCoder/blog_detalle.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        avatar = ""
        if self.request.user.id:
            avatar = Avatar.objects.filter(user= self.request.user.id)[0].imagen.url
            print(avatar)
        context['url'] = avatar
        return context


class BlogCreation(LoginRequiredMixin, CreateView):
    model = Blog
    success_url = "/AppCoder/pages"
    fields = ["titulo", "subtitulo", "cuerpo", "autor", "imagen"]
    template_name = "AppCoder/blog_creation.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        avatar = ""
        if self.request.user.id:
            avatar = Avatar.objects.filter(user= self.request.user.id)[0].imagen.url
            print(avatar)
        context['url'] = avatar
        return context


class BlogUpdate(LoginRequiredMixin, UpdateView):
    model = Blog
    success_url = "/AppCoder/pages"
    fields = ["titulo", "subtitulo", "cuerpo","autor", "imagen"]
    template_name = "AppCoder/blog_edit.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        avatar = ""
        if self.request.user.id:
            avatar = Avatar.objects.filter(user= self.request.user.id)[0].imagen.url
            print(avatar)
        context['url'] = avatar
        return context


class BlogDelete(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = "/AppCoder/pages"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        avatar = ""
        if self.request.user.id:
            avatar = Avatar.objects.filter(user= self.request.user.id)[0].imagen.url
            print(avatar)
        context['url'] = avatar
        return context
