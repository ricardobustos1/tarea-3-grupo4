from django.shortcuts import render
from .models import *
def index(request):
	return render(request, 'olivo/index.html')
def contacto(request):
	contexto={}
	contexto['ingredientes'] = Ingredientes.objects.all()
	return render(request, 'olivo/contacto.html',contexto)

def ingredientes(request):
	return render(request, 'olivo/ingredientes.html')
def mision(request):
	return render(request, 'olivo/mision.html')
def pedido(request):
	return render(request, 'olivo/pedido.html')

def pedidos(request):
	contexto={}
	contexto['todospedidos'] = Sandwiches_Pedido.objects.all()
	return render(request, 'olivo/pedidos.html',contexto)
	
def sandwiches(request):
	contexto={}
	contexto['sandwiches'] = Sandwiches.objects.all()
	return render(request, 'olivo/sandwiches.html',contexto)
	
def inventario(request):
	contexto={}
	contexto['ingredientes'] = Ingredientes.objects.all()
	return render(request, 'olivo/inventario.html',contexto)
	
def modificarin(request):
	return render(request, 'olivo/modificarin.html')
	
def modificarsand(request):
	return render(request, 'olivo/modificarsand.html')
	
def modificar_cantidad(request):
	aa= request.POST['nombre_estudiante']
	xx=request.POST['nueva_cantidad']
	zz=Ingredientes.objects.get(nombre=aa)
	zz.cantidaddisponible=xx
	zz.save()
	return render(request, 'olivo/bueno.html')

def modificar_nombre(request):
	aa= request.POST['nombre_estudiante']
	xx=request.POST['nuevo_nombre']
	zz=Ingredientes.objects.get(nombre=aa)
	zz.nombre=xx
	zz.save()
	return render(request, 'olivo/bueno.html')
	
def modificar_precio(request):
	aa= request.POST['nombre_estudiante']
	xx=request.POST['nuevo_precio']
	zz=Ingredientes.objects.get(nombre=aa)
	zz.preciocompra=xx
	zz.save()
	return render(request, 'olivo/bueno.html')
	
def modificar_proveedor(request):
	aa= request.POST['nombre_estudiante']
	xx=Proveedores.objects.get(nombre=request.POST['nuevo_proveedor'])
	zz=Ingredientes.objects.get(nombre=aa)
	zz.proveedor=xx
	zz.save()
	return render(request, 'olivo/bueno.html')
	
def modificar_nombres(request):
	aa= request.POST['nombre_sandwichs']
	xx=request.POST['nuevo_nombre']
	zz=Sandwiches.objects.get(nombre=aa)
	zz.nombre=xx
	zz.save()
	return render(request, 'olivo/bueno.html')
	
def modificar_precio(request):
	aa= request.POST['nombre_sandwichs']
	xx=request.POST['nuevo_precio']
	zz=Sandwiches.objects.get(nombre=aa)
	zz.precio=xx
	zz.save()
	return render(request, 'olivo/bueno.html')
	
def modificar_descripcion(request):
	aa= request.POST['nombre_sandwichs']
	xx=request.POST['nueva_descripcion']
	zz=Sandwiches.objects.get(nombre=aa)
	zz.descripcion=xx
	zz.save()
	return render(request, 'olivo/bueno.html')

def agregarpedido(request):
	nombre= request.POST['nombre_solicitante']
	cel= request.POST['celular']
	email= request.POST['correo']
	entrega= request.POST['fecha']
	donde= request.POST['lugar']
	sand1= request.POST['c1']
	sand2= request.POST['c2']
	sand3= request.POST['c3']
	carnes=Sandwiches.objects.get(nombre="Carne al ajillo")
	pollos=Sandwiches.objects.get(nombre="Pollo a la peruana")
	lenteja=Sandwiches.objects.get(nombre="vegetariano")
	nuevo = ClientePedido(nombre=nombre, telefono= cel, correo = email)
	nuevo.save()
	nuevop = Pedido(lugar=donde, fechaentrega=entrega, clientepedido= nuevo)
	nuevop.save()
	ww=Sandwiches_Pedido(pedido=nuevop, sandwiches=carnes, cantidad=sand1)
	ww.save()
	ww1=Sandwiches_Pedido(pedido=nuevop, sandwiches=pollos, cantidad=sand2)
	ww1.save()
	ww2=Sandwiches_Pedido(pedido=nuevop, sandwiches=lenteja, cantidad=sand3)
	ww2.save()
	return render(request, 'olivo/bueno.html')

def todospedidos(request):
	contexto={}
	contexto['todospedidos'] = Sandwiches_Pedido.objects.all()
	return render(request, 'olivo/pedidos.html',contexto)
	
def eliminar_ingrediente(request):
	aa= request.POST['nombre_sandwichs']
	zz=Ingredientes.objects.get(nombre=aa)
	zz.delete()
	return render(request, 'olivo/bueno.html')	

def agregar__ingrediente(request):
	aa= request.POST['nombre']
	xx=request.POST['precio']
	aaa= request.POST['cantidad']
	xxx=request.POST['proveedor']
	zz=Proveedores.objects.get(nombre=xxx)
	ee= Ingredientes(nombre=aa, preciocompra=xx, cantidaddisponible=aaa, proveedor=zz)
	ee.save()
	return render(request, 'olivo/bueno.html')	
# Create your views here.

