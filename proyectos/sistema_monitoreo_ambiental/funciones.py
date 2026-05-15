# ============================================================
# Funciones del sistema de monitoreo ambiental
# ============================================================
# Este módulo contiene la lógica principal del proyecto:
# carga y escritura del archivo de datos, autenticación de usuarios,
# gestión de usuarios y estaciones, registro de medidas, reportes
# de depuración y cálculo de estadísticas para visitantes.
# ============================================================

from datetime import datetime, timedelta

from utilidades import (
    imprimir_tabla,
    validar_documento,
    validar_fecha,
    validar_nombre,
)


# -----------------------------------------------------------------
# FUNCIONES GENERALES DE ARCHIVOS Y APOYO
# -----------------------------------------------------------------

def cargar_archivo(archivo):
    """
    Lee un archivo de texto y retorna una lista con sus líneas,
    sin incluir los saltos de línea al final.
    """
    texto = []

    try:
        abrir = open(archivo, "r", encoding="utf-8")
        lineas = abrir.readlines()
        abrir.close()

        for linea in lineas:
            linea = linea.rstrip("\n")
            if linea != "":
                texto.append(linea)

    except FileNotFoundError:
        return([])

    return(texto)


def escribir_archivo(archivo, lineas):
    """
    Sobrescribe un archivo usando las líneas recibidas.
    """
    abrir = open(archivo, "w", encoding="utf-8")

    for linea in lineas:
        abrir.write(linea + "\n")

    abrir.close()


def agregar_linea(archivo, linea):
    """
    Añade una línea al final del archivo.
    """
    abrir = open(archivo, "a", encoding="utf-8")
    abrir.write(linea + "\n")
    abrir.close()


def archivo_existe(archivo):
    """
    Retorna True si el archivo puede abrirse en modo lectura.
    """
    try:
        abrir = open(archivo, "r", encoding="utf-8")
        abrir.close()
        return(True)
    except FileNotFoundError:
        return(False)


def imprimir_lista(lista):
    """
    Imprime los elementos de una lista usando viñetas.
    """
    for elemento in lista:
        print("-", elemento)


def imprimir_lista_numerada(lista):
    """
    Imprime los elementos de una lista usando numeración desde 1.
    """
    contador = 1

    for elemento in lista:
        print(str(contador) + ")", elemento)
        contador = contador + 1


def insertar_usuario_en_archivo(archivo, linea_usuario):
    """
    Inserta un usuario antes de la línea de municipios.
    Si no encuentra la línea de municipios, lo agrega al final.
    """
    lineas = cargar_archivo(archivo)
    nuevas_lineas = []
    insertado = False

    for linea in lineas:
        if not insertado and len(linea) > 0 and linea[0] == ":":
            nuevas_lineas.append(linea_usuario)
            insertado = True

        nuevas_lineas.append(linea)

    if not insertado:
        nuevas_lineas.append(linea_usuario)

    escribir_archivo(archivo, nuevas_lineas)


def insertar_estacion_en_archivo(archivo, linea_estacion):
    """
    Inserta una estación antes de la línea de variables.
    Si no encuentra la línea de variables, la agrega al final.
    """
    lineas = cargar_archivo(archivo)
    nuevas_lineas = []
    insertada = False

    for linea in lineas:
        if not insertada and "[" in linea and "]" in linea:
            nuevas_lineas.append(linea_estacion)
            insertada = True

        nuevas_lineas.append(linea)

    if not insertada:
        nuevas_lineas.append(linea_estacion)

    escribir_archivo(archivo, nuevas_lineas)


def normalizar_rol(rol):
    """
    Retorna 'Administrador' u 'Operador' si el texto recibido
    corresponde a uno de esos roles. Si no corresponde, retorna ''.
    """
    rol = rol.strip().lower()

    if rol == "administrador":
        return("Administrador")
    elif rol == "operador":
        return("Operador")
    else:
        return("")


def verificar_rol(rol):
    """
    Retorna True si el rol es Administrador u Operador.
    """
    if normalizar_rol(rol) != "":
        return(True)
    else:
        return(False)


def validar_contrasena(contrasena):
    """
    Retorna True si la contraseña tiene al menos 4 caracteres.
    """
    if len(contrasena) >= 4:
        return(True)
    else:
        return(False)


