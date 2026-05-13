"""
#Mecanismo del juego:
#El juego pedirá que introduzcamos un número
#El programa te dirá si el número a adivinar es mayor o menor que el número introducido
#El juego te dará tres oportunidades para adivinar.
#Cuando se acaben los intentos, el juego mostrará "GAME OVER"
#En caso que adivines el número, el juego mostrara "WINNER"

#Pasos a seguir
Elegir un número, entre un rango del 1 al 10
Crear una función llamada juego
  Crear una variable para guardar el número de intentos
  Pedir un número al usuario con input
  Bucle que finaliza cuando se introduce el número ganador o se acaban los intentos.
  En cada paso del bucle, evaluar si el numero secreto es mayor que el número introducido
  y el juego mostrará "el número secreto es mayor" y si no mostrará "el número secreto es menor"
  El juego pedirá de nuevo otro número al usuario e incrementará el número de intentos
Crear una función Resultados
  Si el número de intentos es menor al número máximo de intentos
  significa que el usuario adivinó y mostrará el msj de ganador
  sino el número máximo ha sido alcanzado y mostrará el msj de juego terminado.

#Para generar un número aleatorio, primero declarar la librería random
y utilizar la siguiente función:
random.randint(a, b)
Retorna un entero aleatorio N tal que a <= N <= b. 
"""
def juego(numerandom):
  intentos = 3
  for i in range (1,intentos+1,1):
    x = int(input("Ingrese un numero entre 1 y 10 para ver si adivina el numero secreto: "))

    intentos = intentos - 1
    if x == numerandom:
      print("****************************")
      print("FELICIDADES GANASTE EL JUEGO")
      print("****************************")
      print("El numero es:",numerandom)
      print("Te quedaron",intentos,"intentos.")
      break
    if intentos == 0 :
      print("****************************")
      print("PERDISTE, SIGUE INTENTANDO")
      print("****************************")
      print("El numero era:",numerandom)
      break
    if x > int(numerandom):
      print("El numero es menor al que ingresaste.")
    elif x < numerandom:
      print("El numero es mayor al que ingresaste.")    
#Aqui empieza el programa
from random import randint
num = randint(1,10)
juego(num)
    

