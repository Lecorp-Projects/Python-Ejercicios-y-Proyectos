# ============================================================
# Funciones del sistema de gestión de notas
# ============================================================
# Este módulo contiene la lógica del programa:
# carga de datos, validaciones, administración de estudiantes,
# cálculo de promedios, búsquedas, ordenamientos y escritura
# de la base de datos actualizada.
# ============================================================


# -----------------------------------------------------------------
# CARGA Y ESCRITURA DE DATOS
# -----------------------------------------------------------------

def cargar_archivo(archivo):
    """
    Lee un archivo de texto y retorna una lista con sus líneas no vacías,
    sin incluir saltos de línea ni espacios externos.

    Si el archivo no existe, retorna una lista vacía.
    """
    texto = []

    try:
        abrir = open(archivo, "r", encoding="utf-8")

        for linea in abrir:
            linea = linea.strip()

            if linea != "":
                texto.append(linea)

        abrir.close()

    except FileNotFoundError:
        return([])

    return(texto)


def cargar_cursos(lista):
    """
    Recibe la información completa del archivo y retorna la lista
    de cursos contenidos en la primera línea.
    """
    if len(lista) == 0:
        return([])

    cursos_crudos = lista[0].split(",")
    cursos = []

    for curso in cursos_crudos:
        curso = curso.strip()

        if curso != "":
            cursos.append(curso)

    return(cursos)


def cargar_estudiantes(lista):
    """
    Recibe la información completa del archivo y retorna la lista
    de documentos de estudiantes contenidos en la segunda línea.
    """
    if len(lista) < 2:
        return([])

    estudiantes = lista[1].split()
    return(estudiantes)


def cargar_notas(lista):
    """
    Recibe la información completa del archivo y retorna la matriz
    de notas desde la tercera línea en adelante.

    Las notas se convierten a float. Los valores -1 y -2 se conservan
    como indicadores de curso cancelado o no inscrito.
    """
    notas = []

    if len(lista) < 3:
        return(notas)

    for i in range(2, len(lista)):
        fila_texto = lista[i].split()
        fila = []
        fila_valida = True

        for nota in fila_texto:
            try:
                fila.append(float(nota))
            except ValueError:
                fila_valida = False
                break

        if fila_valida and len(fila) > 0:
            notas.append(fila)

    return(notas)


def cargar_datos(archivo):
    """
    Carga cursos, estudiantes y notas desde el archivo indicado.

    Retorna una lista con la forma:
        [cursos, estudiantes, notas]

    Si el archivo no existe o el formato no coincide, retorna:
        [[], [], []]
    """
    lista = cargar_archivo(archivo)

    if len(lista) == 0:
        return([[], [], []])

    cursos = cargar_cursos(lista)
    estudiantes = cargar_estudiantes(lista)
    notas = cargar_notas(lista)

    if len(cursos) == 0 or len(estudiantes) == 0 or len(notas) == 0:
        return([[], [], []])

    if len(estudiantes) != len(notas):
        return([[], [], []])

    for fila in notas:
        if len(fila) != len(cursos):
            return([[], [], []])

    return([cursos, estudiantes, notas])


def formatear_nota(nota):
    """
    Convierte una nota numérica en texto para escribirla en el archivo.

    -1 y -2 se escriben sin decimales.
    Los demás enteros también se escriben sin .0 para mantener el archivo limpio.
    """
    if nota == -1.0:
        return("-1")
    elif nota == -2.0:
        return("-2")
    elif int(nota) == nota:
        return(str(int(nota)))
    else:
        return(str(nota))


def escribir_codigo(archivo, estudiantes, notas, cursos):
    """
    Sobrescribe el archivo de datos con la información actualizada
    de cursos, estudiantes y matriz de notas.
    """
    abrir = open(archivo, "w", encoding="utf-8")

    linea_cursos = ""
    for i in range(len(cursos)):
        linea_cursos = linea_cursos + cursos[i]

        if i < len(cursos) - 1:
            linea_cursos = linea_cursos + ", "

    abrir.write(linea_cursos + "\n")

    linea_estudiantes = ""
    for i in range(len(estudiantes)):
        linea_estudiantes = linea_estudiantes + estudiantes[i]

        if i < len(estudiantes) - 1:
            linea_estudiantes = linea_estudiantes + " "

    abrir.write(linea_estudiantes + "\n\n")

    for fila in notas:
        linea_notas = ""

        for j in range(len(fila)):
            linea_notas = linea_notas + formatear_nota(fila[j])

            if j < len(fila) - 1:
                linea_notas = linea_notas + " "

        abrir.write(linea_notas + "\n")

    abrir.close()