def verificar_contrasena(contrasena, confirmacion):
    """
    Retorna True si la contraseña y su confirmación coinciden.
    """
    if contrasena == confirmacion:
        return(True)
    else:
        return(False)


def texto_no_vacio(texto):
    """
    Retorna True si el texto no queda vacío al quitar espacios externos.
    """
    if texto.strip() == "":
        return(False)
    else:
        return(True)


def nombre_estacion_valido(nombre):
    """
    Valida que el nombre de una estación no esté vacío y no use
    separadores que afectarían el formato del archivo de datos.
    """
    if not texto_no_vacio(nombre):
        return(False)

    prohibidos = ",;[]{}<>"

    for caracter in nombre:
        if caracter in prohibidos:
            return(False)

    return(True)


# -----------------------------------------------------------------
# CARGA DE DATOS DESDE LA BASE DE TEXTO
# -----------------------------------------------------------------

def cargar_usuarios(archivo):
    """
    Carga los usuarios registrados desde el archivo de datos.

    Retorna un diccionario:
        documento -> [nombre, contrasena, rol]
    """
    lineas = cargar_archivo(archivo)
    usuarios = {}

    for linea in lineas:
        if len(linea) >= 2 and linea[0] == "<" and linea[-1] == ">":
            datos = linea[1:-1].split(";")

            if len(datos) == 4:
                documento = datos[0]
                nombre = datos[1]
                contrasena = datos[2]
                rol = datos[3]

                usuarios[documento] = [nombre, contrasena, rol]

    return(usuarios)


def lista_municipios(archivo):
    """
    Extrae la lista de municipios disponibles en el archivo de datos.
    """
    lineas = cargar_archivo(archivo)

    for linea in lineas:
        if len(linea) > 0 and linea[0] == ":":
            municipios = linea[1:].split(",")
            return(municipios)

    return([])


def cargar_estaciones(archivo):
    """
    Carga las estaciones desde el archivo de datos.

    Retorna un diccionario:
        codigo -> [nombre_estacion, municipio]
    """
    lineas = cargar_archivo(archivo)
    estaciones = {}

    for linea in lineas:
        if "," in linea and ";" not in linea and "[" not in linea and not linea.startswith(":"):
            datos = linea.split(",")

            if len(datos) == 3:
                codigo = datos[0]
                nombre = datos[1]
                municipio = datos[2]

                estaciones[codigo] = [nombre, municipio]

    return(estaciones)


def codigo_estacion(archivo):
    """
    Carga una relación auxiliar entre nombre de estación y código.

    Retorna un diccionario:
        nombre_estacion -> codigo
    """
    estaciones = cargar_estaciones(archivo)
    codigos = {}

    for codigo in estaciones:
        nombre = estaciones[codigo][0]
        codigos[nombre] = codigo

    return(codigos)


def cargar_variables(archivo):
    """
    Carga las variables monitoreadas desde el archivo de datos.

    Retorna un diccionario:
        variable -> [minimo, maximo, unidad]
    """
    lineas = cargar_archivo(archivo)
    variables = {}

    for linea in lineas:
        if "[" in linea and "]" in linea and ";" in linea:
            componentes = linea.split(";")

            for componente in componentes:
                if "[" in componente and "]" in componente:
                    nombre = componente[0:componente.find("[")]
                    contenido = componente[componente.find("[") + 1:componente.find("]")]

                    if "," in contenido and ":" in contenido:
                        rango, unidad = contenido.split(",", 1)
                        minimo, maximo = rango.split(":", 1)

                        try:
                            variables[nombre] = [float(minimo), float(maximo), unidad]
                        except ValueError:
                            pass

            break

    return(variables)


def lista_variables(archivo):
    """
    Retorna los nombres de las variables en el mismo orden en que
    aparecen en el archivo de datos.
    """
    lineas = cargar_archivo(archivo)
    variables = []

    for linea in lineas:
        if "[" in linea and "]" in linea and ";" in linea:
            componentes = linea.split(";")

            for componente in componentes:
                if "[" in componente:
                    nombre = componente[0:componente.find("[")]
                    variables.append(nombre)

            break

    return(variables)


