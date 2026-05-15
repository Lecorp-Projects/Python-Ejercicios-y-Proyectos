# ============================================================
# Identificador de día de la semana
# ============================================================
# Este programa solicita al usuario un número entero del 1 al 7
# y muestra el día de la semana correspondiente.
#
# Funcionalidades principales:
# - Relacionar cada número con un día de la semana.
# - Mostrar un mensaje distinto para valores negativos.
# - Indicar cuando el número ingresado está fuera del rango válido.
#
# Este ejercicio practica el uso de condicionales encadenados
# mediante if, elif y else.
# ============================================================

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
    
    
    
    