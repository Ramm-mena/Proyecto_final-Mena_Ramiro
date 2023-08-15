from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

#Formulario para registro de personal-------------------->

class Staform(forms.Form):
    nombre= forms.CharField(label='Nombre' ,max_length=50,required=True)
    apellido= forms.CharField(label='Apellido' ,max_length=50,required=True)
    cargo= forms.CharField(label='Cargo',max_length=50)
    telefono= forms.IntegerField(label='telefono',required=True)
    email= forms.EmailField(label='Email',required=True)

#Formulario para registro de abogados del estudio-------->

class Abogform(forms.Form):

    nombre= forms.CharField(label='Nombre',max_length=50, required=True)
    apellido= forms.CharField(label='Apellido',max_length=50,required=True)
    Especialidad= forms.CharField(label='Especialidad',max_length=50, required=True)
    matricula= forms.IntegerField(label='Matricula',required=True)
    telefono= forms.IntegerField(label='Telefono')
    email= forms.EmailField(label='Email')

#Formulario de expedientes------------------------------->
class Expform(forms.Form):
    cartula = forms.CharField(label='Caratula', max_length=50, required=True)
    fuero = forms.CharField(label='Fuero', max_length=50, required=True)
    numero = forms.IntegerField(label='Numero')
    abogado = forms.CharField(label='Abogado', max_length=50, required=True)
    personas = forms.CharField(label='Personas de contacto', max_length=120)
    estado = forms.CharField(label="Estado", max_length=50)

#Formulario de registro de personas---------------------->
class Persform(forms.Form):
    nombre= forms.CharField(label='Nombre', max_length=50, required=True)
    apellido= forms.CharField(label='Apellido', max_length=50, required=True)
    telefono= forms.IntegerField(label='Telefono', required=True)
    email= forms.EmailField(label='Email' , required=True)

#Registro de usuario------------------------------------->
class RegisterForm(UserCreationForm):
    email= forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#Edición de usuario-------------------------------------->   
class EditForm(UserChangeForm):
    new_password1 = forms.CharField(
        label='Nueva Contraseña', widget=forms.PasswordInput, required=False)
    new_password2 = forms.CharField(
        label='Repetir Nueva Contraseña', widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ['username', 'email']

#Avatar--------------------------------------------------->
class Avatarform(forms.Form):
    imagen = forms.ImageField(label= 'Elegi una imagen para tu usuario:' ,required=True)     
