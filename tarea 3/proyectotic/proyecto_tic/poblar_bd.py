from olivo.models import *
###
##proveedores
proveedor1 = Proveedores(direccion= "José Francisco Vergara 007, Quilicura",
                         nombre="Panaderia Quilicura",
                         telefono=5697523455)
proveedor1.save()
proveedor2 = Proveedores(direccion= "Antonia López de Bello 743",
                         nombre="Local de la vega",
                         telefono=27376161)
proveedor2.save()
proveedor3 = Proveedores(direccion= "21 de Mayo 819, Santiago",
                         nombre="Mayotista 10",
                         telefono=6006000025)
proveedor3.save()
proveedor4 = Proveedores(direccion="Artesanos 711, Recoleta",
                         nombre="Dona carne",
                         telefono=9454347565)
proveedor4.save()
###
##ingredientes
##cantidad y precio es por kilo /exepto los huevos,lechuga y hamburguesa de lenteja que es por unidad
## ejemplo preciocompre= 200 costo 200 el kilo, cantidaddisponible=10 20kilos disponibles
## nos dijeron que 1 kilo de pan ciabatta es 8 panes aprox
carne = Ingredientes(nombre="carne",
                            preciocompra=5490,
                            cantidaddisponible=10,
                            proveedor=proveedor4)
carne.save()
pollo = Ingredientes(nombre="pollo",
                            preciocompra=4986,
                            cantidaddisponible=10,
                            proveedor=proveedor4)
pollo.save()
hamburguesa = Ingredientes(nombre="hamburguesa lenteja",
                            preciocompra=290,
                            cantidaddisponible=100,
                            proveedor=proveedor2)
hamburguesa.save()
pan = Ingredientes(nombre="pan ciabatta",
                            preciocompra=2190,
                            cantidaddisponible=10,
                            proveedor=proveedor1)
pan.save()
papashilo = Ingredientes(nombre="papas hilo",
                            preciocompra=5139,
                            cantidaddisponible=10,
                            proveedor=proveedor3)
papashilo.save()
rucula = Ingredientes(nombre="rucula",
                            preciocompra=9500,
                            cantidaddisponible=2,
                            proveedor=proveedor2)
rucula.save()
palta = Ingredientes(nombre="palta",
                            preciocompra=3190,
                            cantidaddisponible=2,
                            proveedor=proveedor2)
palta.save()
lechuga = Ingredientes(nombre="lechuga",
                            preciocompra=790,
                            cantidaddisponible=10,
                            proveedor=proveedor2)
lechuga.save()
cebolla = Ingredientes(nombre="cebolla",
                            preciocompra=530,
                            cantidaddisponible=5,
                            proveedor=proveedor2)
cebolla.save()
huevomayonesa = Ingredientes(nombre="huevo para mayonesa",
                            preciocompra=80,
                            cantidaddisponible=100,
                            proveedor=proveedor2)
huevomayonesa.save()
champinon = Ingredientes(nombre="champinon",
                            preciocompra=5800,
                            cantidaddisponible=2,
                            proveedor=proveedor2)
champinon.save()
							
###
##Sanwiches
carnes = Sandwiches(nombre="Carne al ajillo",
                         precio=1500,
                         descripcion="Rico sanwich con carne al ajillo,  con verduras y una rica mayonesa casera",
                         vegetarianocarne="carne")
carnes.save()
pollos = Sandwiches(nombre="Pollo a la peruana",
                         precio=1500,
                         descripcion="Rico sanwich de pasta de pollo a la peruana con papas hilo y lechuga",
                         vegetarianocarne="carne")
pollos.save()
lenteja = Sandwiches(nombre="vegetariano",
                         precio=1500,
                         descripcion="Rico sandwich de hamburguesa de lentejas, con verduras y salsa acevichada ",
                         vegetarianocarne="vegetariano")
lenteja.save()

###
##Ingredientes_sandwiches
ingredientes_sandwiches1=Ingredientes_Sandwiches(ingredientes=hamburguesa,
                                                 sandwiches=lenteja,
                                                 cantidad=1)
ingredientes_sandwiches1.save()
ingredientes_sandwiches2=Ingredientes_Sandwiches(ingredientes=champinon,
                                                 sandwiches=lenteja,
                                                 cantidad=0.2)
ingredientes_sandwiches2.save()
ingredientes_sandwiches3=Ingredientes_Sandwiches(ingredientes=palta,
                                                 sandwiches=lenteja,
                                                 cantidad=0.15)