# -----------------------------------------------------------------
# VALIDACIONES Y UTILIDADES
# -----------------------------------------------------------------

def validar_documento(documento):
    """
    Valida que un documento tenga exactamente 10 caracteres numéricos.
    """
    documento = str(documento).strip()

    if len(documento) != 10:
        return(False)

    numeros = "0123456789"

    for caracter in documento:
        if caracter not in numeros:
            return(False)

    return(True)


def validar_nota(nota):
    """
    Valida una nota académica regular.

    La nota debe ser numérica y estar entre 0.0 y 5.0.
    Los valores especiales -1 y -2 se validan por separado
    en la función de agregar estudiante.
    """
    try:
        valor = float(str(nota).strip())
    except ValueError:
        return(False)

    if valor >= 0.0 and valor <= 5.0:
        return(True)
    else:
        return(False)


def posicion_en_lista(lista, elemento):
    """
    Retorna la posición de un elemento en una lista.
    Si no se encuentra, retorna -1.
    """
    for i in range(len(lista)):
        if lista[i] == elemento:
            return(i)

    return(-1)


def eliminar_por_posicion(lista, posicion):
    """
    Elimina el elemento ubicado en la posición indicada desplazando
    los elementos posteriores una posición hacia la izquierda.
    """
    if posicion < 0 or posicion >= len(lista):
        return

    for i in range(posicion, len(lista) - 1):
        lista[i] = lista[i + 1]

    lista.pop()


def printlist(lista):
    """
    Imprime los elementos de una lista con viñetas.
    """
    for elemento in lista:
        print("-", elemento)


def printlistnum(lista):
    """
    Imprime los elementos de una lista enumerados desde 1.
    """
    contador = 1

    for elemento in lista:
        print(str(contador) + ")", elemento)
        contador = contador + 1


def notasfloat(notas):
    """
    Convierte a float todos los valores de una matriz de notas.

    Se conserva por compatibilidad con versiones anteriores del proyecto.
    Si un valor ya es float, permanece igual.
    """
    for fila in notas:
        for i in range(len(fila)):
            fila[i] = float(fila[i])


# -----------------------------------------------------------------
# ADMINISTRACIÓN DE ESTUDIANTES
# -----------------------------------------------------------------

def eliminar_estudiante(estudiantes, notas):
    """
    Solicita un documento y elimina al estudiante junto con su fila
    correspondiente de notas.
    """
    if len(estudiantes) == 0:
        print("\nNo hay estudiantes cargados.\n")
        return

    while True:
        documento = input("Ingrese el documento del estudiante que desea eliminar: ").strip()

        if not validar_documento(documento):
            print("\nIngresó un documento inválido. Debe tener 10 dígitos numéricos.\n")
        elif documento not in estudiantes:
            print("\nEl estudiante identificado con ese documento no se encuentra en la base de datos.\n")
        else:
            break

    posicion = posicion_en_lista(estudiantes, documento)

    eliminar_por_posicion(estudiantes, posicion)
    eliminar_por_posicion(notas, posicion)

    print("\nEstudiante eliminado exitosamente.\n")


def agregar_estudiante(estudiantes, notas, cursos):
    """
    Solicita los datos de un nuevo estudiante y agrega su documento
    junto con las notas de todos los cursos.
    """
    if len(cursos) == 0:
        print("\nNo hay cursos cargados.\n")
        return

    while True:
        documento = input("Ingrese el documento del estudiante que desea agregar: ").strip()

        if not validar_documento(documento):
            print("\nIngresó un documento inválido. Debe tener 10 dígitos numéricos.\n")
        elif documento in estudiantes:
            print("\nEl estudiante identificado con ese documento ya se encuentra registrado.\n")
        else:
            break

    nuevas_notas = []

    for i in range(len(cursos)):
        curso = cursos[i]

        while True:
            print("\nCurso:", curso)
            nota = input(
                "Ingrese la nota de 0 a 5, -1 si canceló el curso o -2 si no está inscrito: "
            ).strip()

            if nota == "-1" or nota == "-2" or validar_nota(nota):
                nuevas_notas.append(float(nota))
                break
            else:
                print(
                    "\nDato inválido. Ingrese una nota entre 0 y 5, -1 o -2.\n"
                )

    estudiantes.append(documento)
    notas.append(nuevas_notas)

    print("\nEstudiante agregado exitosamente.\n")


