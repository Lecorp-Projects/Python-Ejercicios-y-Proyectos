# ============================================================
# Verificación de contraseñas coincidentes
# ============================================================
# Este programa solicita al usuario ingresar una contraseña y luego
# volver a escribirla para comprobar que ambas coincidan.
#
# Si las contraseñas son diferentes, el programa seguirá pidiendo
# la segunda contraseña hasta que sea igual a la primera.
#
# Funcionalidades principales:
# - Solicitar una contraseña inicial.
# - Pedir la confirmación de la contraseña.
# - Validar si ambas contraseñas coinciden.
# - Repetir la solicitud mientras la confirmación sea incorrecta.
# ============================================================

"""
Created on Sun Mar 17 13:32:19 2024

@author: barre
"""

a = str(input("Ingrese una contraseña cualquiera "))
b = str(input("Vuelva a ingresar la misma contraseña "))

while (a != b):
    print("Contraseña incorrecta, no coinciden las contraseñas")
    b = str(input("Ingrese otra vez la contraseña correctamente "))
print("La contraseña es correcta, ambas coinciden")
