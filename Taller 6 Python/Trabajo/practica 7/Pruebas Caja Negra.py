#Jose Gabriel Giraldo F
#Hugo Esteban Barrero
#Grupo 4

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

def cargar_cursos(lista):
    ''' Recibe como parametro una lista con toda la informacion de
    la database, separando la informacion correspondiente a los cursos,
    retornando una lista con dicha informacion. '''
    for element in lista:
        if "," in element:
            cursos = element.split(", ")
            return(cursos)
        
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

def validar_documento(documento):
    '''
    Valida un número de documento. Debe tener 10 caracteres numericos.   
    el documento es el string a validar
    return -> Boolean (True or False) si es valido o no
    '''
    numeros = ["0","1","2","3","4","5","6","7","8","9","."]
    documento = str(documento)
    if len(documento) == 10:
        for character in documento: 
            if character in numeros: 
                continue
            else:
                return(False)
        return(True)
    else:
        return(False)
    
def validar_nota(nota):
    '''
    Valida un número de nota. Debe tener caracteres numericos y/o un punto.   
    el documento es el string a validar
    return -> Boolean (True or False) si es valido o no
    '''
    numeros = ["0","1","2","3","4","5","6","7","8","9"]
    nota = str(nota)
    if len(nota) == 3:
        for i in range(0,len(nota)): 
            if nota[i] in numeros: 
                continue
            elif nota[1] == ".":
                continue
            else:
                return(False)
        if 0 <= float(nota) <= 5.0:
            return(True)
        else:
            return(False)
    elif len(nota) == 1 and nota in numeros and 0 <= float(nota) <= 5.0:
        return(True)
    else:
        return(False)
    
def eliminar_estudiante(estudiantes, notas):
    '''Permite eliminar un usuario de la base de datos referente a un numero
    de documento, tambien elimina las respectivas notas'''
    while True:
        documento = input("Ingrese el documento del estudiante que desea eliminar: ")
        if documento in estudiantes and validar_documento(documento) == True:
            break   
        elif validar_documento(documento) == False:
            print('')
            print("Ingreso un documento invalido. (Asegurese que solo tenga 10 caracteres numericos).")
            print("")
        elif documento not in estudiantes: 
            print('')
            print("El estudiante identificado con este documento no se encuentra en la base de datos.")
            print("")
    for i in range (0,len(estudiantes)):
        if documento == estudiantes[i]:
            estudiantes.remove(documento)
            notas.remove(notas[i])
            break
    print("")
    print("Estudiante eliminado exitosamente.")
    print("")
    
def agregar_estudiante(estudiantes,notas,cursos):
    ''' Permite agregar un estudiante nuevo (identificado por su
    número de documento) junto con las respectivas notas de todos sus cursos.'''
    while True:
        documento = input("Ingrese el documento del estudiante que desea agregar: ")
        if documento not in estudiantes and validar_documento(documento) == True:
            break
        elif validar_documento(documento) == False:
            print('')
            print("Ingreso un documento invalido. (Asegurese que solo tenga 10 caracteres numericos).")
            print("")
        elif documento in estudiantes: 
            print('')
            print("El estudiante identificado con este documento ya se encuentra registrado. ")
            print("")
    nuevasnotas = [] 
    for i in range(0, len(cursos)):
        finish = True
        while finish == True :
            print("Para el curso",i+1,"ingrese:")
            nota = input("La nota del estudiante en caso de haber cancelado el curso ingrese -1 y en caso de que no pertenezca al curso ingrese -2: ",)
            if validar_nota(nota) == True or nota == "-1" or nota == "-2"  :
                nuevasnotas.append(str(nota))
                finish = False  
            else: 
                print("")
                print("Asegurese que ingreso un caracter que sea valido o una nota que este en el rango de 0 a 5 (si va a ingresar decimales ingreselo con un punto, de esta forma num.num).")
                print("")
    estudiantes.append(str(documento))
    notas.append(nuevasnotas)
    print("")
    print("Estudiante agregado exitosamente.")
    print("")

def notasfloat(notas):
    """
    Vuelve todas las notas de string a float. 
    """
    for lista in notas: 
        for i in range(len(lista)):
            lista[i] = float(lista[i])
            
def printlist(lista):
    """Imprime una lista de forma bonita y entendible para el usuario."""
    for elemento in lista:
        print("-",elemento, sep="")
        
def printlistnum(lista):
    """Imprime la lista con numeros antes del valor"""
    x = 1
    for elemento in lista:
        print(x,")",elemento, sep="")
        x = x + 1 
        
