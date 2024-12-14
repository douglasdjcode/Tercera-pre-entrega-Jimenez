from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.urls import reverse_lazy

from.forms import MascotasFormulario, ClienteFormulario, ProductoFormulario, SucursalFormulario

from .models import (Sucursal, Producto, Cliente, Mascota)

# Create your views here.

def inicio(request):
    return render(request,"app_vete/index.html")

def sucursal(request):

    query = request.GET.get('q')

    if query:
        sucursales = Sucursal.objects.filter(Q(nombre__icontains=query) | Q(direccion__icontains=query) | Q(telefono__icontains=query))

    else:
        sucursales = Sucursal.objects.all()


    return render(request,"app_vete/sucursal.html", {"sucursales": sucursales})

def producto(request):

    query = request.GET.get('q')

    if query:
        producto = Producto.objects.filter(Q(nombre__icontains=query) | Q(precio__icontains=query) | Q(categoria__icontains=query))

    else:

        producto = Producto.objects.all()

    return render(request,"app_vete/producto.html", {"producto": producto})
    

def cliente(request):

    query = request.GET.get('q')

    if query:
        cliente = Cliente.objects.filter(Q(nombre__icontains=query) | Q(telefono__icontains=query) | Q(email__icontains=query))


    else:
    
        cliente = Cliente.objects.all()
    print(cliente)
    return render(request,"app_vete/cliente.html", {"cliente": cliente})

def mascota(request):

    query = request.GET.get('q')

    if query:
        mascota = Mascota.objects.filter(Q(especie__icontains=query) | Q(edad__icontains=query) | Q(raza__icontains=query))
        
    else:

        mascota = Mascota.objects.all()

    return render(request,"app_vete/mascota.html", {"mascota": mascota})

def formulario_mascota(request):

    if request.method == "POST":
        mascota_form = MascotasFormulario(request.POST)
        if mascota_form.is_valid():
            info_limpia = mascota_form.cleaned_data
            mascota = Mascota(especie = info_limpia["especie"], raza = info_limpia["raza"], edad = info_limpia["edad"]) 
            mascota.save()
            return redirect("registro-exitoso")
        
    else:
        mascota_form = MascotasFormulario()
    contexto = {"mascota_form": mascota_form}
    print(contexto)
    return render(request, "app_vete/forms/mascota-formulario.html", contexto)

def formulario_cliente(request):
    if request.method == "POST":
        cliente_form = ClienteFormulario(request.POST)
        if cliente_form.is_valid():
            info_limpia = cliente_form.cleaned_data
            cliente = Cliente(nombre=info_limpia["nombre"], telefono=info_limpia["telefono"], email=info_limpia["email"])
            cliente.save()
            return redirect("registro-exitoso")

    else:
        cliente_form = ClienteFormulario()
    contexto = {"cliente_form": cliente_form}
    return render(request, "app_vete/forms/cliente-formulario.html", contexto)

def formulario_producto(request):
    if request.method == "POST":
        producto_form = ProductoFormulario(request.POST)
        if producto_form.is_valid():
            info_limpia = producto_form.cleaned_data
            producto = Producto(nombre=info_limpia["nombre"], precio=info_limpia["precio"], categoria=info_limpia["categoria"])
            producto.save()
            return redirect("registro-exitoso")
    else:
        producto_form = ProductoFormulario()
    contexto = {"producto_form": producto_form}
    return render(request, "app_vete/forms/producto-formulario.html", contexto)

def formulario_sucursal(request):
    if request.method == "POST":
        sucursal_form = SucursalFormulario(request.POST)
        if sucursal_form.is_valid():
            info_limpia = sucursal_form.cleaned_data
            sucursal = Sucursal(nombre=info_limpia["nombre"], direccion=info_limpia["direccion"], telefono=info_limpia["telefono"])
            sucursal.save()
            return redirect("registro-exitoso")
    else:
        sucursal_form = SucursalFormulario()
    contexto = {"sucursal_form": sucursal_form}
    return render(request, "app_vete/forms/sucursal-formulario.html", contexto)

def registro_exitoso(request):
    return render(request,"app_vete/forms/registro-exitoso.html")


def eliminar_producto(request, id):

    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect("producto")

def eliminar_mascota(request, id):

    mascota = Mascota.objects.get(id=id)
    mascota.delete()
    return redirect("mascota")

def eliminar_cliente(request, id):

    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect("cliente")

def eliminar_sucursal(request, id):

    sucursal = Sucursal.objects.get(id=id)
    sucursal.delete()
    return redirect("sucursal")

def editar_sucursal(request, id):

    sucursal = Sucursal.objects.get(id=id)

    if request.method == "POST":
        sucursal_form = SucursalFormulario(request.POST)
        if sucursal_form.is_valid():
            info_limpia = sucursal_form.cleaned_data
            sucursal.nombre = info_limpia["nombre"]
            sucursal.direccion = info_limpia["direccion"]
            sucursal.telefono = info_limpia["telefono"]
            sucursal.save()
        return redirect("sucursal")

    else:
        sucursal = Sucursal.objects.get(id=id)
        sucursal_form = SucursalFormulario(initial={"nombre": sucursal.nombre, "direccion": sucursal.direccion , "telefono": sucursal.telefono})

    return render(request, "app_vete/forms/editar-sucursal.html", {"sucursal_form": sucursal_form})


def editar_mascota(request, id):

    mascota = Mascota.objects.get(id=id)

    if request.method == "POST":
        mascota_form = MascotasFormulario(request.POST)
        if mascota_form.is_valid():
            info_limpia = mascota_form.cleaned_data
            mascota.especie = info_limpia["especie"]
            mascota.raza = info_limpia["raza"]
            mascota.edad = info_limpia["edad"]
            mascota.save()
        return redirect("mascota")

    else:
        mascota = Mascota.objects.get(id=id)
        mascota_form = MascotasFormulario(initial={"especie": mascota.especie, "raza": mascota.raza , "edad": mascota.edad})

    return render(request, "app_vete/forms/editar-mascota.html", {"mascota_form": mascota_form})


def editar_cliente(request, id):

    cliente = Cliente.objects.get(id=id)

    if request.method == "POST":
        cliente_form = ClienteFormulario(request.POST)
        if cliente_form.is_valid():
            info_limpia = cliente_form.cleaned_data
            cliente.nombre = info_limpia["nombre"]
            cliente.telefono = info_limpia["telefono"]
            cliente.email = info_limpia["email"]
            cliente.save()
        return redirect("cliente")

    else:
        cliente = Cliente.objects.get(id=id)
        cliente_form = ClienteFormulario(initial={"nombre": cliente.nombre, "telefono": cliente.telefono , "email": cliente.email})

    return render(request, "app_vete/forms/editar-cliente.html", {"cliente_form": cliente_form})


def editar_producto(request, id):

    producto = Producto.objects.get(id=id)

    if request.method == "POST":
        producto_form = ProductoFormulario(request.POST)
        if producto_form.is_valid():
            info_limpia = producto_form.cleaned_data
            producto.nombre = info_limpia["nombre"]
            producto.precio = info_limpia["precio"]
            producto.categoria = info_limpia["categoria"]
            producto.save()
        return redirect("producto")

    else:
        producto = Producto.objects.get(id=id)
        producto_form = ProductoFormulario(initial={"nombre": producto.nombre, "precio": producto.precio , "categoria": producto.categoria})

    return render(request, "app_vete/forms/editar-producto.html", {"producto_form": producto_form})