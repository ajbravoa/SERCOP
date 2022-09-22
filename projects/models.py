from email.policy import default
from statistics import mode
from django.db import models

#---LIBRERIA QUE PERMITE GENERAR UN SECUENCIAL
import uuid 

# Create your models here.

#Clase Principal del Modulo Proyectos (modelo)
class Proyecto(models.Model):
    Titulo=models.CharField(max_length=200)
    Descripcion=models.TextField(null=True,blank=True)
    #----PARA CARGA DE IMAGEN----
    ImagenDefecto=models.ImageField(null=True, blank=True,default="proyectos.png")
    
    DemoLink=models.CharField(max_length=2000,null=True, blank=True)
    SourceLink=models.CharField(max_length=2000,null=True, blank=True)
    VotosTotal=models.IntegerField(default=0,null=True, blank=True)
    VotosRatio=models.IntegerField(default=0,null=True, blank=True)
    
    #Esta relacion me crea una lista
    Tags=models.ManyToManyField('Tag',blank=True)

    FechaCreacion=models.DateTimeField(auto_now_add=True)
    Id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)

    def __str__(self):
        return self.Titulo

#---CLASE REVISIONES-----
class Revision(models.Model):

    #Lista que sera asignada al comboBox
    Tipo_Voto=(
        (
            'up', 'Voto Aprobado'
        ),

        (
            'down','Voto Negado'
        )
    )
    projecto=models.ForeignKey(Proyecto,on_delete=models.CASCADE)
    Propietario=models.TextField(null=True,blank=True)
    Body=models.TextField(null=True, blank=True)
    #---EMULO UN CAMBO BOX--
    Valor=models.CharField(max_length=200,choices=Tipo_Voto)
    FechaCreacion=models.DateTimeField(auto_now_add=True)
    Id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)

    def __str_(self):
        return self.Valor


#---CLASE ETIQUETAS (TAG)-----
class Tag(models.Model):
    Nombre=models.CharField(max_length=200)
    FechaCreacion=models.DateTimeField(auto_now_add=True)
    Id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)

    def __str__(self):
        return self.Nombre
    







   


