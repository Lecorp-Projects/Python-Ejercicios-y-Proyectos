# ============================================================
# Generador de números pares
# ============================================================
# Este programa solicita un número entero positivo y muestra
# todos los números pares comprendidos entre 1 y ese valor.
#
# Para identificar los números pares, se utiliza el operador
# módulo, verificando cuáles son divisibles exactamente entre 2.
#
# Este ejercicio practica:
# - Recorridos con ciclos for.
# - Uso de range.
# - Condicionales dentro de un ciclo.
# - Operador módulo para evaluar divisibilidad.
# ============================================================

"""
Created on Sun Mar 17 13:14:32 2024

@author: barre
"""
#Escribir un programa que devuelva los números pares del 1 al 50
x = int(input("Ingrese un entero positivo para saber todos los pares entre el 1 y ese numero "))
for num in range(1,x+1):
    if (num % 2 == 0):
        print (num)
print("Esos son todos los pares entre 1 y",x)
