# ============================================================
# Utilidades generales del sistema de monitoreo ambiental
# ============================================================
# Este módulo reúne funciones de apoyo utilizadas por el programa:
# validaciones básicas, limpieza visual de la consola e impresión
# organizada de tablas de datos.
# ============================================================


def validar_nombre(nombre):
    """
    Valida que un nombre contenga únicamente letras y espacios.
    Se admiten vocales con tilde, la letra ñ y la ü.

    Retorna True si es válido y False en caso contrario.
    """
    nombre = nombre.strip()

    if nombre == "":
        return(False)

    letras = "abcdefghijklmnñopqrstuvwxyzáéíóúü"

    for caracter in nombre.lower():
        if caracter not in letras and caracter != " ":
            return(False)

    return(True)


def validar_documento(documento):
    """
    Valida que un documento tenga exactamente 10 caracteres numéricos.

    Retorna True si es válido y False en caso contrario.
    """
    documento = str(documento)

    if len(documento) != 10:
        return(False)

    numeros = "0123456789"

    for caracter in documento:
        if caracter not in numeros:
            return(False)

    return(True)


def es_bisiesto(anio):
    """
    Retorna True si el año recibido es bisiesto y False en caso contrario.
    """
    if anio % 400 == 0:
        return(True)
    elif anio % 100 == 0:
        return(False)
    elif anio % 4 == 0:
        return(True)
    else:
        return(False)


def validar_fecha(fecha):
    """
    Valida que un string corresponda a una fecha real con formato yyyy-mm-dd.

    Retorna True si la fecha es válida y False en caso contrario.
    """
    if len(fecha) != 10:
        return(False)

    if fecha[4] != "-" or fecha[7] != "-":
        return(False)

    anio = fecha[0:4]
    mes = fecha[5:7]
    dia = fecha[8:10]

    if not anio.isdigit() or not mes.isdigit() or not dia.isdigit():
        return(False)

    anio = int(anio)
    mes = int(mes)
    dia = int(dia)

    if mes < 1 or mes > 12:
        return(False)

    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if es_bisiesto(anio):
        dias_mes[1] = 29

    if dia < 1 or dia > dias_mes[mes - 1]:
        return(False)

    return(True)


def limpiar_pantalla():
    """
    Imprime varias líneas en blanco para separar visualmente los menús.
    """
    print("\n" * 20)


def imprimir_tabla(tabla, ancho, encabezado=None):
    """
    Imprime una tabla sencilla en consola.

    Argumentos:
        tabla: Lista donde cada elemento representa una fila.
        ancho: Entero para aplicar el mismo ancho a todas las columnas,
               o lista de enteros con el ancho deseado para cada columna.
        encabezado: Lista opcional con los títulos de las columnas.
    """

    def dividir_fila(anchos, separador="-"):
        linea = ""
        for i in range(len(anchos)):
            linea = linea + "+" + separador * (anchos[i] - 1)
        linea = linea[:-1] + "+"
        print(linea)

    def imprimir_celda(texto, impresos, relleno):
        if type(texto) == type(0.0):
            texto = "{:^7.2f}".format(texto)
        else:
            texto = str(texto)

        texto = texto.replace("\n", " ").replace("\t", " ")

        if impresos + relleno < len(texto):
            print(texto[impresos:impresos + relleno], end="")
            impresos = impresos + relleno
        elif impresos >= len(texto):
            print(" " * relleno, end="")
        else:
            print(texto[impresos:], end="")
            print(" " * (relleno - (len(texto) - impresos)), end="")
            impresos = len(texto)

        return(impresos)

    def imprimir_fila(fila, anchos):
        impresos = []
        alto = 1

        for i in range(len(fila)):
            impresos.append(0)

            if type(fila[i]) == type(0.0):
                texto = "{:7.2f}".format(fila[i])
            else:
                texto = str(fila[i])

            capacidad = anchos[i] - 4

            if capacidad <= 0:
                capacidad = 1

            alto_fila = len(texto) // capacidad

            if len(texto) % capacidad != 0:
                alto_fila = alto_fila + 1

            if alto_fila > alto:
                alto = alto_fila

        for i in range(alto):
            print("| ", end="")

            for j in range(len(fila)):
                relleno = anchos[j] - 3

                if j == len(fila) - 1:
                    relleno = anchos[j] - 4
                    impresos[j] = imprimir_celda(fila[j], impresos[j], relleno)
                    print(" |")
                else:
                    impresos[j] = imprimir_celda(fila[j], impresos[j], relleno)
                    print(" | ", end="")

    if len(tabla) == 0:
        print("No hay datos para mostrar.")
        return

    if type(tabla[0]) is not list:
        print("Error. La tabla debe estar formada por filas en listas.")
        return

    numero_columnas = len(tabla[0])

    if type(ancho) == type(0):
        anchos = [ancho + 3] * numero_columnas
    elif type(ancho) is list:
        anchos = []
        for valor in ancho:
            anchos.append(valor + 3)
    else:
        print("Error. El ancho debe ser un entero o una lista de enteros.")
        return

    if len(anchos) != numero_columnas:
        print("Error. La cantidad de columnas no coincide con los tamaños dados.")
        return

    anchos[-1] = anchos[-1] + 1

    if encabezado is not None:
        if len(encabezado) != numero_columnas:
            print("Error. El encabezado no coincide con la cantidad de columnas.")
            return

        dividir_fila(anchos, "=")
        imprimir_fila(encabezado, anchos)
        dividir_fila(anchos, "=")
    else:
        dividir_fila(anchos)

    for fila in tabla:
        if len(fila) != numero_columnas:
            print("Error. Una fila no coincide con la cantidad de columnas.")
            return

        imprimir_fila(fila, anchos)
        dividir_fila(anchos)