# -----------------------------------------------------------------
# PROMEDIOS
# -----------------------------------------------------------------

def promedio_fila_notas(fila):
    """
    Calcula el promedio de una fila de notas ignorando -1 y -2.
    Si no hay notas válidas, retorna 0.
    """
    suma = 0.0
    cantidad = 0

    for nota in fila:
        if nota >= 0:
            suma = suma + nota
            cantidad = cantidad + 1

    if cantidad == 0:
        return(0.0)

    return(round(suma / cantidad, 2))


def promedio_columna_notas(notas, columna):
    """
    Calcula el promedio de una columna de la matriz de notas,
    ignorando -1 y -2.
    """
    suma = 0.0
    cantidad = 0

    for i in range(len(notas)):
        if columna < len(notas[i]):
            nota = notas[i][columna]

            if nota >= 0:
                suma = suma + nota
                cantidad = cantidad + 1

    if cantidad == 0:
        return(0.0)

    return(round(suma / cantidad, 2))


def promedio_estudiantes(estudiantes, notas):
    """
    Calcula y retorna una lista con el promedio de cada estudiante.
    """
    promedios = []

    for i in range(len(estudiantes)):
        promedios.append(promedio_fila_notas(notas[i]))

    return(promedios)


def promedio_estudiantes_print(estudiantes, notas):
    """
    Calcula los promedios de los estudiantes y los imprime por pantalla.
    También retorna la lista de promedios.
    """
    if len(estudiantes) == 0:
        print("\nNo hay estudiantes cargados.\n")
        return([])

    promedios = promedio_estudiantes(estudiantes, notas)

    print("\nPromedio de cada estudiante:")

    for i in range(len(estudiantes)):
        print(
            "- Documento",
            estudiantes[i] + ":",
            promedios[i]
        )

    print("")
    return(promedios)


def promedio_cursos(cursos, notas):
    """
    Calcula los promedios de todos los cursos, los imprime por pantalla
    y retorna una lista con los resultados.
    """
    if len(cursos) == 0:
        print("\nNo hay cursos cargados.\n")
        return([])

    promedios = []

    print("\nPromedio de cada curso:")

    for i in range(len(cursos)):
        promedio = promedio_columna_notas(notas, i)
        promedios.append(promedio)
        print("-", cursos[i] + ":", promedio)

    print("")
    return(promedios)


def promedio_curso(cursos, notas):
    """
    Solicita un curso y muestra el promedio de las notas registradas
    en ese curso.
    """
    if len(cursos) == 0:
        print("\nNo hay cursos cargados.\n")
        return

    print("\nCursos disponibles:")
    printlist(cursos)
    print("")

    while True:
        curso = input("Ingrese el curso del cual desea ver el promedio: ").strip()

        if curso in cursos:
            break
        else:
            print("\nIngrese un curso que se encuentre en la lista.\n")

    posicion = posicion_en_lista(cursos, curso)
    promedio = promedio_columna_notas(notas, posicion)

    print("\nEl promedio de", curso, "es:", promedio, "\n")


# -----------------------------------------------------------------
# BÚSQUEDAS DE NOTAS
# -----------------------------------------------------------------

def valores_unicos_descendentes(lista):
    """
    Retorna una nueva lista con valores únicos ordenados de mayor a menor.
    El ordenamiento se realiza con burbuja para mantener el enfoque del curso.
    """
    unicos = []

    for valor in lista:
        if valor not in unicos:
            unicos.append(valor)

    for i in range(len(unicos)):
        for j in range(0, len(unicos) - i - 1):
            if unicos[j] < unicos[j + 1]:
                unicos[j], unicos[j + 1] = unicos[j + 1], unicos[j]

    return(unicos)