def cargar_registros(archivo):
    """
    Carga los registros de medidas desde el archivo de datos.

    Retorna una lista donde cada registro tiene la forma:
        [codigo_estacion, fecha_hora, [valores]]
    """
    lineas = cargar_archivo(archivo)
    registros = []

    for linea in lineas:
        if "{" in linea and "}" in linea and ";" in linea:
            datos = linea.split(";")

            if len(datos) == 3:
                fecha_hora = datos[0]
                codigo = datos[1]
                contenido = datos[2]

                contenido = contenido.replace("{", "")
                contenido = contenido.replace("}", "")
                valores_txt = contenido.split(",")
                valores = []

                for valor in valores_txt:
                    try:
                        valores.append(float(valor))
                    except ValueError:
                        valores.append(-999.0)

                registros.append([codigo, fecha_hora, valores])

    return(registros)


def serializar_registro(registro):
    """
    Convierte un registro en el formato de línea usado por la base de datos.
    """
    codigo = registro[0]
    fecha_hora = registro[1]
    valores = registro[2]

    texto_valores = ""

    for i in range(len(valores)):
        texto_valores = texto_valores + str(valores[i])

        if i < len(valores) - 1:
            texto_valores = texto_valores + ","

    return(fecha_hora + ";" + codigo + ";{" + texto_valores + "}")


# -----------------------------------------------------------------
# USUARIOS Y AUTENTICACIÓN
# -----------------------------------------------------------------

def autenticar_usuario(archivo):
    """
    Solicita documento y contraseña.

    Si las credenciales son correctas retorna:
        [documento, nombre, rol]

    Si son incorrectas, retorna una lista vacía.
    """
    usuarios = cargar_usuarios(archivo)

    print("\n--- Inicio de sesión ---")
    documento = input("Documento: ").strip()
    contrasena = input("Contraseña: ")

    if documento in usuarios:
        datos = usuarios[documento]

        if datos[1] == contrasena:
            return([documento, datos[0], datos[2]])

    print("Documento o contraseña incorrectos.")
    return([])


def printusuarios(documentos, archivo):
    """
    Imprime los usuarios disponibles mostrando nombre y documento.
    """
    usuarios = cargar_usuarios(archivo)
    print("\nUsuarios registrados:")

    for documento in documentos:
        if documento in usuarios:
            print("-", usuarios[documento][0] + ":", documento)


def crear_usuario(archivo):
    """
    Crea un nuevo usuario en el sistema y lo inserta en la sección
    de usuarios del archivo de datos.
    """
    usuarios = cargar_usuarios(archivo)

    print("\n--- Crear usuario ---")

    while True:
        documento = input("Ingrese el documento del usuario: ").strip()

        if not validar_documento(documento):
            print("El documento debe tener exactamente 10 dígitos numéricos.")
        elif documento in usuarios:
            print("Ese documento ya está registrado.")
        else:
            break

    while True:
        nombre = input("Ingrese el nombre completo del usuario: ").strip()

        if validar_nombre(nombre):
            break
        else:
            print("El nombre solo puede contener letras y espacios.")

    while True:
        contrasena = input("Ingrese la contraseña: ")

        if not validar_contrasena(contrasena):
            print("La contraseña debe tener mínimo 4 caracteres.")
        else:
            confirmacion = input("Confirme la contraseña: ")

            if verificar_contrasena(contrasena, confirmacion):
                break
            else:
                print("Las contraseñas no coinciden.")

    while True:
        rol = input("Ingrese el rol (Administrador u Operador): ")
        rol = normalizar_rol(rol)

        if rol != "":
            break
        else:
            print("Ingrese un rol válido.")

    linea = "<" + documento + ";" + nombre + ";" + contrasena + ";" + rol + ">"

    insertar_usuario_en_archivo(archivo, linea)

    print("Usuario creado con éxito.")


