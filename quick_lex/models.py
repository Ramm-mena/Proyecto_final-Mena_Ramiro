from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#personal---------------------------------------->

class Staff(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    cargo= models.CharField(max_length=50)
    telefono= models.IntegerField()
    email= models.EmailField()

    def __str__(self):
        return f'{self.apellido},{self.nombre}'
class Abogados(models.Model):

    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    Especialidad= models.CharField(max_length=50)
    matricula= models.IntegerField()
    telefono= models.IntegerField()
    email= models.EmailField()

    def __str__(self):
        return f'{self.apellido},{self.nombre}'

#clientes---------------------------------------->

class Personas(models.Model):

    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    telefono= models.IntegerField()
    email= models.EmailField()

    def __str__(self):
        return f'{self.apellido},{self.nombre}'
    
#causa------------------------------------------->

class Expediente(models.Model):
    cartula= models.CharField(max_length=50)
    fuero= models.CharField(max_length=50)
    numero= models.IntegerField()
    abogado= models.CharField(max_length=50)
    personas= models.CharField(max_length=120)
    estado= models.CharField(max_length=50)

#avatar------------------------------------------> 

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.OneToOneField(User, on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.user} [{self.imagen}]"   
    