ingredientes_sandwiches3.save()
ingredientes_sandwiches4=Ingredientes_Sandwiches(ingredientes=rucula,
                                                 sandwiches=lenteja,
                                                 cantidad=0.2)
ingredientes_sandwiches4.save()
ingredientes_sandwiches5=Ingredientes_Sandwiches(ingredientes=pollo,
                                                 sandwiches=pollos,
                                                 cantidad=0.25)
ingredientes_sandwiches5.save()
ingredientes_sandwiches6=Ingredientes_Sandwiches(ingredientes=papashilo,
                                                 sandwiches=pollos,
                                                 cantidad=0.15)
ingredientes_sandwiches6.save()
ingredientes_sandwiches7=Ingredientes_Sandwiches(ingredientes=lechuga,
                                                 sandwiches=pollos,
                                                 cantidad=0.2)
ingredientes_sandwiches7.save()
ingredientes_sandwiches8=Ingredientes_Sandwiches(ingredientes=rucula,
                                                 sandwiches=carnes,
                                                 cantidad=0.2)
ingredientes_sandwiches8.save()
ingredientes_sandwiches9=Ingredientes_Sandwiches(ingredientes=palta,
                                                 sandwiches=carnes,
                                                 cantidad=0.15)
ingredientes_sandwiches9.save()
ingredientes_sandwiches10=Ingredientes_Sandwiches(ingredientes=cebolla,
                                                 sandwiches=carnes,
                                                 cantidad=0.15)
ingredientes_sandwiches10.save()
ingredientes_sandwiches11=Ingredientes_Sandwiches(ingredientes=huevomayonesa,
                                                 sandwiches=carnes,
                                                 cantidad=1)
ingredientes_sandwiches11.save()
ingredientes_sandwiches12=Ingredientes_Sandwiches(ingredientes=pan,
												sandwiches=carnes,
												cantidad=0.125)
ingredientes_sandwiches12.save()
ingredientes_sandwiches13=Ingredientes_Sandwiches(ingredientes=pan,
												sandwiches=pollos,
												cantidad=0.125)
ingredientes_sandwiches13.save()
ingredientes_sandwiches14=Ingredientes_Sandwiches(ingredientes=pan,
												sandwiches=lenteja,
												cantidad=0.125)
ingredientes_sandwiches14.save()
###
##ClientePresencial
clientepresencial1=ClientePresencial(lugarcompra="Mall plaza Egana")
clientepresencial1.save()
clientepresencial2=ClientePresencial(lugarcompra="Parque Los Reyes")
clientepresencial2.save()
clientepresencial3=ClientePresencial(lugarcompra="Parque Los Reyes")
clientepresencial3.save()
clientepresencial4=ClientePresencial(lugarcompra="Parque Los Reyes")
clientepresencial4.save()
clientepresencial5=ClientePresencial(lugarcompra="Mall plaza Egana")
clientepresencial5.save()
clientepresencial6=ClientePresencial(lugarcompra="Mall plaza Egana")
clientepresencial6.save()
clientepresencial7=ClientePresencial(lugarcompra="Parque Los Reyes")
clientepresencial7.save()
clientepresencial8=ClientePresencial(lugarcompra="Mall plaza Egana")
clientepresencial8.save()
clientepresencial9=ClientePresencial(lugarcompra="Parque Los Reyes")
clientepresencial9.save()
clientepresencial10=ClientePresencial(lugarcompra="Mall plaza Egana")
clientepresencial10.save()

###
##Sandwiches_ClientePresencial
sandwiches_clientePresencial1= Sandwiches_ClientePresencial(clientepresencial=clientepresencial1,
                                                            sandwiches=pollos,
                                                            cantidad=3)
sandwiches_clientePresencial1.save()
sandwiches_clientePresencial2= Sandwiches_ClientePresencial(clientepresencial=clientepresencial1,
                                                            sandwiches=carnes,
                                                            cantidad=2)
sandwiches_clientePresencial2.save()
sandwiches_clientePresencial3= Sandwiches_ClientePresencial(clientepresencial=clientepresencial2,
                                                            sandwiches=lenteja,
                                                            cantidad=1)
sandwiches_clientePresencial3.save()
sandwiches_clientePresencial4= Sandwiches_ClientePresencial(clientepresencial=clientepresencial3,
                                                            sandwiches=pollos,
                                                            cantidad=1)
