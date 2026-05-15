# ============================================================
# Prácticas básicas con condicionales y ciclos
# ============================================================
# Este archivo reúne varios ejercicios iniciales de programación:
#
# - Determinar si un número ingresado es positivo o negativo.
# - Recorrer una cadena de texto letra por letra.
# - Mostrar la tabla de multiplicar del número ingresado.
#
# El objetivo principal es practicar estructuras básicas como
# condicionales, ciclos for, rangos y concatenación de textos
# para presentar resultados en pantalla.
# ============================================================

"""
Spyder Editor

This is a temporary script file.
"""
x = int (input("Numero"))
#x es un valor que ingresa el usuario 
if (x>0):
    print ('Positivo') 
elif (x<0):
    print ('Negativo')

for letter in ("Mimimimi"):
     print (letter)

for mult in range(x+1):
    print(str(x) + " * " + str(mult) + " = " + str(mult*x))
    