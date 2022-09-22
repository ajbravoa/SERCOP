from django.urls import path
from .import views




urlpatterns = [
    
    #AQUI HAGO QUE LA PAGINA DE PROYECTOS SEA EL INDEX

    #----RUTA DE CONSULTA GENERAL (VISTA)-----
    path('',views.proyectos, name='proyectos'),

    #-----RUTA DE CONSULTA ESPECIFICA (VISTA )---
    path('proyecto/<str:pk>/',views.proyecto, name="proyecto"),

    #------METODO DE PRESENTACION DE HOLA MUNDO
    path('HolaMundoProyectos/',views.HolaMundoProyectos, name="HolaMundoProyectos"),

    #------RUTA DE AGREGAR PROYECTOS-------
    path("agregar_proyectos/",views.creacionProyectos, name="agregar_proyectos"),

    #------ACTUALIZAR PROYECTOS------
    path("actualizar_proyectos/<str:pk>/",views.ActualizarProyecto, name="actualizar_proyectos"),

     #------ELIMINAR PROYECTOS------
    path("eliminar_proyectos/<str:Identificador>/",views.EliminarProyectos, name="eliminar_proyectos"),
    
    

]