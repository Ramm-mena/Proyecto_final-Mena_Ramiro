from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import*
from .forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout , update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404



# Create your views here.
#Pricipal---------------------------------------->
@login_required
def index(request):
    return render(request, 'quick_lex/base.html')
#Personal---------------------------------------->
@login_required
def staff(request):
    cxt= {'staff': Staff.objects.all()}
    return render(request, 'quick_lex/staff.html', cxt)

@login_required
def staForm(request):
    if request.method == "POST":
        miForm = Staform(request.POST)
        if miForm.is_valid():
            staff_nombre = miForm.cleaned_data.get('nombre')  
            staff_apellido = miForm.cleaned_data.get('apellido')
            staff_cargo = miForm.cleaned_data.get('cargo')
            staff_telefono = miForm.cleaned_data.get('telefono')
            staff_email = miForm.cleaned_data.get('email')
            personal= Staff(nombre=staff_nombre,  
                               apellido=staff_apellido,
                               cargo=staff_cargo,
                               telefono=staff_telefono,
                               email=staff_email)
            personal.save()
            return redirect(reverse_lazy("sta"))
    else:
        miForm = Staform()

    return render(request, "quick_lex/staForm.html", {"form": miForm})

@login_required
def deleteSta(request, id_staff):
    staff = get_object_or_404(Staff, id=id_staff)
    staff.delete()
    return redirect(reverse_lazy('sta'))

@login_required
def updateSta(request, id_staff):
    staff = Staff.objects.get(id=id_staff)
    if request.method == "POST":
        miForm = Staform(request.POST)
        if miForm.is_valid():
            staff.nombre = miForm.cleaned_data.get('nombre')
            staff.apellido = miForm.cleaned_data.get('apellido')
            staff.cargo = miForm.cleaned_data.get('cargo')
            staff.telefono = miForm.cleaned_data.get('telefono')
            staff.email = miForm.cleaned_data.get('email')
            staff.save()
            return redirect(reverse_lazy("sta"))   
    else:
        miForm = Staform(initial={'nombre':staff.nombre, 
                                       'apellido':staff.apellido,
                                       'cargo':staff.cargo, 
                                       'telefono':staff.telefono, 
                                       'email':staff.email})  
    return render (request, "quick_lex/staForm.html", {'form': miForm})   


#Abogados---------------------------------------->
@login_required
def abogados(request):
  cxt= {'abogados': Abogados.objects.all()}
  return render(request, 'quick_lex/abogados.html', cxt)

@login_required
def abogForm(request):
    if request.method == "POST":
        miForm = Abogform(request.POST)
        if miForm.is_valid():
            abogado_nombre = miForm.cleaned_data.get('nombre')  
            abogado_apellido = miForm.cleaned_data.get('apellido')
            abogado_especialidad = miForm.cleaned_data.get('Especialidad')
            abogado_matricula = miForm.cleaned_data.get('matricula')
            abogado_telefono = miForm.cleaned_data.get('telefono')
            abogado_email = miForm.cleaned_data.get('email')
            lawyer= Abogados(nombre=abogado_nombre,  
                               apellido=abogado_apellido,
                               Especialidad=abogado_especialidad,
                               matricula=abogado_matricula,
                               telefono=abogado_telefono,
                               email=abogado_email)
            lawyer.save()
            return redirect(reverse_lazy("abog"))
    else:
        miForm = Abogform()

    return render(request, "quick_lex/abogForm.html", {"form": miForm})

@login_required
def deleteAbo(request, id_abogado):
    lawyer = get_object_or_404(Abogados, id=id_abogado)
    lawyer.delete()
    return redirect(reverse_lazy('abog'))

