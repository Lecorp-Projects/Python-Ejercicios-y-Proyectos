# ============================================================
# Suma acumulada de números enteros
# ============================================================
# Este programa solicita un número entero positivo y calcula
# la suma de todos los números desde 1 hasta dicho valor.
#
# El resultado se obtiene usando una variable acumuladora que
# va sumando cada número recorrido dentro de un ciclo for.
#
# Este ejercicio practica:
# - Ciclos con range.
# - Uso de acumuladores.
# - Procesamiento básico de datos numéricos.
# ============================================================

"""
Created on Sun Mar 17 12:59:20 2024

@author: barre
"""
#Escribir un programa que devuelva la suma de los números del 1 al 100. Debe ser 5050
x = int(input("Ingrese un entero positivo para saber la suma de todos sus numeros anteriores "))
a = 0 
for num in range(x+1):
    a = a + num
print(a)
    
