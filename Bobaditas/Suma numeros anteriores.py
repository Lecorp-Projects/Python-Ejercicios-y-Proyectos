# -*- coding: utf-8 -*-
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
    
