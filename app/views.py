from pickle import TRUE
import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *


# Create your views here.


def index(request):
    return render(request, 'app/index.html')


@login_required
def index2(request):
    return render(request, 'app/index2.html')


@login_required
def carrito(request):
    discount = 0.0

    carrito = Productos_carrito.objects.all().raw(
        "SELECT codigoCarrito, nombreProducto, CAST(COUNT(nombreProducto) AS INT) AS cantidad, CAST(sum(precioProducto) AS FLOAT) AS montoTotal FROM db_producto_carrito GROUP BY nombreProducto")
    datos = {
        'listaCarrito': carrito,
        'subTotal': round(sum(c.montoTotal for c in carrito)),

        'descuento': round(sum(c.montoTotal*0.05 for c in carrito)),
        'TotalaPagar': round(sum(c.montoTotal - c.montoTotal*0.05 for c in carrito)),
    }
    return render(request, 'app/carrito.html', datos)


@login_required
def despacho(request):
    return render(request, 'app/despacho.html')


@login_required
def historial_compras(request):
    return render(request, 'app/historial_compras.html')


def login(request):
    return render(request, 'registration/login.html')


@login_required
def perfil_usuario(request):

    productos = Producto.objects.all()
    datos = {
        'productos': productos
    }

    return render(request, 'app/perfil_usuario.html', datos)


@login_required
def productos(request):
    productos = Producto.objects.all()
    datos = {
        'productos': productos,
    }

    if request.method == 'POST':
        if request.POST.get('btnAccion') == 'suscripcion':

            suscripcion = Suscripcion()
            suscripcion.username = request.POST.get('usuario')
            suscripcion.suscripcion1 = request.POST.get('suscripcion1')
            suscripcion.save()

        else:
            carrito = Productos_carrito()
            carrito.nombreProducto = request.POST.get('nombreProducto')
            carrito.precioProducto = request.POST.get('precioProducto')
            carrito.stockProducto = request.POST.get('stockProducto')
            carrito.imagen = request.POST.get('imagen')
            carrito.save()

            codigoProd = request.POST.get('codigoProducto')
            producto = Producto.objects.get(codigo=codigoProd)
            producto.stock -= 1
            producto.save()

    return render(request, 'app/productos.html', datos)


@login_required
def productosapi(request):
    response = requests.get('http://127.0.0.1:8000/api/producto/').json()
    datos = {
        'listaJson': response
    }
    return render(request, 'app/productosapi.html', datos)


@login_required
def productosapiexternos(request):
    response2 = requests.get(
        'https://attackontitanapi.herokuapp.com/api/titans').json()
    response3 = requests.get(
        'https://attackontitanapi.herokuapp.com/api/characters').json()
    datos = {
        'listaShingekyTitans': response2,
        'listaShingeky': response3
    }
    return render(request, 'app/productosapiexternos.html', datos)

# SECCION AGREGAR CLIENTES


@login_required
def registro_clientes(request):
    datos = {
        'form': RegistroClienteForm()
    }
    if request.method == 'POST':
        formulario = RegistroClienteForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Usuario Registrado con éxito!")
            return redirect(to="login")
        else:
            datos['form'] = formulario

    return render(request, 'registration/registro_clientes.html', datos)

# SECCION LISTAR CLIENTES


@login_required
def listar_clientes(request):
    clientesAll = RegistroUsuario.objects.all()
    datos = {
        'listarClientes': clientesAll}
    return render(request, 'registration/listar_clientes.html', datos)

# SECCION ELIMINAR CLIENTES


@login_required
def eliminar_cliente(request, alias_usuario):
    print('eliminar_cliente')
    print(alias_usuario)
    cliente = get_object_or_404(RegistroUsuario, alias_usuario=alias_usuario)
    cliente.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listar_clientes")

# SECCION MODIFICAR CLIENTES


@login_required
def modificar_clientes(request, alias_usuario):
    cliente = get_object_or_404(RegistroUsuario, alias_usuario=alias_usuario)
    datos = {
        'form1': RegistroClienteForm(instance=cliente)
    }
    if request.method == 'POST':
        formulario = RegistroClienteForm(
            request.POST, files=request.FILES, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listar_clientes")
        datos['form1'] = formulario
    return render(request, 'registration/modificar_clientes.html', datos)

# SECCION AGREGAR PRODUCTOS


@permission_required('app.add_producto')
def agregar_productos(request):
    datos = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto registrado")
            return redirect(to="listar_productos")
        else:
            datos['form'] = formulario

    return render(request, 'app/productos/agregar_productos.html', datos)

# SECCION LISTAR PRODUCTOS


@permission_required('app.view_producto')
def listar_productos(request):
    productoAll = Producto.objects.all()
    datos = {
        'listarProductos': productoAll}
    return render(request, 'app/productos/listar_productos.html', datos)

# SECCION PARA MODIFICAR PRODUCTOS


@permission_required('app.change_producto')
def modificar_productos(request, codigo):
    producto = get_object_or_404(Producto, codigo=codigo)
    datos = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(
            request.POST, files=request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listar_productos")
        datos['form'] = formulario
    return render(request, 'app/productos/modificar_productos.html', datos)

# SECCION PARA ELIMINAR PRODUCTOS


@permission_required('app.delete_producto')
def eliminar_producto(request, codigo):
    producto = get_object_or_404(Producto, codigo=codigo)
    producto.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listar_productos")

# SECCION PAGO DE CARRITO


def pagar_carrito(request):
    Productos_carrito.objects.all().delete()
    messages.success(request, "Pago Realizado Exitosamente!!")
    return redirect(to="carrito")


def registro_usuarios(request):
    datos = {
        'form': UserRegistroForm()
    }
    if request.method == 'POST':
        formulario = UserRegistroForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registrado correctamente!")
            return redirect(to='login')
        datos["form"] = formulario

    return render(request, 'registration/registro_usuarios.html', datos)
