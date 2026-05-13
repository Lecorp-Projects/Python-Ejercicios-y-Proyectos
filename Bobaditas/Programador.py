# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 12:12:00 2024

@author: barre
"""
print("Este es un pequeño cuestionario para saber si es elegible para ser parte del equipo de programación.")
edad = int(input("Ingrese su edad "))
xp = int(input("Ingrese 1 si tiene experiencia programando en Python, en cambio si no la tiene, ingrese 0 "))
if (xp != 0 and xp != 1 ):
    print("Ingresó un valor incorrecto, vuelva a responder, correctamente")
elif (edad >= 18 and edad <= 60 and xp == 1):
    print("Usted es elegible para ser miembro del equipo de programación, estaremos en contacto.")
else:
    print("Usted no es elegible para ser miembro del equipo de programación, muchas gracias por su tiempo.")
    
    
    
    

        
        