def editar_usuario(archivo):
    """
    Edita nombre, contraseña y rol de un usuario existente.
    """
    usuarios = cargar_usuarios(archivo)
    documentos = []

    for documento in usuarios:
        documentos.append(documento)

    if len(documentos) == 0:
        print("No hay usuarios registrados.")
        return

    print("\n--- Editar usuario ---")
    printusuarios(documentos, archivo)

    while True:
        documento = input("Documento del usuario que desea editar: ").strip()

        if documento in usuarios:
            break
        else:
            print("Ingrese un documento que se encuentre en la base de datos.")

    datos_actuales = usuarios[documento]

    print("Nombre actual:", datos_actuales[0])
    while True:
        nombre = input("Nuevo nombre: ").strip()

        if validar_nombre(nombre):
            break
        else:
            print("El nombre solo puede contener letras y espacios.")

    print("Contraseña actual:", datos_actuales[1])
    while True:
        contrasena = input("Nueva contraseña: ")

        if not validar_contrasena(contrasena):
            print("La contraseña debe tener mínimo 4 caracteres.")
        else:
            confirmacion = input("Confirme la nueva contraseña: ")

            if verificar_contrasena(contrasena, confirmacion):
                break
            else:
                print("Las contraseñas no coinciden.")

    print("Rol actual:", datos_actuales[2])
    while True:
        rol = input("Nuevo rol (Administrador u Operador): ")
        rol = normalizar_rol(rol)

        if rol != "":
            break
        else:
            print("Ingrese un rol válido.")

    nueva_linea = "<" + documento + ";" + nombre + ";" + contrasena + ";" + rol + ">"
    lineas = cargar_archivo(archivo)
    nuevas_lineas = []

    for linea in lineas:
        if linea.startswith("<" + documento + ";"):
            nuevas_lineas.append(nueva_linea)
        else:
            nuevas_lineas.append(linea)

    escribir_archivo(archivo, nuevas_lineas)
    print("Usuario editado exitosamente.")


def eliminar_usuario(documento_actual, archivo):
    """
    Elimina un usuario registrado, excepto al usuario que tiene
    la sesión actual abierta.
    """
    usuarios = cargar_usuarios(archivo)
    documentos = []

    for documento in usuarios:
        documentos.append(documento)

    if len(documentos) == 0:
        print("No hay usuarios registrados.")
        return

    print("\n--- Eliminar usuario ---")
    printusuarios(documentos, archivo)

    while True:
        documento = input("Documento del usuario que desea eliminar: ").strip()

        if documento not in usuarios:
            print("Ingrese un documento que se encuentre en la base de datos.")
        elif documento == documento_actual:
            print("No se puede eliminar el usuario que tiene la sesión actual.")
        else:
            break

    while True:
        confirmacion = input("¿Seguro que desea eliminarlo? Ingrese 1 para sí o 0 para no: ").strip()

        if confirmacion == "1":
            lineas = cargar_archivo(archivo)
            nuevas_lineas = []

            for linea in lineas:
                if not linea.startswith("<" + documento + ";"):
                    nuevas_lineas.append(linea)

            escribir_archivo(archivo, nuevas_lineas)
            print("Usuario eliminado exitosamente.")
            return

        elif confirmacion == "0":
            print("Eliminación cancelada.")
            return

        else:
            print("Ingrese 1 o 0.")


# -----------------------------------------------------------------
# ESTACIONES
# -----------------------------------------------------------------

def crear_estacion(archivo):
    """
    Crea una estación nueva con código numérico incremental y la
    inserta antes de la línea de variables.
    """
    municipios = lista_municipios(archivo)
    estaciones = cargar_estaciones(archivo)

    if len(municipios) == 0:
        print("No hay municipios disponibles.")
        return

    print("\n--- Crear estación ---")
    print("Municipios disponibles:")
    imprimir_lista_numerada(municipios)

    while True:
        opcion = input("Seleccione el número del municipio: ").strip()

        if opcion.isdigit():
            posicion = int(opcion)

            if posicion >= 1 and posicion <= len(municipios):
                municipio = municipios[posicion - 1]
                break

        print("Seleccione un municipio válido.")

    while True:
        nombre = input("Ingrese el nombre de la estación: ").strip()

        if nombre_estacion_valido(nombre):
            break
        else:
            print("Ingrese un nombre no vacío y sin separadores como coma o punto y coma.")

    codigo_mayor = 0

    for codigo in estaciones:
        if codigo.isdigit() and int(codigo) > codigo_mayor:
            codigo_mayor = int(codigo)

    nuevo_codigo = str(codigo_mayor + 1)
    linea = nuevo_codigo + "," + nombre + "," + municipio

    insertar_estacion_en_archivo(archivo, linea)

    print("Estación creada con éxito. Código asignado:", nuevo_codigo)


