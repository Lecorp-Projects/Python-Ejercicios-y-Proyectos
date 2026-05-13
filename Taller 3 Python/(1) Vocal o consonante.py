#Hugo Esteban Barrero Garcia
#Grupo 4
#Escriba un programa que tome un carácter (es decir, un string de longitud 1) y determine si el carácter es vocal o consonante.
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
   

                

    
         
                

    
 

    

