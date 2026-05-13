#Hugo Esteban Barrero Garcia
#Grupo 4
#Haga un algoritmo que muestre el siguiente patron en la pantalla:
#++++++++++++++
#+++++    +++++
#+++        +++
#+            +
#El tamano del patron estara determinado por un numero entero impar que ingrese el usuario. En el ejemplo mostrado, el tamaño de la figura es 7.
t = int(input("Ingrese un numero entero impar positivo que determinara la dimension del patron: "))
#La variable auxiliar t es un dato de entrada. 
if (t%2 != 0):
#Esta condicion es en caso que al usuario le de por ingresar un numero par.
    s = t
#La variable auxiliar s es para saber la cantidad de espacios y de cruces. (Y se le va restando de 2 en 2 hasta que en algun momento llegara al valor de -1.
    while (s > -1 ):
#Se imprimen "+" s veces, luego "  " (t-s) veces, y luego "+" s veces. Y esos serian los datos de salida. 
        print("+" * s + "  "*(t-s) + "+" * s)
#Si se divide en la mitad, a cada lado se le van quitando de a dos cruces, por lo tanto se va aumentado de 2 espacios en cada lado cada que se itera. 
        s = s-2
else:
    print("Ingrese un numero impar")
#Se imprime en caso que lleguen a poner un numero par. 