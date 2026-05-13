archivo = "database_p7.txt"
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

def cargar_cursos(archivo):
    lista = cargar_archivo(archivo)
    curso = ""
    for element in lista:
        if "," in element: 
            for char in element:
                curso = curso + char
            cursos = curso.split(", ")
            return(cursos)
        
def cargar_cursos2(archivo):
    lista = cargar_archivo(archivo)
    for element in lista:
        if "," in element:
            cursos = element.split(",")
            return(cursos)

def printlist(lista):
    for elemento in lista:
        print("-",elemento, sep="")
        
def cargar_estudiantes(archivo):
    lista = cargar_archivo(archivo)
    for element in lista:
        if "," not in element and "." not in element:
            estudiantes = element.split(" ")
            return(estudiantes)
        
def cargar_notas(archivo):
    lista = cargar_archivo(archivo)
    notas = []
    for element in lista:
        if "." in element:
            nota = element.split(" ")
            notas.append(nota)
            for char in notas:
                if "" in char:
                    char.remove("")
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
            print("Ingreso un documento invalido. (Asegurese que solo tenga 10 caracteres numericos).")
        elif documento not in estudiantes: 
            print("El estudiante identificado con este documento no se encuentra en la base de datos.")
    for i in range (0,len(estudiantes)):
        if documento == estudiantes[i]:
            estudiantes.remove(documento)
            notas.remove(notas[i])
            break
    print("Estudiante eliminado exitosamente.")
    
def agregar_estudiante(estudiantes,notas,cursos):
    ''' Permite agregar un estudiante nuevo (identificado por su
    número de documento) junto con las respectivas notas de todos sus cursos.'''
    while True:
        documento = input("Ingrese el documento del estudiante que desea agregar: ")
        if documento not in estudiantes and validar_documento(documento) == True:
            break
        elif validar_documento(documento) == False:
            print("Ingreso un documento invalido. (Asegurese que solo tenga 10 caracteres numericos).")
        elif documento in estudiantes: 
            print("El estudiante identificado con este documento ya se encuentra registrado. ")
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
                print("Asegurese que ingreso un caracter que sea valido o una nota que este en el rango de 0 a 5 (si va a ingresar decimales ingreselo con un punto, de esta forma num.num).")              
    estudiantes.append(str(documento))
    notas.append(nuevasnotas)
    print("Estudiante agregado exitosamente.")
b = cargar_cursos(archivo)
x = cargar_notas(archivo)
a = cargar_estudiantes(archivo)
"""agregar_estudiante(a,x,b)"""
def notasfloat(notas):
    """
    Vuelve todas las notas de string a float. 
    """
    for lista in notas:
        for i in range(len(lista)): 
            lista[i] = float(lista[i])
def promedio_curso(cursos, notas):
    '''Recibe la matriz de las notas en float y la lista de los cursos. Calcula el promedio de las notas del curso,
    devolviendo el resultado en una lista. Este resultado se debe mostrar por 
    pantalla.'''
    print("Esta es la lista de los cursos que hay: ")
    printlist(cursos)
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
    promedio = round(promedio/cantidad,2) 
    print("El promedio del",curso,"es:",promedio)
#notasfloat(x)
"""promedio_curso(b, x)"""
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
         promedio = round(promedio/cantidad,2) 
         notascursos.append(promedio)
         print("El promedio del",curso,"es:",promedio)
    return(notascursos)
#print(promedio_cursos(b,x))

def promedio_estudiantes_print(estudiantes,notas): 
    
    estudiantesnotas = []
    for i in range(0,len(estudiantes)):
         estudiante = estudiantes[i]
         promedio = 0
         cantidad = 0 
         for j in range(0,len(notas[i])):
             if notas[i][j] >= 0: 
                 promedio += notas[i][j]
                 cantidad += 1
         promedio = round(promedio/cantidad,2) 
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
         promedio = round(promedio/cantidad,2) 
         estudiantesnotas.append(promedio)
    return(estudiantesnotas)

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

