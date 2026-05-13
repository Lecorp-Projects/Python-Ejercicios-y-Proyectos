#Hugo Esteban Barrero Garcia
#Jose Gabriel Giraldo 
#Grupo 4
def cargar_archivo(archivo):
    texto = []
    abrir = open(archivo, "r")
    txt = abrir.read()
    dato = ""
    abrir.close()
    for char in txt: 
        if char == "\n":
            texto.append(dato)
            dato = ""
        else:
            dato = dato + char 
    return(texto)
def cargar_registros(archivo):
    texto = cargar_archivo(archivo)
    registros = {}
    datos = ""
    for element in texto:
        if "{" in element:
            for character in element:
                    datos = datos + character 
            datos = datos.split(";") 
            fecha = datos[0]
            codigo = datos[1]
            var = datos[2]
            datos2 = ""
            for character in var: 
                if character == "{":
                    continue 
                elif character == "}":
                    break
                datos2 = datos2 + character       
            var = datos2.split(",")
            registros[codigo,fecha] = [codigo,fecha,var]
            datos = ""
    return(registros)

def cargar_estaciones(archivo):
    """
    Carga la información de las estaciones desde el archivo de texto a la memoria del programa.
    Retorna un diccionario donde las claves son los códigos de estación y los valores son el nombre de la estación y el municipio.
    """
    texto = cargar_archivo(archivo)
    municipios = {}
    datos = ""
    for element in texto:
        if ':' not in element and "," in element:
            for character in element:
                    datos = datos + character 
            datos = datos.split(",") 
            codigo = datos[0]
            estacion = datos[1]
            municipio = datos[2]
            municipios[codigo] = [estacion, municipio]
            datos = ""
    return(municipios)
def codigo_estacion(archivo):
    """
    Carga la información de las estaciones desde el archivo de texto a la memoria del programa.
    Retorna un diccionario donde las claves son los códigos de estación y los valores son el nombre de la estación y el municipio.
    """
    texto = cargar_archivo(archivo)
    estaciones = {}
    datos = ""
    for element in texto:
        if ':' not in element and "," in element:
            for character in element:
                    datos = datos + character 
            datos = datos.split(",") 
            codigo = datos[0]
            estacion = datos[1]
            estaciones[estacion] = codigo
            datos = ""
    return(estaciones)

def eliminar_estacion(nombre,archivo):
    """
    Elimina una estación del sistema si no tiene registros asociados de la base de datos.
    """
    estaciones = codigo_estacion(archivo)
    codigo = estaciones[nombre]
    registros = cargar_registros(archivo)
    claves = list(registros.keys())
    registro = []
    for i in range(0,len(claves)):
        registro.append(registros[claves[i]][0])   
    verificar = False 
    for char in registro:
        h = char
        if str(h) == codigo:
            verificar = True
            break
        else:
            verificar = False 
    if verificar == True:      
       print("No la podemos eliminar")   
    else:
         x = cargar_archivo(archivo)
         texto = []
         i = 0
         while i < len(x):
            if nombre in x[i]:
                i = i + 1
            else:
                texto.append(x[i])
                i = i + 1
         nuevoregistro =""
         for element in texto:
            for character in element: 
                nuevoregistro =  nuevoregistro + character
            nuevoregistro =  nuevoregistro + "\n"
         x = open(archivo,"w")
         x.write(nuevoregistro)
         x.close()
archivo = "registros_.txt"
nombre = input("Estacion")
'''str(input("Ingrese estacion"))
'''
eliminar_estacion(nombre,archivo)
def validar_valor_medida(valor, rango):
    """
    Valida que un valor de medida esté dentro del rango especificado.
    Recibe el valor y un rango en formato (mínimo, máximo).
    Retorna True si el valor está dentro del rango, False si no lo esta.
    """
    ran = rango.split(",")
    if (valor > ran[0]) and (valor < ran[1]):
        return (True)
    else:
        return(False)