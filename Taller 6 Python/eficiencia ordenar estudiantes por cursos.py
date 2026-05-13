def cargar_archivo(archivo):
    """
    Esta funcion es pa abrir un archivo de texto, leerlo y poner los datos como tipos de datos establecidos.
    """
    abrir = open(archivo, "r")
    texto = []
    for char in abrir:
        char = char.strip()
        texto.append(char)
    return(texto)

def cargar_estudiantes(lista):
    ''' Recibe como parametro una lista con toda la informacion de
    la database, separando la informacion correspondiente a los estudiantes,
    para finalmente retornar una lista con dicha informacion. '''
    for element in lista:
        if "," not in element and "." not in element:
            estudiantes = element.split(" ")
            return(estudiantes)
        
def cargar_notas(lista):
    ''' Recibe como parametro una lista con toda la informacion de
     la database, separando la informacion correspondiente a las notas,
     para finalmen retornar una matriz con dicha informacion. '''
    notas = []
    for element in lista:
        if "." in element:
            nota = element.split(" ")
            notas.append(nota)
    return(notas)

def ordenar_mayor_selection(lista):
    """
Ordena una lista de mayor a menor utilizando el algoritmo de selección.

Este algoritmo selecciona el elemento más grande de la lista y lo coloca
en la posición correcta, luego repite el proceso con el resto de la lista.

Recibe una lista y crea una lista auxiliar. 
list: Una nueva lista con los elementos de L ordenados de mayor a menor.
""" 
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[j] > lista[i]:
                lista[i], lista[j] = lista[j], lista[i]

def ordenarEstudiantesCantidadCursos(estudiantes,notas):
    '''Ordena los estudiantes según la cantidad de materias cursadas 
    e imprime el resultado por la pantalla. Para esta funcionalidad 
    usted debe usar obligatoriamente una estrategia de ordenamiento por
    selección.'''
    lista = []
    contador = 0
    for i in range(len(estudiantes)):
        cursos = 0 
        for j in notas[i]: 
            contador += 1
            if j != -2 and j != -1:             
                cursos += 1 
        lista.append(cursos)
    ordenar_mayor_selection(lista)
    for k in lista:
        for i in range(len(estudiantes)):
            cursos = 0 
            for j in notas[i]: 
                contador += 1
                if j != -2 and j != -1:             
                    cursos += 1 
            if cursos == k: 
                lista.remove(k)
    print(contador)
def selection_for_cursos(lista):
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[j][1] > lista[i][1]:
                lista[i], lista[j] = lista[j], lista[i]
        
def ordenarEstudiantesCantidadCursosNew(estudiantes,notas):
    '''Ordena los estudiantes según la cantidad de materias cursadas 
    e imprime el resultado por la pantalla. Para esta funcionalidad 
    usted debe usar obligatoriamente una estrategia de ordenamiento por
    selección.'''
    listatodo = []
    contador = 0
    for i in range(len(estudiantes)):
        cursos = 0 
        lista = []
        for j in notas[i]: 
            contador += 1
            if j != -2 and j != -1:             
                cursos += 1 
        lista.append(estudiantes[i])
        lista.append(cursos)
        listatodo.append(lista)
    selection_for_cursos(listatodo)
    for i in range(len(listatodo)):
        contador += 1
    print(contador)

archivo = "database_p7.txt"
lista = cargar_archivo(archivo)
estudiantes = cargar_estudiantes(lista)
notas = cargar_notas(lista)
print("Iteraciones version 1.")
ordenarEstudiantesCantidadCursos(estudiantes,notas)
print("Iteraciones version 2.")
ordenarEstudiantesCantidadCursosNew(estudiantes,notas)