sandwiches_clientePresencial4.save()
sandwiches_clientePresencial5= Sandwiches_ClientePresencial(clientepresencial=clientepresencial4,
                                                            sandwiches=lenteja,
                                                            cantidad=2)
sandwiches_clientePresencial5.save()
sandwiches_clientePresencial6= Sandwiches_ClientePresencial(clientepresencial=clientepresencial5,
                                                            sandwiches=carnes,
                                                            cantidad=1)
sandwiches_clientePresencial6.save()
sandwiches_clientePresencial7= Sandwiches_ClientePresencial(clientepresencial=clientepresencial6,
                                                            sandwiches=lenteja,
                                                            cantidad=1)
sandwiches_clientePresencial7.save()
sandwiches_clientePresencial8= Sandwiches_ClientePresencial(clientepresencial=clientepresencial6,
                                                            sandwiches=pollos,
                                                            cantidad=1)
sandwiches_clientePresencial8.save()
sandwiches_clientePresencial9= Sandwiches_ClientePresencial(clientepresencial=clientepresencial7,
                                                            sandwiches=carnes,
                                                            cantidad=1)
sandwiches_clientePresencial9.save()
sandwiches_clientePresencial10= Sandwiches_ClientePresencial(clientepresencial=clientepresencial8,
                                                            sandwiches=carnes,
                                                            cantidad=2)
sandwiches_clientePresencial10.save()
sandwiches_clientePresencial11= Sandwiches_ClientePresencial(clientepresencial=clientepresencial9,
                                                            sandwiches=pollos,
                                                            cantidad=2)
sandwiches_clientePresencial11.save()
sandwiches_clientePresencial12= Sandwiches_ClientePresencial(clientepresencial=clientepresencial10,
                                                            sandwiches=carnes,
                                                            cantidad=2)
sandwiches_clientePresencial12.save()
###
##clientepedido
clientepedido1= ClientePedido(nombre="Diego Lopez",
                              telefono=56964644243,
                              correo="diego@gmail.com")
clientepedido1.save()
clientepedido2= ClientePedido(nombre="codelco",
                              telefono=56934578765,
                              correo="codelco@gmail.com")
clientepedido2.save()
clientepedido3= ClientePedido(nombre="paris",
                              telefono=56937583849,
                              correo="paris@gmail.com")
clientepedido3.save()
clientepedido4= ClientePedido(nombre="ripley",
                              telefono=56990238023,
                              correo="ripley@gmail.com")
clientepedido4.save()
clientepedido5= ClientePedido(nombre="la polar",
                              telefono=56975431369,
                              correo="lapolar@gmail.com")
clientepedido5.save()
clientepedido6= ClientePedido(nombre="pc factory",
                              telefono=56936580900,
                              correo="pcfactory@gmail.com")
clientepedido6.save()
clientepedido7= ClientePedido(nombre="Camanchaca",
                              telefono=56955883941,
                              correo="camanchaca@gmail.com")
clientepedido7.save()
clientepedido8= ClientePedido(nombre="lippi",
                              telefono=56953628194,
                              correo="lippi@gmail.com")
clientepedido8.save()
clientepedido9= ClientePedido(nombre="gasco",
                              telefono=56965779904,
                              correo="gasco@gmail.com")
clientepedido9.save()
clientepedido10= ClientePedido(nombre="Angrosuper",
                              telefono=56934564564,
                              correo="agrosuper@gmail.com")
clientepedido10.save()

###
##Pedido
pedido1= Pedido(lugar="Mall Plaza Egana",
                fechaentrega="2019-05-10",
                clientepedido=clientepedido1)
pedido1.save()
pedido2= Pedido(lugar="Mall Plaza Egana",
                fechaentrega="2019-05-20",
                clientepedido=clientepedido2)
pedido2.save()
pedido3= Pedido(lugar="Mall Plaza Egana",
                fechaentrega="2019-05-20",
                clientepedido=clientepedido2)
pedido3.save()
pedido4= Pedido(lugar="Mall Plaza Egana",
                fechaentrega="2019-05-26",
                clientepedido=clientepedido3)
pedido4.save()
pedido5= Pedido(lugar="Mall Plaza Egana",
                fechaentrega="2019-05-29",
                clientepedido=clientepedido4)
pedido5.save()
pedido6= Pedido(lugar=" Movistar Arena",
                fechaentrega="2019-05-14",
                clientepedido=clientepedido5)
pedido6.save()
pedido7= Pedido(lugar="Cerro Santa Lucia",
                fechaentrega="2019-05-18",
                clientepedido=clientepedido6)
