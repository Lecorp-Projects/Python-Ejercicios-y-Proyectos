#Hugo Esteban Barrero Garcia 
#Grupo 4
#Haga un algoritmo que muestre el siguiente patron en la pantalla:
#*
#***
#*****
#*******
#*****
#***
#*
#El tamano del patron estara determinado por un numero entero impar que ingrese el usuario. En el ejemplo mostrado, el tamaño de la figura es 7.
t = int(input("Ingrese un numero entero impar positivo que determinara la dimension del patron: "))
#La variable auxiliar t es un dato de entrada. 
if (t%2 != 0):
#Esta condicion es en caso que al usuario le de por ingresar un numero par.
    c = 1
#La variable auxiliar c1 es un contador para que pare el ciclo cuando el valor de c1 llegue a ser igual al de t. 
    while (t != c):
        print("*"*c)
#Se imprimen c1 asteriscos y luego se le suma 2 a c1.
        c = c+2 
    print("*"*t)
#Se imprimen la cantidad de asteriscos del numero que se ingresa. 
    while (t!=1):
        t = t-2
#Se imprimen t asteriscos luego que se le fuera restado 2 a t.
        print("*"*t)
else:
    print("Ingrese un numero impar")
#Se imprime en caso que lleguen a poner un numero par. 
    