def editar_estacion(archivo):
    """
    Edita el nombre y municipio de una estación existente.
    El código de la estación se conserva.
    """
    estaciones = cargar_estaciones(archivo)
    codigos = []

    for codigo in estaciones:
        codigos.append(codigo)

    if len(codigos) == 0:
        print("No hay estaciones registradas.")
        return

    print("\n--- Editar estación ---")
    tabla = []

    for codigo in estaciones:
        tabla.append([codigo, estaciones[codigo][0], estaciones[codigo][1]])

    imprimir_tabla(tabla, [8, 35, 20], ["Código", "Estación", "Municipio"])

    while True:
        codigo = input("Ingrese el código de la estación que desea editar: ").strip()

        if codigo in estaciones:
            break
        else:
            print("Ingrese un código existente.")

    datos_actuales = estaciones[codigo]
    municipios = lista_municipios(archivo)

    print("Nombre actual:", datos_actuales[0])
    while True:
        nombre = input("Nuevo nombre de la estación: ").strip()

        if nombre_estacion_valido(nombre):
            break
        else:
            print("Ingrese un nombre no vacío y sin separadores como coma o punto y coma.")

    print("Municipio actual:", datos_actuales[1])
    print("Municipios disponibles:")
    imprimir_lista_numerada(municipios)

    while True:
        opcion = input("Seleccione el número del nuevo municipio: ").strip()

        if opcion.isdigit():
            posicion = int(opcion)

            if posicion >= 1 and posicion <= len(municipios):
                municipio = municipios[posicion - 1]
                break

        print("Seleccione un municipio válido.")

    nueva_linea = codigo + "," + nombre + "," + municipio
    lineas = cargar_archivo(archivo)
    nuevas_lineas = []

    for linea in lineas:
        if linea.startswith(codigo + ",") and ";" not in linea:
            nuevas_lineas.append(nueva_linea)
        else:
            nuevas_lineas.append(linea)

    escribir_archivo(archivo, nuevas_lineas)
    print("Estación editada exitosamente.")


def estacion_tiene_registros(codigo, archivo):
    """
    Retorna True si existe al menos un registro asociado a la estación.
    """
    registros = cargar_registros(archivo)

    for registro in registros:
        if registro[0] == codigo:
            return(True)

    return(False)


def eliminar_estacion(archivo):
    """
    Elimina una estación siempre que no tenga registros asociados.
    """
    estaciones = cargar_estaciones(archivo)

    if len(estaciones) == 0:
        print("No hay estaciones registradas.")
        return

    print("\n--- Eliminar estación ---")
    tabla = []

    for codigo in estaciones:
        tabla.append([codigo, estaciones[codigo][0], estaciones[codigo][1]])

    imprimir_tabla(tabla, [8, 35, 20], ["Código", "Estación", "Municipio"])

    while True:
        codigo = input("Ingrese el código de la estación que desea eliminar: ").strip()

        if codigo not in estaciones:
            print("Ingrese un código existente.")
        elif estacion_tiene_registros(codigo, archivo):
            print("No se puede eliminar la estación porque tiene registros asociados.")
            return
        else:
            break

    while True:
        confirmacion = input("¿Seguro que desea eliminarla? Ingrese 1 para sí o 0 para no: ").strip()

        if confirmacion == "1":
            lineas = cargar_archivo(archivo)
            nuevas_lineas = []

            for linea in lineas:
                if not (linea.startswith(codigo + ",") and ";" not in linea):
                    nuevas_lineas.append(linea)

            escribir_archivo(archivo, nuevas_lineas)
            print("Estación eliminada exitosamente.")
            return

        elif confirmacion == "0":
            print("Eliminación cancelada.")
            return

        else:
            print("Ingrese 1 o 0.")


def estaciones_por_municipio(archivo, municipio):
    """
    Retorna una lista de estaciones pertenecientes al municipio recibido.
    Cada elemento tiene la forma [codigo, nombre].
    """
    estaciones = cargar_estaciones(archivo)
    resultado = []

    for codigo in estaciones:
        if estaciones[codigo][1] == municipio:
            resultado.append([codigo, estaciones[codigo][0]])

    return(resultado)


# -----------------------------------------------------------------
# REGISTROS DE MEDIDAS
# -----------------------------------------------------------------

def validar_valor_medida(valor, rango):
    """
    Valida un valor de medida frente a un rango [mínimo, máximo].

    Acepta:
        - 'ND' como valor no disponible.
        - Números dentro del rango inclusivo.

    Retorna:
        [True, valor_convertido] o [False, None]
    """
    texto = str(valor).strip()

    if texto.upper() == "ND":
        return([True, -999.0])

    try:
        numero = float(texto)
    except ValueError:
        return([False, None])

    minimo = rango[0]
    maximo = rango[1]

    if numero >= minimo and numero <= maximo:
        return([True, numero])
    else:
        return([False, None])


