# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 13:32:19 2024

@author: barre
"""
#Escribir un programa que solicite una contraseña (el texto de la contraseña no es importante) y la vuelva a solicitar hasta que las dos contraseñas coincidan.
a = str(input("Ingrese una contraseña cualquiera "))
b = str(input("Vuelva a ingresar la misma contraseña "))

while (a != b):
    print("Contraseña incorrecta, no coinciden las contraseñas")
    b = str(input("Ingrese otra vez la contraseña correctamente "))
print("La contraseña es correcta, ambas coinciden")