def ordenar_lista_mayor(lista):
    """Recibe una lista y devuelve una lista auxiliar de la misma ordena de mayor a menor."""
    lista2 = list(lista)
    for i in range(0,len(lista2)):
        for j in range(0,len(lista2)-i-1):
            if lista2[j] < lista2[j+1]:
                lista2[j], lista2[j+1] = lista2[j+1], lista2[j]
    return(lista2)

def ordenar_lista_menor(lista):
    """Recibe una lista y devuelve una lista auxiliar de la misma, ordenada de menor a mayor."""
    lista2 = list(lista)
    for i in range(0,len(lista2)):
        for j in range(0,len(lista2)-i-1):
            if lista2[j] > lista2[j+1]:
                lista2[j], lista2[j+1] = lista2[j+1], lista2[j]
    return(lista2)

def promedio_curso(cursos, notas):
    '''Recibe la matriz de las notas en float y la lista de los cursos. Calcula el promedio de las notas del curso,
    devolviendo el resultado en una lista. Este resultado se debe mostrar por 
    pantalla.'''
    print("Esta es la lista de los cursos que hay: ")
    print("")
    printlist(cursos)
    print("")
    while True: 
        curso = input("Ingrese el curso del cual desea ver el promedio de las notas de los estudiantes:")
        if curso in cursos:
            break
        else:
            print("Ingrese correctamente el nombre de un curso que se encuentre en la lista de cursos.")
    promedio = 0
    cantidad = 0 
    for i in range(0,len(cursos)):
        if cursos[i] == curso:
            break
    for j in range(0,len(notas)):
        if notas[j][i] >= 0: 
            promedio += notas[j][i]
            cantidad += 1      
    if promedio != 0:
        promedio = round(promedio/cantidad,2) 
    else: 
        promedio = 0 
    print("")
    print("El promedio del",curso,"es:",promedio)
    print("")
    
def promedio_cursos(cursos,notas):
    '''Calcula el promedio de notas en todos los cursos,
    devolviendo el resultado en una lista. Este resultado se debe mostrar por 
    pantalla.'''
    notascursos = []
    for i in range(0,len(cursos)):
         curso = cursos[i]
         promedio = 0
         cantidad = 0 
         for j in range(0,len(notas)):
             if notas[j][i] >= 0: 
                 promedio += notas[j][i]
                 cantidad += 1   
         if promedio != 0:
             promedio = round(promedio/cantidad,2) 
         else: 
             promedio = 0
         notascursos.append(promedio)
         print("El promedio del",curso,"es:",promedio)
    return(notascursos)

def promedio_estudiantes_print(estudiantes,notas): 
    """"Recibe la matriz de las notas en float y la lista de los documentos de los estudiantes. Saca el promedio de cada estudiante y lo imprime en pantalla."""
    estudiantesnotas = []
    for i in range(0,len(estudiantes)):
         estudiante = estudiantes[i]
         promedio = 0
         cantidad = 0 
         for j in range(0,len(notas[i])):
             if notas[i][j] >= 0: 
                 promedio += notas[i][j]
                 cantidad += 1
         if promedio != 0:
             promedio = round(promedio/cantidad,2) 
         else: 
             promedio = 0
         estudiantesnotas.append(promedio)
         print("El promedio del",estudiante,"es:",promedio)
    return(estudiantesnotas)

def promedio_estudiantes(estudiantes,notas): 
    """"Recibe la matriz de las notas en float y la lista de los documentos de los estudiantes. Saca el promedio de cada estudiante"""
    estudiantesnotas = []
    for i in range(0,len(estudiantes)):
         promedio = 0
         cantidad = 0 
         for j in range(0,len(notas[i])):
             if notas[i][j] >= 0: 
                 promedio += notas[i][j]
                 cantidad += 1
         if promedio != 0:
             promedio = round(promedio/cantidad,2) 
         else: 
             promedio = 0
         estudiantesnotas.append(promedio)
    return(estudiantesnotas)