def procesar_registro(variables):
    """
    Solicita los valores de cada variable, valida el rango y convierte
    la entrada 'ND' en -999.0.

    Retorna una lista con los valores ya procesados.
    """
    valores = []

    for variable in variables:
        minimo = variables[variable][0]
        maximo = variables[variable][1]
        unidad = variables[variable][2]

        while True:
            texto = input(
                "Ingrese " + variable +
                " (" + str(minimo) + " a " + str(maximo) + " " + unidad +
                ", o ND si no hay dato): "
            )

            validacion = validar_valor_medida(texto, [minimo, maximo])

            if validacion[0]:
                valores.append(validacion[1])
                break
            else:
                print("Valor inválido. Ingrese un número dentro del rango o ND.")

    return(valores)


def crear_registro(archivo, codigo):
    """
    Crea un registro de medición para la estación indicada, usando
    la fecha y hora actual del sistema.
    """
    variables = cargar_variables(archivo)

    if len(variables) == 0:
        print("No hay variables configuradas.")
        return

    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    valores = procesar_registro(variables)

    registro = [codigo, fecha_hora, valores]
    linea = serializar_registro(registro)
    agregar_linea(archivo, linea)

    print("Registro guardado exitosamente.")


def mostrar_medidas_estacion(archivo, codigo):
    """
    Muestra en una tabla las medidas registradas para una estación.
    """
    registros = cargar_registros(archivo)
    nombres_variables = lista_variables(archivo)
    tabla = []

    for registro in registros:
        if registro[0] == codigo:
            fila = [registro[1]]

            for valor in registro[2]:
                if valor == -999.0:
                    fila.append("ND")
                else:
                    fila.append(valor)

            tabla.append(fila)

    if len(tabla) == 0:
        print("La estación seleccionada no tiene registros.")
        return

    encabezado = ["Fecha y hora"]

    for nombre in nombres_variables:
        encabezado.append(nombre)

    anchos = [20]

    for nombre in nombres_variables:
        if len(nombre) < 12:
            anchos.append(12)
        else:
            anchos.append(len(nombre) + 2)

    imprimir_tabla(tabla, anchos, encabezado)


# -----------------------------------------------------------------
# DEPURACIÓN DE REGISTROS
# -----------------------------------------------------------------

def registro_esta_en_lista(registro_texto, lista_textos):
    """
    Retorna True si el texto del registro ya está en la lista recibida.
    """
    for texto in lista_textos:
        if texto == registro_texto:
            return(True)

    return(False)


def generar_reportes(registros_originales, registros_v2):
    """
    Genera dos reportes:
        1. Registros comunes en ambos archivos.
        2. Registros que aparecen en cualquiera de los dos archivos,
           sin repetirlos.

    Retorna:
        [comunes, union]
    """
    comunes_texto = []
    union_texto = []

    for registro in registros_originales:
        texto = serializar_registro(registro)

        if not registro_esta_en_lista(texto, union_texto):
            union_texto.append(texto)

    for registro in registros_v2:
        texto = serializar_registro(registro)

        if not registro_esta_en_lista(texto, union_texto):
            union_texto.append(texto)

    for registro_original in registros_originales:
        texto_original = serializar_registro(registro_original)

        for registro_v2 in registros_v2:
            texto_v2 = serializar_registro(registro_v2)

            if texto_original == texto_v2:
                if not registro_esta_en_lista(texto_original, comunes_texto):
                    comunes_texto.append(texto_original)
                break

    return([comunes_texto, union_texto])


def mostrar_reporte_registros(textos, titulo):
    """
    Imprime un reporte de registros en formato de tabla.
    """
    print("\n" + titulo)

    if len(textos) == 0:
        print("No hay registros para mostrar.")
        return

    tabla = []

    for texto in textos:
        datos = texto.split(";")
        fecha_hora = datos[0]
        codigo = datos[1]
        valores = datos[2]

        tabla.append([fecha_hora, codigo, valores])

    imprimir_tabla(tabla, [20, 10, 50], ["Fecha y hora", "Estación", "Valores"])


