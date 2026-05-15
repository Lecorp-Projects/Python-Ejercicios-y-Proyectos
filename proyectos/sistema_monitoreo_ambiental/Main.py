# ============================================================
# Programa principal del sistema de monitoreo ambiental
# ============================================================
# Este archivo contiene los menús y el flujo de interacción con
# el usuario. La lógica de procesamiento y manejo de archivos se
# encuentra en funciones.py.
# ============================================================

import os

from funciones import (
    autenticar_usuario,
    crear_estacion,
    crear_registro,
    crear_usuario,
    depurar_registros,
    editar_estacion,
    editar_usuario,
    eliminar_estacion,
    eliminar_usuario,
    estaciones_por_municipio,
    imprimir_lista_numerada,
    lista_municipios,
    mostrar_estadisticas,
    mostrar_medidas_estacion,
)

# Se obtiene la ruta absoluta de la carpeta donde se encuentra este archivo Main.py.
# Esto permite que el programa encuentre correctamente los archivos .txt aunque se
# ejecute desde otra ubicación, por ejemplo desde VS Code, Spyder o una terminal
# cuyo directorio actual no sea exactamente la carpeta del proyecto.
#
# Luego, con os.path.join(), se construyen las rutas completas hacia los archivos
# registros_.txt y registros_v2.txt, asegurando que el programa siempre trabaje
# con los archivos que están dentro de esta misma carpeta.

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_DATOS = os.path.join(BASE_DIR, "registros_.txt")
ARCHIVO_DATOS_V2 = os.path.join(BASE_DIR, "registros_v2.txt")


def menu_inicial():
    """
    Muestra el menú inicial del sistema.
    """
    print("\n" + "=" * 55)
    print("SISTEMA DE MONITOREO AMBIENTAL")
    print("=" * 55)
    print("1) Usuario registrado.")
    print("2) Usuario visitante.")
    print("3) Salir del sistema.")


def menu_visitante():
    """
    Permite a un visitante consultar estadísticas básicas.
    """
    while True:
        print("\n--- Menú de visitante ---")
        print("1) Visualizar estadísticas.")
        print("2) Volver al menú inicial.")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            mostrar_estadisticas(ARCHIVO_DATOS)
        elif opcion == "2":
            return
        else:
            print("Ingrese una opción válida.")


def menu_gestion_usuarios(documento_actual):
    """
    Menú administrativo para crear, editar y eliminar usuarios.
    """
    while True:
        print("\n--- Gestión de usuarios ---")
        print("1) Crear usuario.")
        print("2) Editar usuario.")
        print("3) Eliminar usuario.")
        print("4) Volver.")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            crear_usuario(ARCHIVO_DATOS)
        elif opcion == "2":
            editar_usuario(ARCHIVO_DATOS)
        elif opcion == "3":
            eliminar_usuario(documento_actual, ARCHIVO_DATOS)
        elif opcion == "4":
            return
        else:
            print("Ingrese una opción válida.")


def menu_gestion_estaciones():
    """
    Menú administrativo para crear, editar y eliminar estaciones.
    """
    while True:
        print("\n--- Gestión de estaciones ---")
        print("1) Crear estación.")
        print("2) Editar estación.")
        print("3) Eliminar estación.")
        print("4) Volver.")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            crear_estacion(ARCHIVO_DATOS)
        elif opcion == "2":
            editar_estacion(ARCHIVO_DATOS)
        elif opcion == "3":
            eliminar_estacion(ARCHIVO_DATOS)
        elif opcion == "4":
            return
        else:
            print("Ingrese una opción válida.")


def menu_administrador(documento_actual, nombre_usuario):
    """
    Muestra las opciones disponibles para un administrador.
    """
    while True:
        print("\n" + "=" * 55)
        print("MENÚ DE ADMINISTRADOR -", nombre_usuario)
        print("=" * 55)
        print("1) Gestionar usuarios.")
        print("2) Gestionar estaciones.")
        print("3) Depurar registros entre dos versiones del archivo.")
        print("4) Cerrar sesión.")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            menu_gestion_usuarios(documento_actual)
        elif opcion == "2":
            menu_gestion_estaciones()
        elif opcion == "3":
            depurar_registros(ARCHIVO_DATOS, ARCHIVO_DATOS_V2)
        elif opcion == "4":
            print("Sesión cerrada.")
            return
        else:
            print("Ingrese una opción válida.")