def tresNotasMayores(estudiantes,cursos,notas):
    ''''Recibe la matriz de las notas en float, la lista de los documentos de los estudiantes y la lista de los cursos. Calcula las 3 mayores notas de un curso dado, e imprime los
    números de documento de dichos estudiantes. Si varios estudiantes 
    coinciden en las notas, deben reportarse todos.'''
    print("Esta es la lista de los cursos que hay: ")
    print("")
    printlist(cursos)
    print("")
    while True: 
        curso = input("Ingrese el curso del cual desea ver las 3 notas mayores:")
        if curso in cursos:
            break
        else:
            print("")
            print("Ingrese correctamente el nombre de un curso que se encuentre en la lista de cursos.")
            print("")
    mayor = 0
    lista = []
    parar = 0 
    for i in range(0,len(cursos)):
        if cursos[i] == curso:
            break
    for j in range(0,len(notas)):
        if notas[j][i] >= 0: 
            lista.append(notas[j][i])
            if notas[j][i] > mayor:
                mayor = notas[j][i]
                position = j
    x = ordenar_lista_mayor(lista)
    while parar < 3 :
        print("Del ",curso," uno de los estudiantes con una de las notas mas altas es el identificado con el documento ", estudiantes[position]," y saco una nota de " ,mayor,".", sep="")
        x.remove(mayor)
        if x[0] == mayor:
            parar += 1
            x.remove(mayor)
            for j in range(0,len(notas)):
                if notas[j][i] >= 0: 
                    if notas[j][i] == mayor:
                        position = j
            print("Junto con el estudiante identificado con el documento ", estudiantes[position]," que saco una nota de " ,mayor,".", sep="")
        else:
            parar += 1
        mayor = 0 
        for h in range(len(x)):
            if x[h] > mayor:
                mayor = x[h]
        for j in range(0,len(notas)):
            if notas[j][i] >= 0: 
                if notas[j][i] == mayor:
                    position = j
    
def menorNotaEstudiante(estudiantes,cursos,notas):
    ''' Recibe la matriz de las notas en float, la lista de los documentos de los estudiantes y la lista de los cursos. Retorna el código del curso en el cual ha obtenido su
    menor nota un estudiante dado.'''
    print("Esta es la lista de los documentos de los estudiantes: ")
    printlistnum(estudiantes)
    while True: 
        estudiante = input("Ingrese el documento del estudiante del cual desea ver la menor nota:")
        if estudiante in estudiantes:
            break
        else:
            print("Ingrese correctamente el documento del estudiante, que se encuentre en la lista de documentos.")
    menor = 5   
    lista = []
    parar = 0 
    for i in range(0,len(estudiantes)):
        if estudiantes[i] == estudiante:
            break
    for j in range(0,len(cursos)):
        if notas[i][j] >= 0: 
            lista.append(notas[i][j])
            if notas[i][j] < menor: 
                menor = notas[i][j]
    for j in range(0,len(cursos)):
        if menor == notas[i][j]:
            break
    print("")
    print("La menor nota del estudiante identificado con el documento ",estudiante," fue de ",menor," en el ", cursos[j],".",sep='')
    print("")
    """x = ordenar_lista_menor(lista)
    while parar == 0:
        print("La menor nota del estudiante identificado con el documento ",estudiante," fue de ",menor," en el ", cursos[j],".",sep='')
        x.remove(menor)
        if x[0] == menor:
            x.remove(menor)
            for j in range(0,len(cursos)):
                if notas[i][j] >= 0: 
                    if notas[i][j] == menor:
                        position = j
            print("Y obtuvo la misma nota de " ,menor," en el ", cursos[position], sep="")
        else:
            parar = 1
        menor = 5 
        for h in range(0,len(x)):
            if x[h] < menor:
                menor = x[h]"""
                
def ordenarPromedioEstudiantes(estudiantes,notas):
    '''Imprime por pantalla a los estudiantes ordenados
    según su promedio de notas, de mayor a menor. Para esta funcionalidad 
    usted debe usar obligatoriamente una estrategia de ordenamiento burbuja.'''
    ordenar = promedio_estudiantes(estudiantes, notas)
    x = ordenar_lista_mayor(ordenar)
    print("La lista de los estudiantes ordenados por su promedio es:")
    promedios_impresos = []
    for k in range(0, len(ordenar)):
        for i in range(0, len(estudiantes)):
            estudiante = estudiantes[i]
            promedio = 0
            cantidad = 0 
            for j in range(0, len(notas[i])):
                if notas[i][j] >= 0: 
                    promedio += notas[i][j]
                    cantidad += 1
            if promedio != 0:
                promedio = round(promedio / cantidad, 2) 
            else: 
                promedio = 0
            if promedio == x[k] and estudiante not in promedios_impresos:
                promedios_impresos.append(estudiante)
                print("El estudiante identificado con el documento", estudiante, "saco una nota promedio de", x[k])
                 
def ordenar_mayor_selection(lista):
    """
Ordena una lista de mayor a menor utilizando el algoritmo de selección.

Este algoritmo selecciona el elemento más grande de la lista y lo coloca
en la posición correcta, luego repite el proceso con el resto de la lista.

Recibe una lista y crea una lista auxiliar. 
list: Una nueva lista con los elementos de L ordenados de mayor a menor.
"""
    for i in range(0, len(lista)-1):
        mayor = i 
        for j in range(i+1, len(lista)):
            if lista[j] > lista[mayor]:
                mayor = j 
        if mayor != i: 
            lista[mayor], lista[i] = lista[i], lista[mayor]

