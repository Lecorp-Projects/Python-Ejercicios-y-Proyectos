#Numero de veces que hay un elemento en la lista (.count)
def countelement(lista, elemento):
    veces = 0 
#El contador empieza en cero.
    for element in lista: 
        if element == elemento:
            veces = veces + 1 
#Se hace un ciclo para recorrer todos los elementos y se suma en uno el contador si el elemento es igual al elemento que se está evaluando. 
    return(veces)
#Insertar un elemento en cualquier posicion de la lista (.insert) 
def insertelement(lista, posicion, elemento):
    limite = len(lista)-1
#Como se empieza a contar desde cero, el limite no es la longitud, sino, que es un numero antes. 
    lista.append(lista[limite])
    for element in range(limite, posicion, -1):
           lista[element] = lista[element-1] 
    lista[posicion] = elemento
#Agregar todos los elementos de una lista al final de otra lista (.extend)
def addlist(lista0, lista1):
    for elemento in lista1:
        lista0.append(elemento)
#Eliminar el primer elemento que se le indique (.remove)
def deletelement(lista, elemento):
    posicion = 0 
    limite = len(lista)-1
    #Para saber la posicion del elemento que se desea eliminar. 
    for element in lista:
        if element == elemento:
            break
        posicion = posicion + 1
    for element in range (posicion, limite, 1):
        lista[element] = lista[element + 1]
    lista.pop(limite)
#Saber la posicion en la lista de un elemento (.index)
def posicion(elemento, lista):
    posicion = 0 
    for element in lista:
        if element == elemento:
            return(posicion)
        posicion = posicion + 1  
#Borrar el elemento de una posicion (del)
def deletebyposition(lista, posicion):
        limite = len(lista)-1
        for element in range (posicion, limite, 1):
            lista[element] = lista[element + 1]
        lista.pop(limite) 
#Invertir el orden de la lista (.reverse)
def invertirlista(lista):
    lista0 = []
    limite = len(lista)-1
    for element in range(limite,-1,-1):
        lista0.append(lista[element])
    return(lista0)
#Imprimir lista de forma agradable para el usuario.
def printlist(lista):
    for elemento in lista:
        print(elemento)
#Imprimir lista de forma aun mas agradable.
def printlist2(lista):
    for elemento in lista:
        print("-",elemento, sep="")
#Imprimir lista con orden numerico. 
def printlistnum(lista):
    x = 1
    for elemento in lista:
        print(x,")",elemento, sep="")
        x = x + 1 