#print(promedio_estudiantes(a,x)
def tresNotasMayores(estudiantes,cursos,notas):
    ''''Recibe la matriz de las notas en float, la lista de los documentos de los estudiantes y la lista de los cursos. Calcula las 3 mayores notas de un curso dado, e imprime los
    números de documento de dichos estudiantes. Si varios estudiantes 
    coinciden en las notas, deben reportarse todos.'''
    print("Esta es la lista de los cursos que hay: ")
    printlist(cursos)
    while True: 
        curso = input("Ingrese el curso del cual desea ver las 3 notas mayores:")
        if curso in cursos:
            break
        else:
            print("Ingrese correctamente el nombre de un curso que se encuentre en la lista de cursos.")
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
        print("Del ",curso," el estudiante con la nota mas alta es el identificado con el documento ", estudiantes[position]," y saco una nota de " ,mayor,".", sep="")
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
#tresNotasMayores(a,b,x)
def printlistnum(lista):
    x = 1
    for elemento in lista:
        print(x,")",elemento, sep="")
        x = x + 1 
        
def menorNotaEstudiante(estudiantes,cursos,notas):
    ''' Recibe la matriz de las notas en float, la lista de los documentos de los estudiantes y la lista de los cursosRetorna el código del curso en el cual ha obtenido su
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
    x = ordenar_lista_menor(lista)
    while parar == 0:
        print("La menor nota del estudiante identificado con el documento ",estudiante," fue de ",menor," en el ", cursos[j],".",sep='')
        x.remove(menor)
        if x[0] == menor:
            x.remove(menor)
            parar = 1
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
                menor = x[h]
#while True: 
 #   menorNotaEstudiante(a,b,x)
def ordenarPromedioEstudiantes(estudiantes,notas):
    '''Imprime por pantalla a los estudiantes ordenados
    según su promedio de notas, de mayor a menor. Para esta funcionalidad 
    usted debe usar obligatoriamente una estrategia de ordenamiento burbuja.'''
    ordenar = promedio_estudiantes(estudiantes, notas)
    x = ordenar_lista_mayor(ordenar)
    print("La lista de los estudiantes ordenados por su promedio es:")
    for k in range(0,len(ordenar)):
        for i in range(0,len(estudiantes)):
             estudiante = estudiantes[i]
             promedio = 0
             cantidad = 0 
             for j in range(0,len(notas[i])):
                 if notas[i][j] >= 0: 
                     promedio += notas[i][j]
                     cantidad += 1
             promedio = round(promedio/cantidad,2) 
             if promedio == x[k]:
                 print("El estudiante identificado con el documento", estudiante,"saco una nota promedio de",x[k])
                 
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
                
def selection_for_cursos(lista):
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[j][1] > lista[i][1]:
                lista[i], lista[j] = lista[j], lista[i]
                print(lista)
                print(",")
        
def ordenarEstudiantesCantidadCursosNew(estudiantes,notas):
    '''Ordena los estudiantes según la cantidad de materias cursadas 
    e imprime el resultado por la pantalla. Para esta funcionalidad 
    usted debe usar obligatoriamente una estrategia de ordenamiento por
    selección.'''
    listatodo = []
    for i in range(len(estudiantes)):
        cursos = 0 
        lista = []
        for j in notas[i]: 
            if j != -2 and j != -1:             
                cursos += 1 
        lista.append(estudiantes[i])
        lista.append(cursos)
        listatodo.append(lista)
    selection_for_cursos(listatodo)
    for i in range(len(listatodo)):
        print("El documento",listatodo[i][0],"tiene matriculados",listatodo[i][1],"cursos.")

def escribir_codigo(archivo, estudiantes, notas, cursos):
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
        
escribir_codigo(archivo,a,x,b)       
#ordenarEstudiantesCantidadCursos(a, x)
#print(promedio_estudiantes_print(a,x))
#ordenarPromedioEstudiantes(a,x)
#agregar_estudiante(a,x,b)
#print(x)
"""print(cargar_archivo(archivo))
print(cargar_cursos2(archivo))
print(cargar_estudiantes(archivo))"""