def ordenarEstudiantesCantidadCursos(estudiantes,notas):
    '''Ordena los estudiantes según la cantidad de materias cursadas 
    e imprime el resultado por la pantalla. Para esta funcionalidad 
    usted debe usar obligatoriamente una estrategia de ordenamiento por
    selección.'''
    lista = []
    for i in range(len(estudiantes)):
        cursos = 0 
        for j in notas[i]: 
            if j != -2 and j != -1:             
                cursos += 1 
        lista.append(cursos)
    ordenar_mayor_selection(lista)
    for k in lista:
        for i in range(len(estudiantes)):
            cursos = 0 
            for j in notas[i]: 
                if j != -2 and j != -1:             
                    cursos += 1 
            if cursos == k: 
                lista.remove(k)
                print("El estudiante identificado con el documento", estudiantes[i],"tiene matriculados",k,"cursos.")
  
def escribir_codigo(archivo, estudiantes, notas, cursos):
    ''' Abre el archivo de texto reescribiendo toda la información con los cambios hechos por el usuario en la ejecución del programa '''
    x = open(archivo, "w")
    string = ""
    #Pa los cursos.
    for i in range(len(cursos)): 
        if i != len(cursos)-1:
            string = string + cursos[i] + "," + " "
        else:
            string = string + cursos[i]
    x.write(string + "\n")
    #Pa los estudiantes.
    string = ""
    for i in range(len(estudiantes)): 
        if i != len(estudiantes)-1:
            string = string + estudiantes[i] + " "
        else:
            string = string + estudiantes[i]
    x.write(string + "\n")
    x.write("\n")
    #Pa las notas.
    string = ""
    for i in range(len(notas)): 
        for j in range(len(notas[i])):
            string = string + str(notas[i][j]) + " "
        x.write(string + "\n")
        string = ""
    x.close()
        
def menu():
    print("Por favor, seleccione una opción sobre lo que desea hacer con los datos.")
    print("1. Si desea eliminar un estudiante.")
    print("2. Si desea agregar un estudiante.")
    print("3. Si desea ver el promedio de cada estudiante.")
    print("4. Si desea ver el promedio de todos los cursos.")
    print("5. Si desea ver el promedio de un curso.")
    print("6. Si desea ver las tres notas mayores de un curso.")
    print("7. Si desea ver la menor nota de un estudiante.")
    print("8. Si desea ver los promedios de los estudiantes ordenados.")
    print("9. Si desea ver los estudiantes ordenados por la cantidad de cursos.")
    print("10. Si desea salir y culminar el programa.")
    
archivo = "database_p7.txt"
lista = cargar_archivo(archivo)
estudiantes = cargar_estudiantes(lista)
notas = cargar_notas(lista)
cursos = cargar_cursos(lista)
notasfloat(notas)

"""Prueba de validar_documento"""

assert validar_documento("1234567890") == True
assert validar_documento("123456789") == False
assert validar_documento("12345678901") == False
assert validar_documento("12345a7890") == False

'''Prueba de promedio_cursos'''

cursos = ["Curso1", "Curso2", "Curso3"]
notas = [[4.0, 3.5, 4.2], [2.5, 3.0, 3.8], [4.5, 2.0, 3.7], [3.0, 4.0, 2.5]]
resultado_esperado = [3.5, 3.12, 3.55]
assert promedio_cursos(cursos, notas) == resultado_esperado
# Probar con grandes volúmenes de datos
cursos_large = []
for i in range(100):
     x = "Curso" + str(i)
     cursos_large.append(x)
notas_large = []
for j in range(1000):
    notas_j = []
    for i in range(100):
        nota = round(i % 5 + 0.1 * j, 1)
        notas_j.append(nota)
    notas_large.append(notas_j)
# Verificar si la función maneja grandes volúmenes sin error
promedios_large = promedio_cursos(cursos_large, notas_large)
assert len(promedios_large) == 100

"""Prueba eliminar_estudiante"""

# Datos de prueba
estudiantes = ["1033492448", "1032090603", "1002152167", "1028854736", "1014191590"]
notas = [[4.0, 3.5, 4.2], [2.5, 3.0, 3.8], [4.5, 2.0, 3.7], [3.0, 4.0, 2.5], [3.5, 2.8, 3.2]]
documento_eliminar = "1028854736"
resultado_esperado_estudiantes = ["1033492448", "1032090603", "1002152167", "1014191590"]
resultado_esperado_notas = [[4.0, 3.5, 4.2], [2.5, 3.0, 3.8], [4.5, 2.0, 3.7], [3.5, 2.8, 3.2]]
# Ejecutar la función
eliminar_estudiante(estudiantes, notas)
# Verificar si el estudiante y sus notas fueron eliminados correctamente
assert estudiantes == resultado_esperado_estudiantes
assert notas == resultado_esperado_notas