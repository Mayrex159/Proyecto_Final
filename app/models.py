from distutils.command.upload import upload
from django.db import models


# Create your models here.


class TipoProducto(models.Model):
    tipo = models.CharField(max_length=25)

    def __str__(self):
        return self.tipo

    class Meta:
        db_table = 'db_tipo_producto'


class Producto(models.Model):
    codigo = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    precio = models.IntegerField()
    stock = models.IntegerField()
    descripcion = models.TextField()
    tipo = models.ForeignKey(TipoProducto, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="productos", null=True)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'db_producto'


class ImagenProducto(models.Model):
    imagen = models.ImageField(upload_to="productos")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="imagenes")



class Productos_carrito(models.Model):
    codigoCarrito = models.AutoField(primary_key=True)
    nombreProducto = models.CharField(max_length=40)
    precioProducto = models.IntegerField()
    stockProducto = models.IntegerField()
    imagen = models.ImageField(upload_to="productos_carrito", null=True)

    def __str__(self):
        return self.nombreProducto

    class Meta:
        db_table = 'db_producto_carrito'



class TipoUsuario(models.Model):
    tipo = models.CharField(max_length=25)

    def __str__(self):
        return self.tipo

    class Meta:
        db_table = 'db_tipo_usuario'


class RegistroUsuario(models.Model):
    alias_usuario = models.CharField(max_length=10, null=False, primary_key=True)
    nombre_usuario = models.CharField(null=False, max_length=20)
    apellido_usuario = models.CharField(null=False, max_length=20)
    correo_usuario = models.CharField(null=False, max_length=30)
    password = models.CharField(null=False, max_length=20 )
    repetir_password = models.CharField(null=False, max_length=20)
    tipo = models.ForeignKey(TipoUsuario, on_delete=models.PROTECT)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.apellido_usuario

    class Meta:
        db_table = 'db_registro_usuario'

class Suscripcion(models.Model):
    username = models.CharField(max_length=5, null=False, primary_key=True)
    suscripcion1 = models.BooleanField(null=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'db_suscripcion'