pedido7.save()
pedido8= Pedido(lugar="Cerro San Cristobal",
                fechaentrega="2019-05-20",
                clientepedido=clientepedido7)
pedido8.save()
pedido9= Pedido(lugar="Alto Las Condes",
                fechaentrega="2019-05-23",
                clientepedido=clientepedido8)
pedido9.save()
pedido10= Pedido(lugar="Estadio Nacional",
                fechaentrega="2019-05-20",
                clientepedido=clientepedido8)
pedido10.save()
pedido11= Pedido(lugar="Estadio Monumental",
                fechaentrega="2019-05-26",
                clientepedido=clientepedido9)
pedido11.save()
pedido12= Pedido(lugar="Costanera Center",
                fechaentrega="2019-05-21",
                clientepedido=clientepedido10)
pedido12.save()
###
##Sandwiches_Pedido
sandwiches_pedido1= Sandwiches_Pedido(pedido=pedido1,
                                      sandwiches=carnes,
                                      cantidad=40, entregado= False)
sandwiches_pedido1.save()
sandwiches_pedido2= Sandwiches_Pedido(pedido=pedido1,
                                      sandwiches=pollos,
                                      cantidad=50, entregado= False)
sandwiches_pedido2.save()
sandwiches_pedido3= Sandwiches_Pedido(pedido=pedido2,
                                      sandwiches=pollos,
                                      cantidad=60, entregado= False)
sandwiches_pedido3.save()
sandwiches_pedido4= Sandwiches_Pedido(pedido=pedido3,
                                      sandwiches=lenteja,
                                      cantidad=20, entregado= False)
sandwiches_pedido4.save()
sandwiches_pedido5= Sandwiches_Pedido(pedido=pedido3,
                                      sandwiches=carnes,
                                      cantidad=15, entregado= False)
sandwiches_pedido5.save()
sandwiches_pedido6= Sandwiches_Pedido(pedido=pedido4,
                                      sandwiches=lenteja,
                                      cantidad=20, entregado= False)
sandwiches_pedido6.save()
sandwiches_pedido7= Sandwiches_Pedido(pedido=pedido5,
                                      sandwiches=pollos,
                                      cantidad=30, entregado= False)
sandwiches_pedido7.save()
sandwiches_pedido8= Sandwiches_Pedido(pedido=pedido6,
                                      sandwiches=carnes,
                                      cantidad=60, entregado= False)
sandwiches_pedido8.save()
sandwiches_pedido9= Sandwiches_Pedido(pedido=pedido7,
                                      sandwiches=lenteja,
                                      cantidad=90, entregado= False)
sandwiches_pedido9.save()
sandwiches_pedido10= Sandwiches_Pedido(pedido=pedido8,
                                      sandwiches=pollos,
                                      cantidad=12, entregado= False)
sandwiches_pedido10.save()
sandwiches_pedido11= Sandwiches_Pedido(pedido=pedido9,
                                      sandwiches=carnes,
                                      cantidad=10, entregado= False)
sandwiches_pedido11.save()
sandwiches_pedido12= Sandwiches_Pedido(pedido=pedido10,
                                      sandwiches=lenteja,
                                      cantidad=20, entregado= True)
sandwiches_pedido12.save()
sandwiches_pedido13= Sandwiches_Pedido(pedido=pedido10,
                                      sandwiches=carnes,
                                      cantidad=20, entregado= True)
sandwiches_pedido13.save()
sandwiches_pedido14= Sandwiches_Pedido(pedido=pedido10,
                                      sandwiches=pollos,
                                      cantidad=20, entregado= True)
sandwiches_pedido14.save()
sandwiches_pedido15= Sandwiches_Pedido(pedido=pedido11,
                                      sandwiches=pollos,
                                      cantidad=30, entregado= True)
sandwiches_pedido15.save()
sandwiches_pedido16= Sandwiches_Pedido(pedido=pedido11,
                                      sandwiches=lenteja,
                                      cantidad=10, entregado=True)
sandwiches_pedido16.save()
sandwiches_pedido17= Sandwiches_Pedido(pedido=pedido12,
                                      sandwiches=carnes,
                                      cantidad=10, entregado= True)
sandwiches_pedido17.save()
sandwiches_pedido18= Sandwiches_Pedido(pedido=pedido12,
                                      sandwiches=pollos,
                                      cantidad=34, entregado= True)
sandwiches_pedido18.save()

###




