# ============================================================
# Cálculo de volumen y material de una caneca cilíndrica
# ============================================================
# Este programa solicita la altura y el radio de una caneca con
# forma cilíndrica para calcular:
#
# - El volumen que puede almacenar.
# - La cantidad aproximada de material necesaria para cubrirla.
#
# Para realizar estos cálculos se utilizan fórmulas geométricas
# relacionadas con el cilindro y el valor de pi del módulo math.
#
# También se revisa que las medidas ingresadas no sean negativas.
# Este ejercicio practica fórmulas matemáticas, uso de módulos,
# condicionales y redondeo de resultados.
# ============================================================

import math
#Importo este modulo para poder operar con un valor mas cercano al real de pi. 
h = float(input("Para hallar el valor que puede almanenar una caneca ingrese su altura en metros como un racional no fraccionario "))
#h es una variable de entrada y auxiliar que guarda el valor ingresado de la altura. 
r = float(input("Ahora ingrese el radio de la tapa en metros como un racional positivo no fraccionario ")) 
#r es una variable de entrada y auxiliar que guarda el valor ingresado del radio. 
if (h < 0 or r < 0  ):
    print("Las medidas no tienen un valor negativo")
    h = float(input("Para hallar el valor que puede almanenar una caneca ingrese su altura en metros como un racional no fraccionario"))
    #Esto es en caso que se lleguen a ingresar valores negativos. 
vol = math.pi*(r**2)*h
#Ahora se halla el volumen con esa operacion y se denomina con la variable auxiliar: vol. 
mat = (2*math.pi*r*h)+(2*math.pi*r**2)
#Ahora se halla la cantidad de material necesario con esa operacion y se denomina con la variable auxiliar: mat. 
print("Segun los valores ingresados:")
print('El material necesario para cubrir la caneca es de ', round(mat,3), ' metros cubicos')
#Se imprime el valor de la variable mat como dato de salida. Este valor se redondea con la funcion round a 3 decimales porque podria llegar a tener mas.
print('Y la caneca puede almacenar ', round(vol,3), ' litros')
#Se imprime el valor de la variable vol como dato de salida. Este valor se redondea con la funcion round a 3 decimales porque podria llegar a tener mas.
