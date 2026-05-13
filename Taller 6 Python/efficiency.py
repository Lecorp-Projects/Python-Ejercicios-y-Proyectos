def cargar_archivoviejito(archivo):
    """
    Esta funcion es pa abrir un archivo de texto, leerlo y poner los datos como tipos de datos establecidos.
    """
    texto = []
    abrir = open(archivo, "r")
    txt = abrir.read()
    dato = ""
    abrir.close()
    contador = 0 
    for char in txt: 
        contador += 1
        if char == "\n":
            texto.append(dato)
            dato = ""
        else:
            dato = dato + char
    print(contador)
    return(texto)

def cargar_archivo(archivo):
    """
    Esta funcion es pa abrir un archivo de texto, leerlo y poner los datos como tipos de datos establecidos.
    """
    abrir = open(archivo, "r")
    texto = []
    contador = 0 
    for char in abrir:
        contador += 1 
        char = char.strip()
        texto.append(char)
    print(contador)
    return(texto)

def cargar_notasviejita(lista):
    ''' Recibe como parametro una lista con toda la informacion de
     la database, separando la informacion correspondiente a las notas,
     para finalmen retornar una matriz con dicha informacion. '''
    notas = []
    contador = 0
    for element in lista:
        if "." in element:
            nota = element.split(" ")
            notas.append(nota)
            for char in notas:
                contador += 1 
                if "" in char:
                    char.remove("")
    print(contador)
    return(notas)

def cargar_notas(lista):
    ''' Recibe como parametro una lista con toda la informacion de
     la database, separando la informacion correspondiente a las notas,
     para finalmen retornar una matriz con dicha informacion. '''
    notas = []
    contador = 0
    for element in lista:
        contador += 1 
        if "." in element:
            nota = element.split(" ")
            notas.append(nota)
    print(contador)
    return(notas)

archivo = "database_p7.txt"
print("Iteraciones version 1.")
lista1 = cargar_archivoviejito(archivo)
cargar_notasviejita(lista1)
print("Iteraciones version 2.")
lista2 = cargar_archivo(archivo)
cargar_notas(lista2)
