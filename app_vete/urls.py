from django.contrib import admin
from django.urls import path

from app_vete import views

urlpatterns = [

    path('', views.inicio, name = "inicio"),
    path('sucursal/', views.sucursal, name = "sucursal"),
    path('producto/', views.producto, name = "producto"),
    path('cliente/', views.cliente, name = "cliente"),
    path('mascota/', views.mascota, name = "mascota"),
    path('mascota-form/', views.formulario_mascota, name = "mascota-form" ),
    path('cliente-form/', views.formulario_cliente, name = "cliente-form" ),
    path('producto-form/', views.formulario_producto, name = "producto-form" ),
    path('sucursal-form/', views.formulario_sucursal, name = "sucursal-form" ),
    path('registro-exitoso/', views.registro_exitoso, name = "registro-exitoso" ),
    
]