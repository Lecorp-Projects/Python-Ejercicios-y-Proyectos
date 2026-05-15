# ============================================================
# Juego para adivinar un número aleatorio
# ============================================================
# Este programa genera un número secreto dentro de un rango definido
# y le da al usuario una cantidad limitada de intentos para adivinarlo.
#
# En cada intento:
# - Se solicita un número al usuario.
# - Se valida que la entrada sea numérica.
# - Se valida que el número esté dentro del rango permitido.
# - Se informa si el número secreto es mayor o menor.
#
# El intento solo cuenta cuando el usuario ingresa un número válido
# dentro del rango establecido.
#
# Este ejercicio practica:
# - Funciones.
# - Ciclos while.
# - Condicionales.
# - Validación de entradas.
# - Uso de números aleatorios con randint.
# ============================================================

from random import randint


def mostrar_bienvenida(minimo, maximo, intentos_maximos):
    """
    Muestra el mensaje inicial del juego.
    """
    print("¡Bienvenido al juego de adivinar el número!")
    print("Tienes", intentos_maximos, "intentos para adivinar el número entre", minimo, "y", str(maximo) + ".")
    print("=" * 55)


def pedir_numero(minimo, maximo):
    """
    Solicita al usuario un número y valida que sea correcto.

    Retorna:
    - El número como entero si la entrada es válida.
    - None si la entrada no es válida o está fuera de rango.
    """
    entrada = input("Introduce tu número entre " + str(minimo) + " y " + str(maximo) + ": ")

    if not entrada.isdigit():
        print("Por favor, introduce un número válido.")
        print("Este intento no se contará.")
        return(None)

    numero = int(entrada)

    if numero < minimo or numero > maximo:
        print("Número fuera de rango. Por favor, introduce un número entre", minimo, "y", str(maximo) + ".")
        print("Este intento no se contará.")
        return(None)

    return(numero)


def revisar_intento(numero_usuario, numero_secreto):
    """
    Compara el número ingresado con el número secreto.

    Retorna:
    - True si el usuario adivinó.
    - False si todavía no lo ha adivinado.
    """
    if numero_usuario < numero_secreto:
        print("Demasiado bajo. Intenta de nuevo.")
        return(False)

    elif numero_usuario > numero_secreto:
        print("Demasiado alto. Intenta de nuevo.")
        return(False)

    else:
        return(True)


def jugar():
    """
    Ejecuta el flujo completo del juego.
    """
    minimo = 1
    maximo = 100
    intentos_maximos = 8

    numero_secreto = randint(minimo, maximo)
    intentos_realizados = 0
    adivinado = False

    mostrar_bienvenida(minimo, maximo, intentos_maximos)

    while intentos_realizados < intentos_maximos and not adivinado:
        intentos_restantes = intentos_maximos - intentos_realizados
        print("\nIntentos restantes:", intentos_restantes)

        numero_usuario = pedir_numero(minimo, maximo)

        if numero_usuario == None:
            continue

        intentos_realizados = intentos_realizados + 1
        adivinado = revisar_intento(numero_usuario, numero_secreto)

        if adivinado:
            print("¡Felicidades! Has adivinado el número", numero_secreto, "en", intentos_realizados, "intentos.")

    if not adivinado:
        print("\nSe terminaron los intentos.")
        print("El número secreto era:", numero_secreto)


jugar()