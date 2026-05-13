#Hugo Esteban Barrero Garcia
#Grupo 4
#Diseñe un algoritmo que lea un número entero y determine si es par o impar.
x = float(input("Ingrese un numero entero para ver si es par o impar: "))
#La variable x es un valor de entrada que pide un numero entero. 
if (x%2==0):
#Si se cumple la condicion el numero es par, osea si es divisible entre 2 y no tiene residuo.  
    print("El numero ingresado es par")
else:
#Si no se cumple la condicion y la division tiene residuo, entonces el numero es impar.
    print("El numero ingresado es impar")
    