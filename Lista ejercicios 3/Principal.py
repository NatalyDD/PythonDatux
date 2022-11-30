from ejercicio1 import *
r1=Profesor("Leonardo","Perez","16467979","456138792")
print(r1)

from ejercicio2 import *
p=Producto("bujia","BOSCH","DGHJIU-15")
p1=Producto("espejo","NSK","ASDO-4SD")
p2=Producto("manija","FESTO","4578/SD")
c1=Catalogo(p)
c1.agregar(p1)
c1.agregar(p2)
print("A continuación, se muestra la lista de productos:")
c1.mostrar()

from ejercicio3 import *
s1=Perro("terrestre","caninos","perro")
s1.sonido()
s2=Gato("terrestre","felinos","gato")
s2.sonido()

import ejercicio4
ejercicio4.problibreria()

import ejercicio5
ejercicio5.obtener_nom_archivo()

import ejercicio6
ejercicio6.genenumale()

import ejercicio7
ejercicio7.consultapdolar()

from ejercicio8 import *
busca()

from ejercicio9 import *
buscaocurrencias("python")