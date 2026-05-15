# ============================================================
# Clasificador de vocales y consonantes
# ============================================================
# Este programa solicita al usuario ingresar un carácter y determina
# si corresponde a una vocal, una consonante o a un símbolo que no
# pertenece al abecedario considerado en el ejercicio.
#
# Funcionalidades principales:
# - Convertir la entrada a minúsculas para facilitar la comparación.
# - Verificar si el carácter ingresado es una vocal.
# - Verificar si corresponde a una consonante.
# - Informar cuando se ingresa un carácter no contemplado.
# - Detectar si el usuario escribió más de un carácter.
#
# Este ejercicio practica validación de texto, uso del operador in
# y condicionales para clasificar una entrada del usuario.
# ============================================================

letra = str(input("Ingrese una letra para determinar si es vocal o consonante: "))
letra = letra.lower()
#Pa tenerlo todo en minusculas
vocales = "aeiou"
consonantes = "bcdfghijklmnpqrstuvxyz"
if letra in vocales: 
    print("Es vocal")
elif letra in consonantes:
    print("Es consonante")
elif len(letra) == 1:
    print("Ingresó un caracter que no es ninguna letra del abecedario (letras sin tildes ni acentos, ni verguilillas)")
else:
    print("Ingreso mas de un caracter")
   

                

    
         
                

    
 

    

