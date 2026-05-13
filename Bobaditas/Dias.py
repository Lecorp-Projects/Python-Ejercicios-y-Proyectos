# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 12:00:20 2024

@author: barre
"""

num = int(input("Introduzca un número entero del 1 al 7 para saber cual dia de la semana es ")) 

if (num == 1):
    print("El dia es lunes")
elif (num == 2): 
    print("El dia es martes")
elif (num == 3): 
    print("El dia es miércoles")
elif (num == 4): 
    print("El dia es jueves")
elif (num == 5): 
    print("El dia es viernes")
elif (num == 6): 
    print("El dia es sábado")
elif (num == 7): 
    print("El dia es domingo")
elif (num <0):
    print ("No hay días negativos.")
else:
    print("La semana solo tiene 7 días." )
    
    
    
    