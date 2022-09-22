from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse

#Importo la clase Proyecto del modelo
from .models import Proyecto

#IMPORTO el archivo Forms. py (Clase proyectoForm)--
from .forms import ProyectoForm


#Definimos la vista la cual nos retorna un valor del controlador

#----CONSULTA GENERAL DE PROYECTOS-----------
def proyectos(request):
    
    #Emulamos un select *from tabla
    proyecto=Proyecto.objects.all()
    context={'proyecto':proyecto}
    return render(request,"proyectos/proyectos.html",context)

   
#-----CONSULTA ESPECIFICA DE PROYECTOS ID------------------------
def proyecto(request, pk):
    proyectoObj=Proyecto.objects.get(Id=pk)
    return render(request,"proyectos/consula_proyectos.html",{"proyecto":proyectoObj})


#------CREACION DE PROYECTOS-----
def creacionProyectos(request):
    #--INSTANCIO LA CLASE PROYECTO FORM---
    form=ProyectoForm()

    #--- SI LA PETICION ES POST
    if(request.method=="POST"):
        form=ProyectoForm(request.POST,request.FILES)

        if(form.is_valid()):
            form.save()
            return redirect("proyectos")

    context={'form':form}
    return render(request,"proyectos/agregar_proyectos.html",context)


#------ACTUALIZACION DE PROYECTOS----

def ActualizarProyecto(request,pk):
    #--INSTANCIO LA CLASE PROYECTO FORM---
    proyecto=Proyecto.objects.get(Id=pk)

    #---ASIGNO LOS DATOS RECUPERADOS (FILTRADOS DE LA BUSQUEDA)-----
    form=ProyectoForm(instance=proyecto)

    #--- SI LA PETICION ES POST
    if(request.method=="POST"):
        form=ProyectoForm(request.POST,request.FILES,instance=proyecto)

        if(form.is_valid()):
            form.save()
            return redirect("proyectos")

    context={'form':form}
    return render(request,"proyectos/agregar_proyectos.html",context)



#------ELIMINACION DE PROYECTOS-------
def EliminarProyectos(request,Identificador):
    #--INSTANCIO LA CLASE PROYECTO FORM---
    proyecto=Proyecto.objects.get(Id=Identificador)

    #--- SI LA PETICION ES POST
    if(request.method=="POST"):
        proyecto.delete()
        return redirect("proyectos")

    context={"objeto": proyecto}
    template_name="proyectos/eliminar_proyecto.html"
    return render(request,template_name, context)

       







#----HACER LA PANTALL DE BIENVENIDO----
def HolaMundoProyectos(request):
    return HttpResponse ("Hola mundo modulo de proyectos")
