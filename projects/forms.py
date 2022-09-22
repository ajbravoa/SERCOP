from .models import Proyecto

#---SETEA LOS CAMPOS DE LA ENTIDAD (CLASE) A COMPONENTES HTML-----
from django.forms import ModelForm


#ESTA CLASE ES AQUELLA QUE ME PERMITIRA REALIZAR UN INGRESO O ACTUALIZACION
class ProyectoForm(ModelForm):
    class Meta:
        model=Proyecto
        #fields="__all__"

        #---OBTENGO LOS ATRIBUTOS DE LA CLASE PROYECTO-----
        fields=["Titulo","Descripcion","DemoLink", "SourceLink", "VotosTotal","VotosRatio", "ImagenDefecto", "Tags"]