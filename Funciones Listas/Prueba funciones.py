#Pruebas. 
#Prueba countelement.
from funciones import countelement
print("Prueba countelement:")
print("Cuantas veces esta el 2")
arroz = [2,3,2,2,3,2,222,241413,2,634]
print("Lista:", arroz)
a5 = countelement(arroz,2)
print("El numero esta",a5,"veces.")
#Prueba insertelement.
from funciones import insertelement
print("Prueba insertelement:")
print("Se agrega el 0 en la segunda posicion.")
lista1 = [1, 2, 3,4,5,6,7]
print("Lista:", lista1)
insertelement(lista1, 1, 0)
print(lista1)
#Prueba addlist.
from funciones import addlist
print("Prueba addlist:")
lista1 = [1, 2, 3]
print("Lista:", lista1)
lista2 = [4, 5, 6]
print("Lista:", lista2)
addlist(lista1, lista2)
print(lista1)
#Prueba deletelement.
from funciones import deletelement
print("Prueba deletelement:")
bebe = ["No se", "si", "no", "puede pasar", "no", "JAJAJAJAJAJA", "ammmmm", "tiamo", 4]
print("Lista:", bebe)
deletelement(bebe,"no")
print("Se elimina 'no'.")
print(bebe)
bebe = ["No se", "si", "no", "puede pasar", "no", "JAJAJAJAJAJA", "ammmmm", "tiamo", 4]
print("Prueba deletelement 2.")
deletelement(bebe,4)
print("Se elimina el 4.")
print(bebe)
#Prueba posicion.
from funciones import posicion
print("Prueba posicion:")
bebe = ["No se", "si", "no", "puede pasar", "no", "JAJAJAJAJAJA", "ammmmm", "tiamo", 4]
print("Lista:", bebe)
a = posicion("tiamo",bebe)
print("Posicion tiamo es:",a)
#Prueba deletebyposition.
from funciones import deletebyposition
print("Prueba deletebyposition:")
bebe = ["No se", "si", "no", "puede pasar", "no", "JAJAJAJAJAJA", "ammmmm", "tiamo", 4]
print("Lista:", bebe)
deletebyposition(bebe,6)
print("Se elimina la posicion 6 y queda:",bebe)
#Prueba invertirlista.
from funciones import invertirlista
print("Prueba invertirlista:")
numeros = [0,1,2,3,4]
print("Lista:", numeros)
invertida = invertirlista(numeros)
print(invertida)
#Prueba printlist.
from funciones import printlist
print("Prueba printlist:")
lista = ["Rato","Beba","Ninikin",4,10,"Chuspita","Yo"]
print("Lista:",lista)
printlist(lista)
#Prueba printlist2.
from funciones import printlist2
print("Prueba printlist2:")
lista = ["Rato","Beba","Ninikin",4,10,"Chuspita","Yo"]
print("Lista:",lista)
printlist2(lista)
#Prueba printlistnum.
from funciones import printlistnum
print("Prueba printlistnum:")
lista = ["Rato","Beba","Ninikin",4,10,"Chuspita","Yo"]
print("Lista:",lista)
printlistnum(lista)
