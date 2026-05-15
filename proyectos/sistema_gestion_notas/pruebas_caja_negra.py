# ============================================================
# Pruebas de caja negra del sistema de gestión de notas
# ============================================================
# Este archivo contiene pruebas automáticas sencillas sobre funciones
# del proyecto. Se usan assert para verificar que los resultados
# obtenidos coincidan con los esperados.
# ============================================================

from funciones import (
    obtener_tres_notas_mayores,
    ordenar_promedios_burbuja,
    promedio_cursos,
    validar_documento,
)


def prueba_validar_documento():
    """
    Verifica documentos válidos e inválidos.
    """
    assert validar_documento("1234567890") == True
    assert validar_documento("123456789") == False
    assert validar_documento("12345678901") == False
    assert validar_documento("12345a7890") == False

    print("Prueba 1 superada: validar_documento.")


def prueba_promedio_cursos():
    """
    Verifica que el promedio de cursos ignore los valores -1 y -2.
    """
    cursos = ["Curso1", "Curso2", "Curso3"]

    notas = [
        [4.0, 3.5, 4.2],
        [2.5, -1.0, 3.8],
        [4.5, 2.0, -2.0],
        [3.0, 4.0, 2.5],
    ]

    resultado = promedio_cursos(cursos, notas)
    esperado = [3.5, 3.17, 3.5]

    assert resultado == esperado

    print("Prueba 2 superada: promedio_cursos.")


def prueba_tres_notas_mayores_con_empates():
    """
    Verifica que se reporten empates al buscar las tres notas mayores.
    """
    estudiantes = [
        "1000000001",
        "1000000002",
        "1000000003",
        "1000000004",
        "1000000005",
    ]

    cursos = ["Curso1"]

    notas = [
        [5.0],
        [4.8],
        [4.8],
        [4.2],
        [3.5],
    ]

    resultado = obtener_tres_notas_mayores(estudiantes, cursos, notas, "Curso1")

    esperado = [
        [5.0, ["1000000001"]],
        [4.8, ["1000000002", "1000000003"]],
        [4.2, ["1000000004"]],
    ]

    assert resultado == esperado

    print("Prueba 3 superada: obtener_tres_notas_mayores.")


def prueba_ordenamiento_gran_volumen():
    """
    Verifica el ordenamiento por promedio con un volumen mayor de datos.
    """
    datos = []

    for i in range(200):
        documento = "E" + str(i)
        promedio = float((200 - i) % 17)
        datos.append([documento, promedio])

    ordenar_promedios_burbuja(datos)

    for i in range(len(datos) - 1):
        assert datos[i][1] >= datos[i + 1][1]

    print("Prueba 4 superada: ordenamiento con gran volumen de datos.")


def main():
    """
    Ejecuta todas las pruebas.
    """
    print("\nINICIO DE PRUEBAS DE CAJA NEGRA\n")

    prueba_validar_documento()
    prueba_promedio_cursos()
    prueba_tres_notas_mayores_con_empates()
    prueba_ordenamiento_gran_volumen()

    print("\nTodas las pruebas finalizaron correctamente.\n")


if __name__ == "__main__":
    main()