def depurar_registros(archivo_original, archivo_v2):
    """
    Lee dos archivos de registros y muestra:
        - Registros comunes.
        - Registros presentes en cualquiera de los dos archivos.
    """
    if not archivo_existe(archivo_v2):
        print("No se encontró el archivo duplicado:", archivo_v2)
        print("Para usar esta opción, cree ese archivo con el mismo formato de la base original.")
        return

    registros_originales = cargar_registros(archivo_original)
    registros_v2 = cargar_registros(archivo_v2)

    reportes = generar_reportes(registros_originales, registros_v2)

    mostrar_reporte_registros(
        reportes[0],
        "Registros comunes en ambas versiones:"
    )

    mostrar_reporte_registros(
        reportes[1],
        "Registros presentes en cualquiera de las dos versiones:"
    )


# -----------------------------------------------------------------
# ESTADÍSTICAS PARA VISITANTES
# -----------------------------------------------------------------

def seleccionar_periodo():
    """
    Permite elegir el periodo de análisis para las estadísticas.

    Retorna:
        [fecha_inicio, fecha_fin]
    """
    while True:
        print("\nPeriodo de análisis:")
        print("1) Últimos 7 días.")
        print("2) Últimos 30 días.")
        print("3) Elegir fechas manualmente.")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            hoy = datetime.now()
            inicio = hoy - timedelta(days=6)

            return([
                inicio.strftime("%Y-%m-%d"),
                hoy.strftime("%Y-%m-%d")
            ])

        elif opcion == "2":
            hoy = datetime.now()
            inicio = hoy - timedelta(days=29)

            return([
                inicio.strftime("%Y-%m-%d"),
                hoy.strftime("%Y-%m-%d")
            ])

        elif opcion == "3":
            while True:
                inicio = input("Fecha inicial (yyyy-mm-dd): ").strip()

                if validar_fecha(inicio):
                    break
                else:
                    print("Ingrese una fecha inicial válida.")

            while True:
                fin = input("Fecha final (yyyy-mm-dd): ").strip()

                if not validar_fecha(fin):
                    print("Ingrese una fecha final válida.")
                elif fin < inicio:
                    print("La fecha final no puede ser anterior a la fecha inicial.")
                else:
                    break

            return([inicio, fin])

        else:
            print("Ingrese una opción válida.")


def seleccionar_varias_opciones(lista, nombre_grupo):
    """
    Permite seleccionar uno, varios o todos los elementos de una lista.

    El usuario puede escribir:
        - T para todos.
        - Números separados por coma, por ejemplo: 1,3,4.

    Retorna una lista con los elementos seleccionados.
    """
    print("\nSeleccione", nombre_grupo + ":")
    imprimir_lista_numerada(lista)
    print("T) Todos")

    while True:
        seleccion = input("Ingrese su selección: ").strip()

        if seleccion.upper() == "T":
            resultado = []

            for elemento in lista:
                resultado.append(elemento)

            return(resultado)

        partes = seleccion.split(",")
        resultado = []
        valido = True

        for parte in partes:
            parte = parte.strip()

            if not parte.isdigit():
                valido = False
                break

            posicion = int(parte)

            if posicion < 1 or posicion > len(lista):
                valido = False
                break

            elemento = lista[posicion - 1]

            if elemento not in resultado:
                resultado.append(elemento)

        if valido and len(resultado) > 0:
            return(resultado)
        else:
            print("Ingrese T o números válidos separados por coma.")


def fecha_registro_en_periodo(fecha_hora, inicio, fin):
    """
    Verifica si la fecha de un registro está dentro del rango recibido.
    """
    fecha = fecha_hora[0:10]

    if fecha >= inicio and fecha <= fin:
        return(True)
    else:
        return(False)


