#Hugo Esteban Barrero Garcia
#Grupo 4
#Haga un programa que determine si una palabra ingresada por el usuario es palíndroma o no. Utilice la instrucción while.
palabra = str(input("Ingrese una palabra para ver si esta es palindroma: "))
palabra = palabra.lower()
#Pa tenerlo todo en minusculas
i = 0
f = len(palabra)-1
while i < f:
    if palabra[i] != palabra[f]:
        print("La palabra no es palindroma.")
        break 
    i = i + 1 
    f = f - 1
else:
    print("La palabra es palindroma.")
    
        
        
        
    