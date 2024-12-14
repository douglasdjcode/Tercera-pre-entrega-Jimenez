from django import forms

class MascotasFormulario(forms.Form):
    especie = forms.ChoiceField(choices=[
        ('perro', 'Perro'),
        ('gato', 'Gato'),
        ('pez', 'Pez'),
        ('ave', 'Ave'),
        ('reptil', 'Reptil'),
    ], label="Especie")
    raza = forms.CharField(max_length=100, label="Raza")
    edad = forms.IntegerField(label="Edad")

class ClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    telefono = forms.CharField(max_length=15)
    email = forms.EmailField()

class ProductoFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    precio = forms.FloatField()
    categoria = forms.CharField(max_length=50)
    descipcion = forms.TextInput()

class SucursalFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    direccion = forms.CharField(max_length=255)
    telefono = forms.CharField(max_length=20)
