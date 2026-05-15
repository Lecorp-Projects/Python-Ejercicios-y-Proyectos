# ============================================================
# Cálculo del máximo común divisor
# ============================================================
# Este programa calcula el máximo común divisor de dos números
# enteros usando el algoritmo de Euclides.
#
# El máximo común divisor es el mayor número que divide exactamente
# a los dos valores ingresados.
#
# El algoritmo funciona calculando residuos sucesivos entre los
# números hasta que el residuo sea igual a cero. En ese momento,
# el último divisor utilizado corresponde al máximo común divisor.
#
# Este ejercicio practica ciclos while, operador módulo,
# condicionales y aplicación de un algoritmo matemático clásico.
# ============================================================

print("Ingrese el valor de dos numeros enteros para hallar su maximo comun divisor.")
a = int(input("Primer numero: "))
b = int(input("Segundo numero: "))
num1 = a 
num2 = b 
#Las variables auxiliares a y b, son datos de entrada que almacenan los numeros ingresados, que a su vez se guardan en las variables auxiliares num1 y num2. 
if (a>=b):
#Esta condicion se hace para saber cual numero es mayor que el otro, para poder dividir el mayor con el menor y asi poder realizar tranquilamente el algoritmo de Euclides. 
    r = a%b 
#La variable auxiliar r es el residuo de la division del numero mayor entre el menor. 
    while (r != 0):
#El mayor toma el valor del menor y el menor el valor del residuo, se repite el ciclo hasta que el residuo sea igual a 0.
        a = b
        b = r
#Se halla otro valor del residuo con los nuevos valores.
        r = a%b
#a, b y r son variables auxiliares.
    print("El maximo comun divisor entre",num1,"y",num2,"es:",b)
#Las variables auxiliares num1, num2 y b se imprimen como valores de entrada. 
else:
    r = b%a 
#La variable auxiliar r es el residuo de la division del numero mayor entre el menor. 
    while (r != 0):
#El mayor toma el valor del menor y el menor el valor del residuo, se repite el ciclo hasta que el residuo sea igual a 0.
        b = a
        a = r
#Se halla otro valor del residuo con los nuevos valores.
        r = b%a
#b, a y r son variables auxiliares.
    print("El maximo comun divisor entre",num1,"y",num2,"es:",a)
#Las variables auxiliares num1, num2 y a se imprimen como valores de entrada. 
    
    