def obtener_tres_notas_mayores(estudiantes, cursos, notas, curso):
    """
    Retorna las tres notas más altas de un curso, agrupando todos los
    estudiantes que empaten en cada una.

    El resultado tiene la forma:
        [[nota, [documentos]], ...]
    """
    resultado = []
    posicion_curso = posicion_en_lista(cursos, curso)

    if posicion_curso == -1:
        return(resultado)

    notas_validas = []

    for i in range(len(estudiantes)):
        nota = notas[i][posicion_curso]

        if nota >= 0:
            notas_validas.append(nota)

    notas_ordenadas = valores_unicos_descendentes(notas_validas)

    cantidad_niveles = 3

    if len(notas_ordenadas) < 3:
        cantidad_niveles = len(notas_ordenadas)

    for i in range(cantidad_niveles):
        nota_objetivo = notas_ordenadas[i]
        documentos = []

        for j in range(len(estudiantes)):
            if notas[j][posicion_curso] == nota_objetivo:
                documentos.append(estudiantes[j])

        resultado.append([nota_objetivo, documentos])

    return(resultado)


def tresNotasMayores(estudiantes, cursos, notas):
    """
    Solicita un curso y muestra las tres notas más altas registradas.
    Si hay empates, muestra todos los documentos asociados.
    """
    if len(cursos) == 0:
        print("\nNo hay cursos cargados.\n")
        return

    print("\nCursos disponibles:")
    printlist(cursos)
    print("")

    while True:
        curso = input("Ingrese el curso del cual desea ver las tres notas mayores: ").strip()

        if curso in cursos:
            break
        else:
            print("\nIngrese un curso que se encuentre en la lista.\n")

    resultado = obtener_tres_notas_mayores(estudiantes, cursos, notas, curso)

    if len(resultado) == 0:
        print("\nNo hay notas válidas registradas para ese curso.\n")
        return

    print("\nTres niveles de notas más altos en", curso + ":")

    for i in range(len(resultado)):
        nota = resultado[i][0]
        documentos = resultado[i][1]

        print("\nNota", str(i + 1) + ":", nota)
        print("Estudiantes con esta nota:")

        for documento in documentos:
            print("-", documento)

    print("")


def obtener_menor_nota_estudiante(estudiantes, cursos, notas, documento):
    """
    Retorna la menor nota válida de un estudiante y los cursos en los
    que obtuvo ese valor.

    El resultado tiene la forma:
        [menor_nota, [cursos]]

    Si no hay información válida, retorna:
        [None, []]
    """
    posicion_estudiante = posicion_en_lista(estudiantes, documento)

    if posicion_estudiante == -1:
        return([None, []])

    menor = None
    cursos_menor = []

    for j in range(len(cursos)):
        nota = notas[posicion_estudiante][j]

        if nota >= 0:
            if menor is None or nota < menor:
                menor = nota
                cursos_menor = [cursos[j]]
            elif nota == menor:
                cursos_menor.append(cursos[j])

    return([menor, cursos_menor])


def menorNotaEstudiante(estudiantes, cursos, notas):
    """
    Solicita un documento y muestra la menor nota válida del estudiante,
    incluyendo el curso o los cursos donde ocurrió.
    """
    if len(estudiantes) == 0:
        print("\nNo hay estudiantes cargados.\n")
        return

    print("\nDocumentos disponibles:")
    printlistnum(estudiantes)
    print("")

    while True:
        documento = input("Ingrese el documento del estudiante del cual desea ver la menor nota: ").strip()

        if documento in estudiantes:
            break
        else:
            print("\nIngrese un documento que se encuentre en la lista.\n")

    resultado = obtener_menor_nota_estudiante(estudiantes, cursos, notas, documento)
    menor = resultado[0]
    cursos_menor = resultado[1]

    if menor is None:
        print("\nEl estudiante no tiene notas válidas registradas.\n")
        return

    print("\nLa menor nota del estudiante", documento, "fue:", menor)
    print("Curso o cursos asociados:")

    for curso in cursos_menor:
        print("-", curso)

    print("")


# -----------------------------------------------------------------
# ORDENAMIENTOS
# -----------------------------------------------------------------

def ordenar_lista_mayor(lista):
    """
    Retorna una copia de la lista ordenada de mayor a menor usando
    ordenamiento burbuja.
    """
    lista2 = list(lista)

    for i in range(len(lista2)):
        for j in range(0, len(lista2) - i - 1):
            if lista2[j] < lista2[j + 1]:
                lista2[j], lista2[j + 1] = lista2[j + 1], lista2[j]

    return(lista2)


