#Hugo Esteban Barrero Garcia
#Grupo 4
#Reciba una palabra del usuario y un número entero menor que 26. El programa debe cambiar cada letra por la que le corresponda al dar saltos
#en el alfabeto de acuerdo al número especificado por el usuario. La nueva palabra codificada deberá ser mostrada en pantalla.
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
    

    


