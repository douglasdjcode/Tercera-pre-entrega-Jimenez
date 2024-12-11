from django.contrib import admin

# Register your models here.
from .models import (Cliente, Mascota, Sucursal, Producto) 

admin.site.register(Mascota)
admin.site.register(Cliente)
admin.site.register(Sucursal)
admin.site.register(Producto)