@login_required
def updateAbo(request, id_abogado):
    abogado = Abogados.objects.get(id=id_abogado)
    if request.method == "POST":
        miForm = Abogform(request.POST)
        if miForm.is_valid():
            abogado.nombre = miForm.cleaned_data.get('nombre')
            abogado.apellido = miForm.cleaned_data.get('apellido')
            abogado.Especialidad = miForm.cleaned_data.get('Especialidad')
            abogado.matricula = miForm.cleaned_data.get('matricula')
            abogado.telefono = miForm.cleaned_data.get('telefono')
            abogado.email = miForm.cleaned_data.get('email')
            abogado.save()
            return redirect(reverse_lazy("abog"))   
    else:
        miForm = Abogform(initial={'nombre':abogado.nombre, 
                                       'apellido':abogado.apellido,
                                       'Especialidad':abogado.Especialidad,
                                       'matricula':abogado.matricula,  
                                       'telefono':abogado.telefono, 
                                       'email':abogado.email})  
    return render (request, "quick_lex/abogForm.html", {'form': miForm})   

#Personas---------------------------------------->
@login_required
def personas(request):
   cxt= {'personas': Personas.objects.all()}
   return render(request, 'quick_lex/personas.html', cxt)

@login_required
def createPers(request):    
    if request.method == "POST":
        miForm = Persform(request.POST)
        if miForm.is_valid():
            pers_nombre = miForm.cleaned_data.get('nombre')
            pers_apellido = miForm.cleaned_data.get('apellido')
            pers_telefono = miForm.cleaned_data.get('telefono')
            pers_email = miForm.cleaned_data.get('email')
            persona = Personas(nombre=pers_nombre, 
                             apellido=pers_apellido,
                             telefono=pers_telefono,
                             email=pers_email
                             )
            persona.save()
            return redirect(reverse_lazy('pers'))
    else:
        miForm = Persform()
    return render(request, "quick_lex/persForm.html", {"form":miForm})

  
@login_required
def deletePers(request, id_personas):
    persona = get_object_or_404(Personas, id=id_personas)
    persona.delete()
    return redirect(reverse_lazy('pers'))

@login_required
def updatePers(request, id_personas):
    personas = Personas.objects.get(id=id_personas)
    if request.method == "POST":
        miForm = Persform(request.POST)
        if miForm.is_valid():
            personas.nombre = miForm.cleaned_data.get('nombre')
            personas.apellido = miForm.cleaned_data.get('apellido')
            personas.telefono = miForm.cleaned_data.get('telefono')
            personas.email = miForm.cleaned_data.get('email')
            personas.save()
            return redirect(reverse_lazy("pers"))   
    else:
        miForm = Persform(initial={'nombre':personas.nombre, 
                                       'apellido':personas.apellido, 
                                       'telefono':personas.telefono, 
                                       'email':personas.email})  
    return render (request, "quick_lex/persForm.html", {'form': miForm})   

#Expedientes------------------------------------->
@login_required
def expedientes(request):
   cxt= {'expedientes': Expediente.objects.all()}
   return render(request, 'quick_lex/expedientes.html', cxt)

@login_required
def createExp(request):    
    if request.method == "POST":
        miForm = Expform(request.POST)
        if miForm.is_valid():
            exp_caratula = miForm.cleaned_data.get('cartula')
            exp_fuero = miForm.cleaned_data.get('fuero')
            exp_numero = miForm.cleaned_data.get('numero')
            exp_abogado = miForm.cleaned_data.get('abogado')
            exp_personas = miForm.cleaned_data.get('personas')
            exp_estado = miForm.cleaned_data.get('estado')
            expediente = Expediente(cartula=exp_caratula,
                                    fuero=exp_fuero,
                                    numero=exp_numero,
                                    abogado=exp_abogado,
                                    personas=exp_personas
                                    ,estado=exp_estado)
            expediente.save()
            return redirect(reverse_lazy('exp'))
    else:
        miForm = Expform()

    return render(request, "quick_lex/expForm.html", {"form":miForm})

