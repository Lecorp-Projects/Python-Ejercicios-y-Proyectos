# ============================================================
# Codificador de palabras por desplazamiento alfabético
# ============================================================
# Este programa solicita una palabra y un número entero entre 0 y 26
# para generar una versión codificada desplazando cada letra dentro
# del abecedario.
#
# Funcionalidades principales:
# - Convertir la palabra a minúsculas.
# - Verificar que el desplazamiento esté dentro del rango esperado.
# - Validar que la palabra contenga únicamente letras sin tildes
#   ni caracteres especiales.
# - Buscar la posición de cada letra en el abecedario.
# - Construir una nueva palabra desplazada según el número ingresado.
#
# Este ejercicio practica recorridos de cadenas, validaciones,
# búsqueda de posiciones con index y transformación de texto.

palabra = str(input("Ingrese una palabra: "))
numero = int(input("Ingrese un numero entero positivo menor o igual que 26: "))
palabra = palabra.lower()
#Pa tenerlo todo en minusculas
letras = "abcdefghijklmnopqrstuvwxyz"
codificada = ""
verificador = False
if not numero in range(0,27):
    print("Ingreso un numero como se le pide")
for caracter in palabra:
    if not caracter in letras: 
        print("Ingreso un caracter incorrecto, vuelva a hacerlo (no se pueden numeros)")
        verificador = False
        break
    else:
        verificador = True 
if verificador == True: 
    for letra in palabra: 
        posicion = letras.index(letra)
        nuevaposicion = posicion + numero
        if nuevaposicion >= 27:
            nuevaposicion = nuevaposicion - 26
        codificada = codificada + letras[nuevaposicion]
    print("Para la palabra",palabra,"su palabra codificada es:",codificada)
    

    


