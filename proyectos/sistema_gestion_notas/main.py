# ============================================================
# Programa principal del sistema de gestión de notas
# ============================================================
# Este archivo controla el flujo del programa, muestra el menú,
# permite cargar la base de datos y conecta cada opción con las
# funciones definidas en funciones.py.
# ============================================================

import os

from funciones import (
    agregar_estudiante,
    cargar_datos,
    eliminar_estudiante,
    escribir_codigo,
    menorNotaEstudiante,
    menu,
    ordenarEstudiantesCantidadCursos,
    ordenarPromedioEstudiantes,
    promedio_curso,
    promedio_cursos,
    promedio_estudiantes_print,
    tresNotasMayores,
)


# Se obtiene la carpeta real donde se encuentra este archivo main.py.
# Así el programa puede localizar database_p7.txt aunque se ejecute
# desde otra ruta en VS Code, Spyder o la terminal.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_PREDETERMINADO = os.path.join(BASE_DIR, "database_p7.txt")


def solicitar_archivo():
    """
    Solicita la ruta del archivo de datos.

    Si el usuario presiona Enter sin escribir nada, se usa
    database_p7.txt ubicado en la misma carpeta de main.py.
    """
    print("\nArchivo predeterminado:", ARCHIVO_PREDETERMINADO)
    archivo = input(
        "Ingrese la ruta del archivo de datos o presione Enter para usar el predeterminado: "
    ).strip()

    if archivo == "":
        return(ARCHIVO_PREDETERMINADO)

    return(archivo)


def mostrar_estado_carga(archivo, cursos, estudiantes, notas):
    """
    Muestra un resumen corto de la información cargada.
    """
    print("\nDatos cargados correctamente.")
    print("Archivo:", archivo)
    print("Cursos cargados:", len(cursos))
    print("Estudiantes cargados:", len(estudiantes))
    print("Filas de notas cargadas:", len(notas))
    print("")


def datos_disponibles(cursos, estudiantes, notas):
    """
    Retorna True si ya hay datos cargados para trabajar.
    """
    if len(cursos) > 0 and len(estudiantes) > 0 and len(notas) > 0:
        return(True)

    return(False)


def main():
    """
    Función principal del programa.
    """
    archivo_actual = ""
    cursos = []
    estudiantes = []
    notas = []

    print("\nBIENVENIDO AL SISTEMA DE GESTIÓN DE NOTAS DE LA UNIVERSIDAD DE ANTIOQUIA.\n")

    while True:
        menu()
        print("")
        opcion = input("Ingrese el número de la opción deseada: ").strip()

        if opcion == "1":
            archivo_actual = solicitar_archivo()
            datos = cargar_datos(archivo_actual)
            cursos = datos[0]
            estudiantes = datos[1]
            notas = datos[2]

            if datos_disponibles(cursos, estudiantes, notas):
                mostrar_estado_carga(archivo_actual, cursos, estudiantes, notas)
            else:
                print(
                    "\nNo fue posible cargar la información. "
                    "Revise que el archivo exista y tenga el formato esperado.\n"
                )
                archivo_actual = ""

        elif opcion == "11":
            if datos_disponibles(cursos, estudiantes, notas) and archivo_actual != "":
                escribir_codigo(archivo_actual, estudiantes, notas, cursos)
                print("\nCambios guardados correctamente en:", archivo_actual)

            print("Gracias por usar el sistema. ¡Hasta luego!")
            break

        elif not datos_disponibles(cursos, estudiantes, notas):
            print("\nPrimero debe cargar los datos usando la opción 1.\n")

        elif opcion == "2":
            eliminar_estudiante(estudiantes, notas)

        elif opcion == "3":
            agregar_estudiante(estudiantes, notas, cursos)

        elif opcion == "4":
            promedio_estudiantes_print(estudiantes, notas)

        elif opcion == "5":
            promedio_cursos(cursos, notas)

        elif opcion == "6":
            promedio_curso(cursos, notas)

        elif opcion == "7":
            tresNotasMayores(estudiantes, cursos, notas)

        elif opcion == "8":
            menorNotaEstudiante(estudiantes, cursos, notas)

        elif opcion == "9":
            ordenarPromedioEstudiantes(estudiantes, notas)

        elif opcion == "10":
            ordenarEstudiantesCantidadCursos(estudiantes, notas)

        else:
            print("\nPor favor ingrese un número válido entre 1 y 11.\n")


if __name__ == "__main__":
    main()