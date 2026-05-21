"""
Sistema de gestión de estudiantes

Funciones:
- agregar_estudiante(base_datos, nombre)
- agregar_nota(base_datos, nombre, nota)
- promedio_estudiante(base_datos, nombre)
- mejor_estudiante(base_datos)
- mostrar_resumen(base_datos)
- menu()

Usa diccionarios y funciones básicas de Python.
"""

def agregar_estudiante(base_datos, nombre):
    """Agrega un estudiante con lista vacía de notas."""
    if nombre in base_datos:
        return False
    base_datos[nombre] = []
    return True


def agregar_nota(base_datos, nombre, nota):
    """Agrega una nota float entre 0 y 10 al estudiante."""
    if nombre not in base_datos:
        return False
    try:
        n = float(nota)
    except (TypeError, ValueError):
        return False
    if not (0 <= n <= 10):
        return False
    base_datos[nombre].append(n)
    return True


def eliminar_estudiante(base_datos, nombre):
    """Elimina un estudiante de la base de datos."""
    if nombre not in base_datos:
        return False
    del base_datos[nombre]
    return True


def promedio_estudiante(base_datos, nombre):
    """Retorna promedio o None si no existe o no tiene notas."""
    if nombre not in base_datos:
        return None
    notas = base_datos[nombre]
    if not notas:
        return None
    return sum(notas) / len(notas)


def mejor_estudiante(base_datos):
    """Retorna nombre del estudiante con mayor promedio o None si no hay promedios."""
    mejor = None
    mejor_prom = -1
    for nombre in base_datos:
        prom = promedio_estudiante(base_datos, nombre)
        if prom is None:
            continue
        if prom > mejor_prom:
            mejor_prom = prom
            mejor = nombre
    return mejor


def mostrar_resumen(base_datos):
    """Muestra tabla: nombre, promedio (2 dec), estado."""
    if not base_datos:
        print("No hay estudiantes en la base de datos.")
        return
    encabezado = f"{'Nombre':30} {'Promedio':>8} {'Estado':>10}"
    print(encabezado)
    print('-' * len(encabezado))
    for nombre, notas in base_datos.items():
        prom = promedio_estudiante(base_datos, nombre)
        if prom is None:
            prom_str = 'N/A'
            estado = 'Sin notas'
        else:
            prom_str = f"{prom:.2f}"
            estado = 'Aprobado' if prom >= 6 else 'Reprobado'
        print(f"{nombre:30} {prom_str:>8} {estado:>10}")


def menu():
    base = {}
    while True:
        print('\n--- Menú ---')
        print('1. Agregar estudiante')
        print('2. Agregar nota')
        print('3. Mostrar promedio de un estudiante')
        print('4. Mostrar mejor estudiante')
        print('5. Mostrar resumen')
        print('6. Eliminar estudiante')
        print('7. Salir')
        opcion = input('Elija una opción: ').strip()
        if opcion == '1':
            nombre = input('Nombre del estudiante: ').strip()
            if agregar_estudiante(base, nombre):
                print('Estudiante agregado.')
            else:
                print('El estudiante ya existe.')
        elif opcion == '2':
            nombre = input('Nombre del estudiante: ').strip()
            nota = input('Nota (0-10): ').strip()
            if agregar_nota(base, nombre, nota):
                print('Nota agregada.')
            else:
                print('Error al agregar la nota. Revise nombre/valor.')
        elif opcion == '3':
            nombre = input('Nombre del estudiante: ').strip()
            prom = promedio_estudiante(base, nombre)
            if prom is None:
                print('No existe el estudiante o no tiene notas.')
            else:
                print(f'Promedio de {nombre}: {prom:.2f}')
        elif opcion == '4':
            mejor = mejor_estudiante(base)
            if mejor is None:
                print('No hay estudiantes con notas.')
            else:
                print(f'Mejor estudiante: {mejor} (Promedio: {promedio_estudiante(base, mejor):.2f})')
        elif opcion == '5':
            mostrar_resumen(base)
        elif opcion == '6':
            nombre = input('Nombre del estudiante a eliminar: ').strip()
            if eliminar_estudiante(base, nombre):
                print('Estudiante eliminado.')
            else:
                print('No existe el estudiante.')
        elif opcion == '7':
            print('Saliendo...')
            break
        else:
            print('Opción inválida.')


if __name__ == '__main__':
    menu()
