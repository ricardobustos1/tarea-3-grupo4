from django.db import models

# Create your models here.
class Proveedores(models.Model):
	direccion=models.CharField(max_length=512)
	nombre=models.CharField(max_length=30)
	telefono=models.IntegerField()

class Ingredientes(models.Model):
	nombre=models.CharField(max_length=30)
	preciocompra=models.IntegerField()
	cantidaddisponible=models.IntegerField()
	proveedor=models.ForeignKey(Proveedores,on_delete=models.CASCADE)
	
	
class Sandwiches(models.Model):
	nombre=models.CharField(max_length=30)
	precio=models.IntegerField()
	descripcion=models.CharField(max_length=512)
	vegetarianocarne=models.CharField(max_length=30)




class Ingredientes_Sandwiches(models.Model):
        ingredientes=models.ForeignKey(Ingredientes,on_delete=models.CASCADE)
        sandwiches=models.ForeignKey(Sandwiches,on_delete=models.CASCADE)
        cantidad=models.FloatField()


class ClientePresencial(models.Model):
        lugarcompra=models.CharField(max_length=30)
		
class Sandwiches_ClientePresencial(models.Model):
		sandwiches=models.ForeignKey(Sandwiches,on_delete=models.CASCADE)
		clientepresencial=models.ForeignKey(ClientePresencial,on_delete=models.CASCADE)
		cantidad=models.IntegerField()


class ClientePedido(models.Model):
        nombre=models.CharField(max_length=30)
        telefono=models.IntegerField()
        correo=models.CharField(max_length=30)

class Pedido(models.Model):
        lugar=models.CharField(max_length=30)
        fechaentrega=models.DateField()
        clientepedido=models.ForeignKey(ClientePedido,on_delete=models.CASCADE)

class Sandwiches_Pedido(models.Model):
		pedido=models.ForeignKey(Pedido,on_delete=models.CASCADE)
		sandwiches=models.ForeignKey(Sandwiches,on_delete=models.CASCADE)
		cantidad=models.IntegerField()
		entregado=models.BooleanField(default=False)

