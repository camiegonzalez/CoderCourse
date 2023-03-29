
from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):

    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
   
    last_name = forms.CharField()
    first_name = forms.CharField()
    imagen_avatar = forms.ImageField(required=False)

   

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name'] 
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}


class CarterasFormulario(forms.Form):
    color= forms.CharField(max_length=30)
    material= forms.CharField(max_length=30)
    precio=forms.IntegerField()
    capacidad = forms.IntegerField()
    nombre= forms.CharField(max_length=30)


class MaquillajesFormulario(forms.Form):
    tipo= forms.CharField(max_length=30)
    color= forms.CharField(max_length=30)
    tamanio= forms.CharField(max_length=30)
    precio=forms.IntegerField()
    water_proof = forms.BooleanField()
    nombre= forms.CharField(max_length=30)


class RopaFormulario(forms.Form):
    tipo= forms.CharField(max_length=30)
    color= forms.CharField(max_length=30)
    talle= forms.CharField(max_length=30)
    precio=forms.IntegerField()
    nombre= forms.CharField(max_length=30)