#Hugo Esteban Barrero Garcia
#Grupo 4
#Teniendo en cuenta que un carro necesita cambio de aceite cada 5.678 km, haga un algoritmo que calcule cuantos cambios de aceite ha tenido un carro segun el total de kilometros que ha recorrido.
#Ejemplo1: Si recorre 6.000km, tiene que hacer cambio de aceite una vez. 
#Ejemplo2: Si recorre 200.000km, tiene que hacer 35 cambios de aceite. 
k = float(input("Ingrese el valor recorrido en kilometros como un valor positivo: "))
#La variable k es auxiliar y es un dato de entrada. 
c = k//5678
#c es una variable auxiliar que al hacer la division entera entre 5678 que es cada vez que se cambia el aceite, nos dice cuantos cambios tuvieron que hacerse. 
if (c==0):
#Si c es cero entonces se imprime en pantalla lo siguiente. 
    print("En su recorrido no tuvo que hacer cambio de aceite.")
elif(c==1):
#Si c es uno entonces se imprime en pantalla lo siguiente. 
    print ("En su recorrido tuvo que hacer cambio de aceite una vez.")
else: 
#Se imprime el valor de la variable c como dato de salida. 
    print("En su recorrido tuvo que hacer cambio de aceite " ,int(c), " veces.")

  