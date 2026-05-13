# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 13:14:32 2024

@author: barre
"""
#Escribir un programa que devuelva los números pares del 1 al 50
x = int(input("Ingrese un entero positivo para saber todos los pares entre el 1 y ese numero "))
for num in range(1,x+1):
    if (num % 2 == 0):
        print (num)
print("Esos son todos los pares entre 1 y ",x)
