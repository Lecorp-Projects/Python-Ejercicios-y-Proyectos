# ============================================================
# Verificador de número par o impar
# ============================================================
# Este programa solicita un número entero y determina si es par
# o impar.
#
# Para realizar la verificación, se usa el operador módulo (%),
# que permite conocer el residuo de una división. Si el residuo
# al dividir entre 2 es cero, el número es par; en caso contrario,
# es impar.
#
# Este ejercicio practica entrada de datos, condicionales y uso
# del operador módulo para evaluar divisibilidad.
# ============================================================

x = float(input("Ingrese un numero entero para ver si es par o impar: "))
#La variable x es un valor de entrada que pide un numero entero. 
if (x%2==0):
#Si se cumple la condicion el numero es par, osea si es divisible entre 2 y no tiene residuo.  
    print("El numero ingresado es par")
else:
#Si no se cumple la condicion y la division tiene residuo, entonces el numero es impar.
    print("El numero ingresado es impar")
    