def obtener_estadisticas(archivo, inicio, fin, variables_seleccionadas, municipios_seleccionados):
    """
    Calcula máximo, mínimo y promedio para cada variable seleccionada,
    considerando únicamente los municipios y el periodo elegidos.

    Retorna una lista con filas listas para mostrarse o escribirse.
    """
    variables = lista_variables(archivo)
    estaciones = cargar_estaciones(archivo)
    registros = cargar_registros(archivo)
    resultados = []

    for variable in variables_seleccionadas:
        indice_variable = -1

        for i in range(len(variables)):
            if variables[i] == variable:
                indice_variable = i
                break

        if indice_variable == -1:
            continue

        cantidad = 0
        suma = 0.0
        minimo = None
        maximo = None
        estacion_min = ""
        estacion_max = ""
        fecha_min = ""
        fecha_max = ""

        for registro in registros:
            codigo = registro[0]
            fecha_hora = registro[1]
            valores = registro[2]

            if codigo not in estaciones:
                continue

            municipio = estaciones[codigo][1]

            if municipio not in municipios_seleccionados:
                continue

            if not fecha_registro_en_periodo(fecha_hora, inicio, fin):
                continue

            if indice_variable >= len(valores):
                continue

            valor = valores[indice_variable]

            if valor == -999.0:
                continue

            cantidad = cantidad + 1
            suma = suma + valor

            if minimo is None or valor < minimo:
                minimo = valor
                estacion_min = estaciones[codigo][0]
                fecha_min = fecha_hora

            if maximo is None or valor > maximo:
                maximo = valor
                estacion_max = estaciones[codigo][0]
                fecha_max = fecha_hora

        if cantidad == 0:
            resultados.append([
                variable,
                "Sin datos",
                "Sin datos",
                "Sin datos",
                "Sin datos",
                "Sin datos"
            ])
        else:
            promedio = suma / cantidad

            resultados.append([
                variable,
                round(minimo, 2),
                estacion_min + " | " + fecha_min,
                round(maximo, 2),
                estacion_max + " | " + fecha_max,
                round(promedio, 2)
            ])

    return(resultados)


def construir_texto_estadisticas(resultados, inicio, fin, variables, municipios):
    """
    Construye un texto plano con el resumen de estadísticas.
    """
    texto = ""
    texto = texto + "ESTADÍSTICAS DE MEDIDAS AMBIENTALES\n"
    texto = texto + "Periodo: " + inicio + " a " + fin + "\n"
    texto = texto + "Variables: "

    for i in range(len(variables)):
        texto = texto + variables[i]

        if i < len(variables) - 1:
            texto = texto + ", "

    texto = texto + "\nMunicipios: "

    for i in range(len(municipios)):
        texto = texto + municipios[i]

        if i < len(municipios) - 1:
            texto = texto + ", "

    texto = texto + "\n\n"

    for fila in resultados:
        texto = texto + "Variable: " + str(fila[0]) + "\n"
        texto = texto + "Mínimo: " + str(fila[1]) + "\n"
        texto = texto + "Estación y fecha del mínimo: " + str(fila[2]) + "\n"
        texto = texto + "Máximo: " + str(fila[3]) + "\n"
        texto = texto + "Estación y fecha del máximo: " + str(fila[4]) + "\n"
        texto = texto + "Promedio: " + str(fila[5]) + "\n"
        texto = texto + "-" * 60 + "\n"

    return(texto)


def mostrar_estadisticas(archivo):
    """
    Ejecuta el flujo completo de estadísticas para usuarios visitantes:
    periodo, variables, municipios y modo de salida.
    """
    variables = lista_variables(archivo)
    municipios = lista_municipios(archivo)

    if len(variables) == 0 or len(municipios) == 0:
        print("No hay variables o municipios disponibles para realizar el análisis.")
        return

    periodo = seleccionar_periodo()
    inicio = periodo[0]
    fin = periodo[1]

    variables_seleccionadas = seleccionar_varias_opciones(variables, "las variables")
    municipios_seleccionados = seleccionar_varias_opciones(municipios, "los municipios")

    resultados = obtener_estadisticas(
        archivo,
        inicio,
        fin,
        variables_seleccionadas,
        municipios_seleccionados
    )

    while True:
        print("\nModo de visualización:")
        print("1) Mostrar por pantalla.")
        print("2) Guardar en Estadisticas.txt.")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("\nESTADÍSTICAS DE MEDIDAS AMBIENTALES")
            print("Periodo:", inicio, "a", fin)
            imprimir_tabla(
                resultados,
                [16, 12, 42, 12, 42, 12],
                ["Variable", "Mínimo", "Estación y fecha mínimo", "Máximo", "Estación y fecha máximo", "Promedio"]
            )
            return

        elif opcion == "2":
            texto = construir_texto_estadisticas(
                resultados,
                inicio,
                fin,
                variables_seleccionadas,
                municipios_seleccionados
            )

            archivo_salida = open("Estadisticas.txt", "w", encoding="utf-8")
            archivo_salida.write(texto)
            archivo_salida.close()

            print("Estadísticas guardadas en Estadisticas.txt.")
            return

        else:
            print("Ingrese una opción válida.")