from django import forms
from django .forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError


# TEMPLATE PARA EL FORMULARIO


class ProductoForm(ModelForm):


    nombre = forms.CharField(min_length=1, max_length=20)
    precio = forms.IntegerField(min_value=1, max_value=1000000)

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe = Producto.objects.filter(nombre__iexact=nombre).exists()

        if existe:
            raise ValidationError("Este nombre ya existe")

        return nombre

    class Meta:
        model = Producto
        fields = ['codigo', 'nombre', 'marca', 'precio',
                  'stock', 'descripcion', 'tipo', 'imagen']


class RegistroClienteForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    repetir_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = RegistroUsuario
        fields = ['alias_usuario', "nombre_usuario", "apellido_usuario",
                  "correo_usuario", "password", "repetir_password", "tipo"]


class UserRegistroForm(UserCreationForm):
    pass

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']
