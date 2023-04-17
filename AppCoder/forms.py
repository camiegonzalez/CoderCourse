
from django import forms
from django.contrib.auth.models import User
from AppCoder.models import Avatar
from django.contrib.auth.forms import UserCreationForm

class MessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={"rows":"4", "columns": "3"}))

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)

class UserEditForm(UserCreationForm):

    # Obligatorios
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
    label='Repetir la contraseña', widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']


class UserRegisterForm(UserCreationForm):

    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
   
    last_name = forms.CharField()
    first_name = forms.CharField()
    imagen_avatar = forms.ImageField(required=False)
    
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('imagen_avatar',)

    def save(self, commit=True):
        user = super().save(commit=commit)
        imagen_avatar = self.cleaned_data.get('imagen_avatar', None)
        if imagen_avatar:
            avatar = Avatar(user=user, imagen=imagen_avatar)
            avatar.save()
        return user


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name'] 
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}