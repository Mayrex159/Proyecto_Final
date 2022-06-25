from django.contrib import admin
from .models import *
from .forms import *

# Register your models here.

class ImagenProductoAdmin(admin.TabularInline):
    model = ImagenProducto


class ProductosAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre','marca','precio','stock','descripcion','tipo','imagen','create_at','update_at']
    list_filter = ['tipo','create_at']
    search_fields = ['codigo']
    list_per_page = 5
    inlines = [
        ImagenProductoAdmin
    ]



class Productos_carritoAdmin(admin.ModelAdmin):
    list_display = ['codigoCarrito','nombreProducto','precioProducto','stockProducto','imagen']
    search_fields = ['nombreProducto']
    list_per_page = 5

class RegistroUsuarioAdmin(admin.ModelAdmin):
    list_display = ['alias_usuario','nombre_usuario','apellido_usuario','correo_usuario', 'password', 'repetir_password', 'tipo', 'create_at','update_at']
    list_filter = ['tipo']
    search_fields = ['alias_usuario']
    list_per_page = 5



admin.site.register(TipoProducto)
admin.site.register(Producto,ProductosAdmin)
admin.site.register(Productos_carrito, Productos_carritoAdmin)
admin.site.register(TipoUsuario)
admin.site.register(RegistroUsuario, RegistroUsuarioAdmin)