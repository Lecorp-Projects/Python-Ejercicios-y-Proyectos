#Hugo Esteban Barrero Garcia
#Grupo 4
#Escriba un programa que le pida al usuario una palabra o frase y una palabra. El programa deberá imprimir la misma frase o palabra ingresada, pero ocultando la letra que ingresó el usuario con un asterisco.
frase = str(input("Ingrese una palabra o frase: "))
letra = str(input("Ahora ingrese una letra y todas las veces que este esa letra en la frase se van a cambiar por un asterisco: "))
secreta = ""
for i in frase: 
    if i == letra:
        secreta = secreta + "*"
    else: 
        secreta = secreta + i 
print (secreta)
    
    
                  