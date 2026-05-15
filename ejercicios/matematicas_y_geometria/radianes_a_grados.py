# ============================================================
# Conversor de radianes a grados
# ============================================================
# Este programa solicita un valor en radianes y lo convierte a
# grados utilizando el valor de pi proporcionado por el módulo math.
#
# La conversión se realiza mediante la fórmula:
# grados = radianes * 180 / pi
#
# El resultado se muestra redondeado a dos decimales para facilitar
# su lectura.
#
# Este ejercicio practica uso de módulos, operaciones matemáticas
# y presentación de resultados numéricos.
# ============================================================

import math
#Importo este modulo para poder operar con un valor mas cercano al real de pi. 
rad = float(input("Ingrese el valor en radianes como un numero racional no fraccionario: "))
#rad es una variable de entrada y auxiliar que guarda el valor ingresado en radianes. 
dg = (rad*180)/math.pi
#Esta es una operacion para pasar el valor de radianes a grados y el resultado se almacena en la variable auxiliar dg. 
print ("El valor ingresado al pasarlo a grados es aproximadamente: ", round(dg,2))
#Se imprime el valor de la variable dg como dato de salida. Este valor se redondea con la funcion round a dos decimales porque podria llegar a tener mas.

