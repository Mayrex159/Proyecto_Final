from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('index2/', index2, name="index2"),
    path('carrito/', carrito, name="carrito"),
    path('despacho/', despacho, name="despacho"),
    path('historial_compras/', historial_compras, name="historial_compras"),
    path('login/', login, name="login"),
    path('perfil_usuario/', perfil_usuario, name="perfil_usuario"),
    path('productos/', productos, name="productos"),
    path('productosapi/', productosapi, name="productosapi"),
    path('productosapiexternos/', productosapiexternos, name="productosapiexternos"),
    path('registro_clientes/', registro_clientes, name="registro_clientes"),
    path('listarClientes/', listar_clientes, name='listar_clientes'),
    path('eliminarClientes/<alias_usuario>', eliminar_cliente, name='eliminar_clientes'),
    path('modificarCliente/<alias_usuario>', modificar_clientes, name="modificar_clientes"),
    
    path('agregar/', agregar_productos, name="agregar_productos"),
    path('listar/', listar_productos, name="listar_productos"),
    path('modificar/<codigo>', modificar_productos, name="modificar_productos"),
    path('eliminar/<codigo>', eliminar_producto, name="eliminar_producto"),
    path('carrito/pagar_carrito/', pagar_carrito, name='pagar_carrito'),
    path('registro_usuarios/', registro_usuarios, name='registro_usuarios'),
]