def ordenar_lista_menor(lista):
    """
    Retorna una copia de la lista ordenada de menor a mayor usando
    ordenamiento burbuja.
    """
    lista2 = list(lista)

    for i in range(len(lista2)):
        for j in range(0, len(lista2) - i - 1):
            if lista2[j] > lista2[j + 1]:
                lista2[j], lista2[j + 1] = lista2[j + 1], lista2[j]

    return(lista2)


def ordenar_promedios_burbuja(lista):
    """
    Ordena de mayor a menor una lista con elementos:
        [documento, promedio]

    Se usa el algoritmo de burbuja, como exige la práctica.
    """
    for i in range(len(lista)):
        for j in range(0, len(lista) - i - 1):
            if lista[j][1] < lista[j + 1][1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


def ordenarPromedioEstudiantes(estudiantes, notas):
    """
    Imprime a los estudiantes ordenados de mayor a menor según su promedio.
    El ordenamiento se hace con burbuja.
    """
    if len(estudiantes) == 0:
        print("\nNo hay estudiantes cargados.\n")
        return

    promedios = promedio_estudiantes(estudiantes, notas)
    datos = []

    for i in range(len(estudiantes)):
        datos.append([estudiantes[i], promedios[i]])

    ordenar_promedios_burbuja(datos)

    print("\nEstudiantes ordenados por promedio:")

    for fila in datos:
        print("- Documento", fila[0] + ":", fila[1])

    print("")


def ordenar_mayor_selection(lista):
    """
    Ordena de mayor a menor una lista numérica usando selección.

    Se conserva como función general para el ordenamiento por selección.
    """
    for i in range(0, len(lista) - 1):
        mayor = i

        for j in range(i + 1, len(lista)):
            if lista[j] > lista[mayor]:
                mayor = j

        if mayor != i:
            lista[mayor], lista[i] = lista[i], lista[mayor]


def contar_cursos_matriculados(fila_notas):
    """
    Cuenta cuántos cursos tienen una nota válida o registrada.
    Los valores -1 y -2 no se cuentan.
    """
    cantidad = 0

    for nota in fila_notas:
        if nota != -1 and nota != -2:
            cantidad = cantidad + 1

    return(cantidad)


def ordenar_cantidad_cursos_seleccion(lista):
    """
    Ordena de mayor a menor una lista con elementos:
        [documento, cantidad_cursos]

    Se usa ordenamiento por selección, como exige la práctica.
    """
    for i in range(0, len(lista) - 1):
        mayor = i

        for j in range(i + 1, len(lista)):
            if lista[j][1] > lista[mayor][1]:
                mayor = j

        if mayor != i:
            lista[mayor], lista[i] = lista[i], lista[mayor]


def ordenarEstudiantesCantidadCursos(estudiantes, notas):
    """
    Imprime a los estudiantes ordenados por la cantidad de cursos
    matriculados. El ordenamiento se hace con selección.
    """
    if len(estudiantes) == 0:
        print("\nNo hay estudiantes cargados.\n")
        return

    datos = []

    for i in range(len(estudiantes)):
        cantidad = contar_cursos_matriculados(notas[i])
        datos.append([estudiantes[i], cantidad])

    ordenar_cantidad_cursos_seleccion(datos)

    print("\nEstudiantes ordenados por cantidad de cursos matriculados:")

    for fila in datos:
        print("- Documento", fila[0], "tiene", fila[1], "cursos matriculados.")

    print("")


# -----------------------------------------------------------------
# MENÚ
# -----------------------------------------------------------------

def menu():
    """
    Imprime el menú principal del sistema.
    """
    print("=" * 68)
    print("SISTEMA DE GESTIÓN DE NOTAS - PRÁCTICA 7")
    print("=" * 68)
    print("1. Cargar o recargar datos desde archivo.")
    print("2. Eliminar estudiante.")
    print("3. Agregar estudiante.")
    print("4. Ver el promedio de cada estudiante.")
    print("5. Ver el promedio de todos los cursos.")
    print("6. Ver el promedio de un curso específico.")
    print("7. Ver las tres notas mayores de un curso.")
    print("8. Ver la menor nota de un estudiante.")
    print("9. Ordenar estudiantes por promedio.")
    print("10. Ordenar estudiantes por cantidad de cursos.")
    print("11. Guardar cambios y salir.")