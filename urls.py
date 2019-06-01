from django.contrib import admin
from django.urls import path
from . import views
urlpatterns =[
	path('', views.index, name='index'),
	path('mision', views.mision, name='mision'),
	path('sandwiches', views.sandwiches, name='sandwiches'),
	path('contacto', views.contacto, name='contacto'),
	path('inventario',views.inventario,name='inventario'),
	path('modificarin',views.modificarin,name='modificarin'),
	path('modificarsand',views.modificarsand,name='modificarsand'),
	path('modificar_cantidad',views.modificar_cantidad, name='modificar_cantidad'),
	path('modificar_nombre',views.modificar_nombre, name='modificar_nombre'),
	path('modificar_precio',views.modificar_precio, name='modificar_precio'),
	path('modificar_proveedor',views.modificar_proveedor, name='modificar_proveedor'),
	path('modificar_nombres',views.modificar_nombres, name='modificar_nombres'),
	path('modificar_precio',views.modificar_precio, name='modificar_precio'),
	path('modificar_descripcion',views.modificar_descripcion, name='modificar_descripcion'),
	path('pedido',views.pedido, name='pedido'),
	path('agregarpedido',views.agregarpedido, name='agregarpedido'),
	path('pedidos',views.pedidos, name='pedidos'),
	path('eliminar_ingrediente',views.eliminar_ingrediente, name='eliminar_ingrediente'),
	path('ingredientes',views.ingredientes, name='ingredientes'),
	path('agregar__ingrediente',views.agregar__ingrediente, name='agregar__ingrediente'),
	]