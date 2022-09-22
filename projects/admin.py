from django.contrib import admin
from . models import Proyecto
from .models import Revision
from .models import Tag


# Register your models here.
admin.site.register(Proyecto)
admin.site.register(Revision)
admin.site.register(Tag)


