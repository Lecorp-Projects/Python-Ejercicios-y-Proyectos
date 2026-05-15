# ============================================================
# Analizador de calificaciones de estudiantes
# ============================================================
# Este programa permite registrar las notas de varios estudiantes
# y consultar distintos resultados mediante un menú interactivo.
#
# Funcionalidades principales:
# - Ingresar nombres y calificaciones entre 0 y 10.
# - Calcular el promedio general del grupo.
# - Identificar al estudiante con la mejor nota.
# - Mostrar los estudiantes aprobados y reprobados.
# - Mostrar los estudiantes que quedan en recuperación.
#
# Debido a la restricción de no usar listas ni estructuras de datos
# similares, la información se almacena en una cadena de texto usando
# separadores, y luego se recorre para realizar los análisis.
# ============================================================

menu = """
Opcion 1) Ingresar datos.
Opcion 2) Ver promedio del grupo y mejor estudiante.
Opcion 3) Ver estudiantes que ganan.
Opcion 4) Ver estudiantes que pierden y recuperación.
Opcion 5) Salir.
"""

opcion = ""
registro = ""
numero = 0


def validar_nota(nota):
    if nota < 0 or nota > 10:
        return False
    return True


def estudiantes():
    while True:
        try:
            numero = int(input("Cuantos estudiantes desea registrar: "))

            if numero > 0:
                return numero
            else:
                print("Ingrese un numero mayor que 0.")

        except ValueError:
            print("Ingrese un numero entero valido.")


def datos():
    numero = estudiantes()
    registro = ""

    for i in range(numero):
        print("\nEstudiante", i + 1)

        nombre = input("Ingrese el nombre del estudiante: ").strip()

        while nombre == "" or "|" in nombre or ";" in nombre:
            print("Ingrese un nombre valido. No puede estar vacio ni contener | o ;")
            nombre = input("Ingrese el nombre del estudiante: ").strip()

        while True:
            try:
                nota = float(input("Ingrese la nota del estudiante: "))

                if validar_nota(nota):
                    break
                else:
                    print("Ingrese una nota valida (entre 0 y 10).")

            except ValueError:
                print("Ingrese un numero valido para la nota.")

        # Se guarda cada estudiante como: nombre|nota;
        registro = registro + nombre + "|" + str(nota) + ";"

    return registro, numero


def promedio(registro, numero):
    suma = 0
    inicio = 0

    while inicio < len(registro):
        separador = registro.find("|", inicio)
        fin = registro.find(";", separador)

        nota = float(registro[separador + 1:fin])

        suma += nota
        inicio = fin + 1

    return suma / numero


def comparaciones(registro, numero):
    mejor_nombre = ""
    mejor_nota = -1

    inicio = 0

    while inicio < len(registro):
        separador = registro.find("|", inicio)
        fin = registro.find(";", separador)

        nombre = registro[inicio:separador]
        nota = float(registro[separador + 1:fin])

        if nota > mejor_nota:
            mejor_nota = nota
            mejor_nombre = nombre

        inicio = fin + 1

    return mejor_nombre, mejor_nota


def mostrar_promedio_y_mejor(registro, numero):
    prom = promedio(registro, numero)
    mejor_nombre, mejor_nota = comparaciones(registro, numero)

    print("\n" + "=" * 40)
    print("PROMEDIO Y MEJOR ESTUDIANTE")
    print("=" * 40)
    print("Promedio del grupo:", round(prom, 2))
    print("Mejor estudiante:", mejor_nombre, "(" + str(mejor_nota) + ")")


def ganadores(registro, numero):
    aprobados = 0
    nombres_aprobados = ""
    primero = True

    inicio = 0

    while inicio < len(registro):
        separador = registro.find("|", inicio)
        fin = registro.find(";", separador)

        nombre = registro[inicio:separador]
        nota = float(registro[separador + 1:fin])

        if nota >= 6:
            aprobados += 1

            if primero:
                nombres_aprobados = nombre + " (" + str(nota) + ")"
                primero = False
            else:
                nombres_aprobados = nombres_aprobados + ", " + nombre + " (" + str(nota) + ")"

        inicio = fin + 1

    print("\n" + "=" * 40)
    print("ESTUDIANTES QUE GANAN")
    print("=" * 40)
    print("Cantidad de estudiantes aprobados:", aprobados)

    if nombres_aprobados == "":
        print("Estudiantes aprobados: Ninguno")
    else:
        print("Estudiantes aprobados:", nombres_aprobados)


def perdedores(registro, numero):
    reprobados = 0
    nombres_reprobados = ""
    recuperacion = ""

    primero_reprobado = True
    primero_recuperacion = True

    inicio = 0

    while inicio < len(registro):
        separador = registro.find("|", inicio)
        fin = registro.find(";", separador)

        nombre = registro[inicio:separador]
        nota = float(registro[separador + 1:fin])

        if nota < 6:
            reprobados += 1

            if primero_reprobado:
                nombres_reprobados = nombre + " (" + str(nota) + ")"
                primero_reprobado = False
            else:
                nombres_reprobados = nombres_reprobados + ", " + nombre + " (" + str(nota) + ")"

        if nota >= 5 and nota < 6:
            if primero_recuperacion:
                recuperacion = nombre + " (" + str(nota) + ")"
                primero_recuperacion = False
            else:
                recuperacion = recuperacion + ", " + nombre + " (" + str(nota) + ")"

        inicio = fin + 1

    print("\n" + "=" * 40)
    print("ESTUDIANTES QUE PIERDEN")
    print("=" * 40)
    print("Cantidad de estudiantes reprobados:", reprobados)

    if nombres_reprobados == "":
        print("Estudiantes reprobados: Ninguno")
    else:
        print("Estudiantes reprobados:", nombres_reprobados)

    if recuperacion == "":
        print("Estudiantes en recuperación (5 a 5.9): Ninguno")
    else:
        print("Estudiantes en recuperación (5 a 5.9):", recuperacion)

print("Bienvenido al programa de notas de estudiantes.")
while opcion != "5":
    print(menu)
    opcion = input("Ingrese una opcion entre 1 y 5: ")

    if opcion == "1":
        registro, numero = datos()
        print("\nDatos registrados correctamente.")

    elif opcion == "2":
        if numero == 0:
            print("\nPrimero debe ingresar los datos de los estudiantes.")
        else:
            mostrar_promedio_y_mejor(registro, numero)

    elif opcion == "3":
        if numero == 0:
            print("\nPrimero debe ingresar los datos de los estudiantes.")
        else:
            ganadores(registro, numero)

    elif opcion == "4":
        if numero == 0:
            print("\nPrimero debe ingresar los datos de los estudiantes.")
        else:
            perdedores(registro, numero)

    elif opcion == "5":
        print("\nGracias por usar el programa, hasta luego!")

    else:
        print("\nIngrese un dato valido.")