@login_required
def deleteExp(request, id_expediente):
    expediente = get_object_or_404(Expediente,id=id_expediente)
    expediente.delete()
    return redirect(reverse_lazy('exp'))

@login_required
def updateExp(request, id_expediente):
    expediente = Expediente.objects.get(id=id_expediente)
    if request.method == "POST":
        miForm = Expform(request.POST)
        if miForm.is_valid():
            expediente.cartula = miForm.cleaned_data.get('cartula')
            expediente.fuero = miForm.cleaned_data.get('fuero')
            expediente.numero = miForm.cleaned_data.get('numero')
            expediente.abogado = miForm.cleaned_data.get('abogado')
            expediente.personas = miForm.cleaned_data.get('personas')
            expediente.estado = miForm.cleaned_data.get('estado')
            expediente.save()
            return redirect(reverse_lazy('exp'))   
    else:
        miForm = Expform(initial={'caratula':expediente.cartula, 
                                  'fuero':expediente.fuero, 
                                  'numero':expediente.numero, 
                                  'abogado':expediente.abogado,
                                  'personas':expediente.personas,
                                  'estado':expediente.estado})         
    return render(request, "quick_lex/expForm.html", {'form': miForm})   

#FUNCIONES---------------------------------------->

#Buscador----------------------------------------->
@login_required
def buscarExp(request):
   return render(request, 'quick_lex/buscarexp.html')

@login_required
def buscador(request):

    if request.GET:
        expediente = request.GET['expedientes']
        info = Expediente.objects.filter(cartula__icontains= expediente)
        return render(request, "quick_lex/buscarexp.html", {"buscados":info})


    return render(request, "quick_lex/buscarexp.html")

#Registro----------------------------------------->
def registro(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():  
            usuario = form.cleaned_data.get('username')
            form.save()
            return render(request, "quick_lex/base.html", {"mensaje":"Usuario Creado"})        
    else:
        form = RegisterForm() 

    return render(request, "quick_lex/registro.html", {"form": form})  
#login--------------------------------------------> 
def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            clave = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return render(request, "quick_lex/base.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, "quick_lex/login.html", {"form":miForm, "mensaje": "Datos Inválidos"})
        else:    
            return render(request, "quick_lex/login.html", {"form":miForm, "mensaje": "Datos Inválidos"})

    miForm = AuthenticationForm()

    return render(request, "quick_lex/login.html", {"form":miForm})    
#Editar usuario----------------------------------->

@login_required
def editarUsuario(request):
    usuario = request.user
    if request.method == "POST":
        form = EditForm(request.POST, instance=usuario)
        if form.is_valid():
            user = form.save(commit=False)
            new_password1 = form.cleaned_data.get('new_password1')
            new_password2 = form.cleaned_data.get('new_password2')
            if new_password1 == new_password2 and new_password1:
                user.set_password(new_password1)
                user.save()
                update_session_auth_hash(request, user)
                return render(request, "quick_lex/base.html", {'mensaje': f"Usuario {usuario.username} actualizado correctamente"})
            elif new_password1:
                form.add_error('new_password2', 'Las contraseñas no coinciden')
    else:
        form = EditForm(instance=usuario)
    return render(request, "quick_lex/user_edit.html", {'form': form, 'usuario': usuario.username})

#Avatar------------------------------------------->

@login_required
def addAvatar(request):
    if request.method == "POST":
        form = Avatarform(request.POST, request.FILES)
        if form.is_valid():
            renovar_avatar = Avatar.objects.filter(user=request.user)
            if len(renovar_avatar) > 0: 
                renovar_avatar[0].delete()
            avatar = Avatar(user=request.user, imagen=form.cleaned_data['imagen'])
            avatar.save()
        return render(request, "quick_lex/base.html")
    else:
        form = Avatarform()
    return render(request, "quick_lex/addAvatar.html", {'form': form})

#About me----------------------------------------->
@login_required
def aboutMe(request):
    return render(request, 'quick_lex/about_me.html')