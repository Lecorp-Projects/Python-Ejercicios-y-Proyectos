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
'''print(cargar_archivo("registros_.txt"))'''
def cargar_usuarios(archivo):
    """
    Carga la información de usuarios desde el archivo de texto a la memoria del programa.
    Retorna un diccionario donde las claves son los documentos y los valores son listas con el nombre completo, contraseña y rol del usuario.
    """
    texto = cargar_archivo(archivo)
    usuarios = {}
    datos = ""
    for element in texto:
        if '<' in element:
            for character in element:
                if character == '<':
                    continue
                elif character == '>':
                     datos = datos.split(";") 
                     documento = datos[0]
                     nombre = datos[1]
                     contraseña = datos[2]
                     rol = datos[3]
                     usuarios[documento] = [nombre, contraseña, rol]
                     datos = ""
                     continue
                else: 
                    datos = datos + character 
    return(usuarios)
print(cargar_usuarios('registros_.txt'))
def lista_municipios(archivo):
    texto = cargar_archivo(archivo)
    municipios = ""
    for element in texto:
       if ':' in element:
          for character in element:
              if character == ':':
                  continue
              municipios = municipios + character   
          municipios = municipios.split(",") 
          break
                  
    return(municipios)
def cargar_estaciones(archivo):
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
print(cargar_estaciones('registros_.txt'))
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
            registros[fecha] = [codigo,fecha,var]
            datos = ""
    return(registros)
def cargar_variables(archivo):
    texto = cargar_archivo(archivo)
    variables = {}
    datos = ""
    for element in texto:
        if "[" in element:
            for character in element:
                    datos = datos + character 
            datos = datos.split(";") 
            for element in datos: 
                datos2 = ""
                for character in element: 
                    if not character == "]":
                        datos2 = datos2 + character
                datos2 = datos2.split("[")
                datos2[1] = datos2[1].split(",")
                nombre = datos2[0]
                rango = datos2[1][0]
                unidad = datos2[1][1]
                variables[nombre] = [rango,unidad]                 
    return(variables)
def crear_usuario(archivo):
    x = open(archivo, "a")
    documento = input("Ingrese el documento del usuario:")
    nombre = input("Ingrese el nombre del usuario:")
    clave = input("Ingrese la clave del usuario: ")
    rol = input("Ingrese el rol del usuario: ")
    string = "<" + documento +";" + nombre +";" + clave + ";"+ rol + ">"
    x.write(string + "\n")
    x.close()

def crear_estacion(archivo):
    x = open(archivo, "a")
    estacion = input("Ingrese el nombre de la estacion:")
    municipio = input("Ingrese el nombre del municipio:")
    cantidad = cargar_estaciones(archivo)
    codigo = len(cantidad) + 1 
    string = str(codigo) + "," + estacion + "," + municipio
    x.write(string + "\n")
    x.close()
    
def crear_registro(archivo,codigo):
    from datetime import datetime 
    x = open(archivo, "a")
    hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cantidadvar = len(cargar_variables(archivo))
    variables = ""
    for i in range(0,cantidadvar):
        x2 = input("Ingrese el dato de la variable: ")
        variables = variables + x2 + ","
    variables = variables[0:-1]
    string = str(hora) + ";" + str(codigo) + ";" + "{" + variables + "}" 
    x.write(string + "\n")
    x.close()
def validar_nombre(nombre):
    '''
    Valida nombre válido (solo letras y espacios)
    El nombre es el string a validar
    return -> Boolean (True or False) si es valido o no
    '''
    nombre = nombre.lower()
    abcdario = "abcdefghijklmnñopqrstuvwxyz"
    for character in nombre: 
       if character in abcdario or character == " ":
           return(True)
       else:
           return(False)
def validar_contraseña(contraseña):
    """
    Valida que una contraseña tenga mínimo 4 caracteres.
    Retorna True si la contraseña es válida, False de lo contrario.
    """
    if len(contraseña) >= 4:
        return(True)
    else:
        return(False)
def verificar_contraseña(contraseña, confirmacion):
    if contraseña == confirmacion: 
        return(True)
    else:
        return(False)

def validar_valor_medida(valor, rango):
    """
    Valida que un valor de medida esté dentro del rango especificado.
    Recibe el valor y un rango en formato (mínimo, máximo).
    Retorna True si el valor está dentro del rango, False si no lo esta.
    """
    
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
x = "registros_.txt"
print(cargar_archivo(x))
"""
print(crear_estacion(x))
print(crear_registro(x,input("ALLGOaivfiaug")))
print(validar_nombre(input("Nombre")))
print(validar_documento(input("Documento")))
print(validar_contraseña(input("Contrasena")))"""
print(verificar_contraseña(input("Contrasena"),input("Contra")))

"""def editar_usuario(documento):
    
    Edita los detalles de un usuario existente en el sistema.
    Recibe el documento del usuario a editar, el nuevo nombre, contraseña y rol.
    Hay que actualizar la información del usuario en la base de datos.

    x = cargar_archivo(archivo)
    texto = []
    i = 0
    while i < len(x):
        if str(documento) not in x[i]:
            texto.append(x[i])
            i = i + 1
        else:
            i = i + 1
    nuevoregistro =""
    for element in texto:
        for character in element: 
            nuevoregistro =  nuevoregistro + character
        nuevoregistro =  nuevoregistro + "\n"
    x = open(archivo,"w")
    x.write(nuevoregistro)
    x.close()
    """
def validar_documento(documento):
    '''
    Valida un número de documento. Debe tener 10 caracteres numericos.   
    el documento es el string a validar
    return -> Boolean (True or False) si es valido o no
    '''
    numeros = "0123456789"
    documento = str(documento)
    if len(documento) == 10:
        for character in documento: 
            if character in numeros: 
                return(True)
            else:
                return(False)
    else:
        return(False)
def eliminar_usuario(documento,documento2,archivo):
    """
    Elimina un usuario del sistema, pero no se puede el usuario actual.
    Recibe el documento del usuario a eliminar (el unico input), tambien el documento del usuario actual (documento2) y el nombre del archivo. 
    Elimina el usuario de la base de datos.
    """
    x = cargar_archivo(archivo)
    texto = []
    if validar_documento(documento) != False or validar_documento(documento2) != False: 
        if documento in x :
            if documento != documento2:
                for line in x:
                    if str(documento) not in line:
                        texto.append(line)
                nuevoregistro =""
                for element in texto:
                    for character in element: 
                        nuevoregistro =  nuevoregistro + character
                    nuevoregistro =  nuevoregistro + "\n"
                x = open(archivo,"w")
                x.write(nuevoregistro)
                x.close()
            else:
                print("No se puede eliminar el usuario actual")
        else:
            print("El documento ingresado no se haya en la base de datos")
    else:
         print("El documento ingresado no es valido. (Asegurese que tenga 10 digitos y solo haya escrito numeros).")
       
       
eliminar_usuario(input(),input(),x)
        
    