def seleccionar_municipio():
    """
    Permite elegir un municipio o volver al menú anterior.

    Retorna el municipio seleccionado o una cadena vacía.
    """
    municipios = lista_municipios(ARCHIVO_DATOS)

    if len(municipios) == 0:
        print("No hay municipios disponibles.")
        return("")

    while True:
        print("\nSeleccione el municipio de la estación:")
        imprimir_lista_numerada(municipios)
        print("0) Volver.")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "0":
            return("")

        if opcion.isdigit():
            posicion = int(opcion)

            if posicion >= 1 and posicion <= len(municipios):
                return(municipios[posicion - 1])

        print("Seleccione una opción válida.")


def seleccionar_estacion(municipio):
    """
    Permite elegir una estación de un municipio o volver.

    Retorna el código de estación o una cadena vacía.
    """
    estaciones = estaciones_por_municipio(ARCHIVO_DATOS, municipio)

    if len(estaciones) == 0:
        print("No hay estaciones registradas en ese municipio.")
        return("")

    while True:
        print("\nEstaciones disponibles en", municipio + ":")

        nombres = []

        for estacion in estaciones:
            nombres.append(estacion[0] + " - " + estacion[1])

        imprimir_lista_numerada(nombres)
        print("0) Volver a elegir municipio.")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "0":
            return("")

        if opcion.isdigit():
            posicion = int(opcion)

            if posicion >= 1 and posicion <= len(estaciones):
                return(estaciones[posicion - 1][0])

        print("Seleccione una estación válida.")


def menu_estacion_operador(codigo_estacion):
    """
    Muestra las opciones disponibles para una estación seleccionada.
    """
    while True:
        print("\n--- Estación seleccionada ---")
        print("1) Mostrar medidas registradas.")
        print("2) Ingresar nuevas medidas.")
        print("3) Volver a elegir estación.")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            mostrar_medidas_estacion(ARCHIVO_DATOS, codigo_estacion)
        elif opcion == "2":
            crear_registro(ARCHIVO_DATOS, codigo_estacion)
        elif opcion == "3":
            return
        else:
            print("Ingrese una opción válida.")


def menu_operador(nombre_usuario):
    """
    Flujo de trabajo del operador:
    municipio -> estación -> consultar o registrar medidas.
    """
    while True:
        print("\n" + "=" * 55)
        print("MENÚ DE OPERADOR -", nombre_usuario)
        print("=" * 55)
        print("1) Seleccionar municipio y estación.")
        print("2) Cerrar sesión.")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            while True:
                municipio = seleccionar_municipio()

                if municipio == "":
                    break

                while True:
                    codigo = seleccionar_estacion(municipio)

                    if codigo == "":
                        break

                    menu_estacion_operador(codigo)

        elif opcion == "2":
            print("Sesión cerrada.")
            return
        else:
            print("Ingrese una opción válida.")


def iniciar_sesion():
    """
    Autentica a un usuario registrado y abre el menú correspondiente
    a su rol.
    """
    datos_usuario = autenticar_usuario(ARCHIVO_DATOS)

    if len(datos_usuario) == 0:
        return

    documento = datos_usuario[0]
    nombre = datos_usuario[1]
    rol = datos_usuario[2]

    if rol == "Administrador":
        menu_administrador(documento, nombre)
    elif rol == "Operador":
        menu_operador(nombre)
    else:
        print("El usuario tiene un rol no reconocido.")


def main():
    """
    Función principal del programa.
    """
    while True:
        menu_inicial()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            iniciar_sesion()
        elif opcion == "2":
            menu_visitante()
        elif opcion == "3":
            print("Gracias por usar el sistema. Hasta luego.")
            break
        else:
            print("Ingrese una opción válida.")


if __name__ == "__main__":
    main()