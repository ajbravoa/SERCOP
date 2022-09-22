from http.client import HTTPResponse
from django.contrib import admin
from django.urls import path,include

#----LIBRERIAS PARA EL TRATAOD DE IMAGENES-----
from django.conf import settings
from django.conf.urls.static import static

#Importamos momentaneamente la libreria HttpResponde
from django.http import HttpResponse



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('projects.urls'))

]

#----REGISTRAMOS LAS PROPIEDADES DEL ARCHIVO SETTINGS DE IMANGES-------
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
