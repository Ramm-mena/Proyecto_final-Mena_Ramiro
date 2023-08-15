from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    #principal--------------------------------->
    path('', index, name= "main"),
    #personal---------------------------------->
    path('staff/', staff , name= "sta"),
    path('Staform/', staForm, name= "staff_create"),
    path('delStaff/<id_staff>', deleteSta, name= "staff_delete"),
    path('upStaff/<id_staff>', updateSta, name= "staff_update"),
    #abogados---------------------------------->
    path('abogados/', abogados, name= "abog"),
    path('Abogform/', abogForm, name= "abog_create"),
    path('delAbog/<id_abogado>', deleteAbo, name= "abog_delete"),
    path('upAbog/<id_abogado>', updateAbo, name= "abog_update"),
    #personas---------------------------------->
    path('personas/' ,personas, name="pers"),
    path('create_pers/', createPers, name="pers_create"),
    path('delete_pers/<id_personas>/', deletePers, name="pers_delete"),
    path('update_pers/<id_personas>/', updatePers, name="pers_update"),
    #expedientes------------------------------->
    path('exptes/' ,expedientes, name="exp"),
    path('create_exptes/', createExp, name="exp_create"),
    path('delete_exptes/<id_expediente>/', deleteExp, name="exp_delete"),
    path('update_exptes/<id_expediente>/', updateExp, name="exp_update"),
    #BUSCADOR---------------------------------->
    path('buscarexp/', buscarExp, name="buscar_exp"),
    path('buscador/', buscador, name="buscador"),
    #REGISTRO---------------------------------->
    path('registro/', registro, name="registro"),
    #LOGIN/LOGOUT------------------------------>
    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="quick_lex/logout.html"), name="logout"),
    #EDITAR USUARIO---------------------------->
    path('editar_usuario/', editarUsuario, name="user_edit"),
    path('avatar/', addAvatar, name="agregar_avatar"),
    #ABOUT ME---------------------------------->
    path('about_me/' , aboutMe, name="about_me"),

]
