#Hugo Esteban Barrero Garci­a 
#Grupo 4
#Haga un algoritmo que convierta de radianes a grados.
#Ejemplo1: rad = 6.982, ese valor es de aproximadamente 400 grados.
#Ejemplo2: rad = 6.283, ese valor es de aproximadamente 360 grados. 
import math
#Importo este modulo para poder operar con un valor mas cercano al real de pi. 
rad = float(input("Ingrese el valor en radianes como un numero racional no fraccionario: "))
#rad es una variable de entrada y auxiliar que guarda el valor ingresado en radianes. 
dg = (rad*180)/math.pi
#Esta es una operacion para pasar el valor de radianes a grados y el resultado se almacena en la variable auxiliar dg. 
print ("El valor ingresado al pasarlo a grados es aproximadamente: ", round(dg,2))
#Se imprime el valor de la variable dg como dato de salida. Este valor se redondea con la funcion round a dos decimales porque podria llegar a tener mas.

