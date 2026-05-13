#Hugo Esteban Barrero Garcia
#Jose Gabriel Giraldo 
#Grupo 4
def verificar_rol(rol):
    rol = rol.lower().capitalize()
    roles = ["Operador","Administrador"]
    if rol in roles:
        return(True)
    else:
        return(False)
    
def cargar_archivo(archivo):
    """
    Esta funcion es pa abrir un archivo, leerlo y poner los datos como tipos de datos establecidos.
    """
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

def validar_nombre(nombre):
    '''
    Valida nombre válido (solo letras y espacios)
    El nombre es el string a validar
    return -> Boolean (True or False) si es valido o no
    '''
    nombre = nombre.lower()
    abcdario = "abcdefghijklmnñopqrstuvwxyzáéíóúüñ"
    for character in nombre: 
       if character in abcdario or character == " ":
           return(True)
       else:
           return(False)
       
def validar_documento(documento):
    '''
    Valida un número de documento. Debe tener 10 caracteres numericos.   
    el documento es el string a validar
    return -> Boolean (True or False) si es valido o no
    '''
    numeros = ["0","1","2","3","4","5","6","7","8","9"]
    documento = str(documento)
    if len(documento) == 10:
        for character in str(documento): 
            if character in numeros: 
                continue
            else:
                return(False)
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
    """
    Verifica si dos contraseñas son iguales.
    Recibe una contraseña y su confirmación.
    Retorna True si las contraseñas coinciden, False, si no coinciden.
    """
    if contraseña == confirmacion: 
        return(True)
    else:
        return(False)
    
def printusuarios(lista,archivo):
    """
    Imprime en pantalla los usuarios disponibles en la lista, junto con sus documentos.
    """
    Documentos = cargar_usuarios(archivo)
    print("Elija entre los siguientes usuarios.(Nombre: Documento).")
    for elemento in lista:
        print("-",Documentos[elemento][0],": ",elemento, sep="")
        
def crear_usuario(archivo):
    """
    Crea un nuevo usuario en el sistema.
    Recibe el documento, nombre completo, contraseña y rol del nuevo usuario.
    Guarda la información del nuevo usuario en la base de datos.
    """
    x = open(archivo, "a")
    while True:
        documento = input("Ingrese el documento del usuario: ")
        
        if validar_documento(documento) == True:
            break
        else:
            print("El documento ingresado es invalido, ingreselo de nuevo.")  
    while True:
        nombre = input("Ingrese el nombre del usuario: ")
        
        if validar_nombre(nombre) == True:
            break
        else:
            print("El nombre ingresado es invalido, ingreselo de nuevo.")  
    while True:
        rol = input("Ingrese el rol del usuario (elija entre Operador o Administrador): ")
        
        if verificar_rol(rol) == True:
            break
        else:
            print("Ingreso un rol invalido.")  
    while True:
        contraseña = input("Ingrese la contraseña del usuario: ")
        
        if validar_contraseña(contraseña) == True:
            verificacion = input("Ingrese otra vez la contraseña: ")
            if verificar_contraseña(contraseña, verificacion) == True :
                break
            else:
                print("Las contraseñas no coinciden.")
        else:
            print("La contraseña ingresada no es valida, ingreselo de nuevo. (Minimo debe tener 4 caracteres).")  
    string = "<" + documento +";" + nombre +";" + contraseña + ";"+ rol + ">"
    x.write(string + "\n")
    print("Usuario creado con exito.")
    x.close()
    
def editar_usuario(archivo):
    """
    Edita los detalles de un usuario existente en el sistema.
    Recibe el documento del usuario a editar y el nombre del archivo que contiene la información de los usuarios.
    Actualiza la información del usuario en la base de datos.
    """
    Documentos = cargar_usuarios(archivo).keys()
    usuarios = cargar_usuarios(archivo)
    printusuarios(Documentos,archivo)
    while True:
        documento = input("Ingrese el documento del usuario que desea editar: ")
        
        if validar_documento(documento) == True:
            if documento in Documentos:
                break
            else:
                print("El documento ingresado no se encuentra en la base de datos, ingrese el documento nuevamente.")
            
        else:
            print("El documento ingresado es invalido, ingreselo de nuevo (asegurese que tenga 10 digitos y solo haya escrito numeros).")  
    x = cargar_archivo(archivo)
    texto = []
    info = usuarios[documento]
    for line in x:
        if documento not in line:
            texto.append(line)
        else:
            while True:
                print("El nombre actual es: ",info[0])
                nombre = input("Ingrese el nuevo nombre del usuario: ")
                
                if validar_nombre(nombre) == True:
                    break
                else:
                    print("El nombre ingresado es invalido, ingreselo de nuevo.")  
            while True:
                print("El rol actual es: ",info[2])
                rol = input("Ingrese el nuevo rol del usuario (elija entre Operador o Administrador): ")
                
                if verificar_rol(rol) == True:
                    break
                else:
                    print("Ingreso un rol invalido.")  
            while True:
                print("La contraseña actual es: ",info[1])
                contraseña = input("Ingrese la nueva contraseña del usuario: ")
                
                if validar_contraseña(contraseña) == True:
                    verificacion = input("Ingrese otra vez la contraseña: ")
                    if verificar_contraseña(contraseña, verificacion) == True :
                        break
                    else:
                        print("Las contraseñas no coinciden.")
                else:
                    print("La contraseña ingresada no es valida, ingreselo de nuevo. (Minimo debe tener 4 caracteres).")  
            string = "<" + documento +";" + nombre +";" + contraseña + ";"+ rol + ">"
            texto.append(string)
    nuevoregistro = ""
    for element in texto:
        for character in element: 
            nuevoregistro =  nuevoregistro + character
        nuevoregistro =  nuevoregistro + "\n"
    x = open(archivo,"w")
    x.write(nuevoregistro)
    x.close()
    print("Usuario editado exitosamente.")

def eliminar_usuario(documento2,archivo):
    """
    Elimina un usuario del sistema, pero no se puede el usuario actual.
    El documento del usuario actual (documento2) y el nombre del archivo. 
    Elimina el usuario de la base de datos.
    """
    Documentos = cargar_usuarios(archivo).keys()
    printusuarios(Documentos,archivo)
    while True:
        documento = input("Ingrese el documento del usuario que desea Eliminar: ")
        if validar_documento(documento) == True:
            
            if documento != documento2:
                if documento in Documentos:
                    while True:
                        print("Seguro que desea eliminar el usuario identificado con el documento:",documento)
                        y = input(" Ingrese 1 si esta de acuerdo, y si no, ingrese 0: ")
                        if y == "1":
                            break
                        elif y == "0":
                            break
                        else:
                            print("Ingrese 0, para negarse y elegir otro usuario y 1 si esta de acuerdo.")
    
                    break
                else:
                    print("El documento ingresado no se encuentra en la base de datos, ingrese el documento nuevamente.")
            else:
                print("No se puede eliminar el usuario actual")
            
            
        else:
            print("El documento ingresado es invalido, ingreselo de nuevo (asegurese que tenga 10 digitos y solo haya escrito numeros).") 
    
    x = cargar_archivo(archivo)
    texto = []
    Documentos = cargar_usuarios(archivo).keys()
    for line in x:
        if documento not in line:
            texto.append(line)
    nuevoregistro = ""
    for element in texto:
        for character in element: 
            nuevoregistro =  nuevoregistro + character
        nuevoregistro =  nuevoregistro + "\n"
    x = open(archivo,"w")
    x.write(nuevoregistro)
    x.close()
    print("Usuario eliminado exitosamente.")
     
def lista_municipios(archivo):
    """
    Extrae la lista de municipios de un archivo de texto y la devuelve como una lista de strings.
    """
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
    Retorna un diccionario donde las claves son los nombres de estación y los valores son el codigo de la estación.
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

def crear_estacion(archivo):
    """
    Crea una nueva estación de monitoreo en el sistema.
    Recibe el nombre de la estación y el municipio donde está ubicada.
    Genera automáticamente un nuevo código de estación incremental y lo asigna.
    Guarda la información de la nueva estación en la base de datos.
    """
    def printlist(lista):
        for elemento in lista:
            print("-",elemento, sep="")
    x = open(archivo, "a")
    municipios = lista_municipios(archivo)
    print("Este es el listado de municipios: ")
    printlist(municipios)
    while True:
        municipio = input("Ingrese el nombre del municipio: ")
        if municipio in municipios :
            break
        else: 
            print("El municipio ingresado no se encuentra en la lista de municipios.")
    estacion = input("Ingrese el nombre de la estacion:")
    codigoestacion = codigo_estacion(archivo).values()
    highercode = 0
    for a in codigoestacion:
        if int(a) > highercode:
            highercode = int(a) 
    codigo = highercode + 1 
    string = str(codigo) + "," + estacion + "," + municipio
    x.write(string + "\n")
    x.close()
    print("Estacion creada con exito.")

def editar_estacion(archivo):
    
    """
    Edita los detalles de una estación existente en el sistema.
    Recibe el nombre de la estación a editar, el nuevo nombre y municipio.
    Actualiza la información de la estación en la base de datos.
    """
    def printlist(lista):
        x = 1
        for elemento in lista:
            print(x,") ",elemento, sep="")
            x = x + 1 
    nombreestaciones = codigo_estacion(archivo).keys()
    print("Observe la lista de estaciones:")
    printlist(nombreestaciones)
    municipios = lista_municipios(archivo)
    ciclo = 0 
    while ciclo == 0:
        nombre = input("Ingrese la estacion que desea editar: ")
        if nombre in nombreestaciones:
            estaciones = codigo_estacion(archivo)
            codigo = estaciones[nombre]
            registros = cargar_registros(archivo)
            claves = list(registros.keys())
            registro = []
            for i in range(0,len(claves)):
                registro.append(registros[claves[i]][0])   
            verificar = bool 
            for code in registro:
                if str(code) == codigo:
                    verificar = True
                    break
                else:
                    verificar = False 
            if verificar == True:      
               print("No se puede eliminar esta estacion porque tiene valores asociados.")  
            else:
                 x = cargar_archivo(archivo)
                 texto = []
                 for linea in x:
                    if nombre in linea:
                        print("Este es el listado de municipios: ")
                        printlist(municipios)
                        while True:
                            municipio = input("Ingrese el municipio al que quiere que pertenezca la estacion: ")
                            if municipio in municipios :
                                break
                            else: 
                                print("El municipio ingresado no se encuentra en la lista de municipios.")
                        estacion = input("Ingrese el nuevo nombre de la estacion:")
                        string = str(codigo) + "," + estacion + "," + municipio
                        texto.append(string)
                    else:
                        texto.append(linea)
                 nuevoregistro = ""
                 for element in texto:
                    for character in element: 
                        nuevoregistro =  nuevoregistro + character
                    nuevoregistro =  nuevoregistro + "\n"
                 x = open(archivo,"w")
                 x.write(nuevoregistro)
                 x.close()
                 print("Estacion editada exitosamente.")
                 ciclo = 1
        else:
            print("Ingrese una estacion que este en la lista y hagalo correctamente.")
def eliminar_estacion(archivo):
    """
    Elimina una estación del sistema si no tiene registros asociados de la base de datos.
    """
    def printlist(lista):
        x = 1
        for elemento in lista:
            print(x,") ",elemento, sep="")
            x = x + 1 
    nombreestaciones = codigo_estacion(archivo).keys()
    print("Mire la lista de estaciones:")
    printlist(nombreestaciones)
    ciclo = 0 
    while ciclo == 0:
        nombre = input("Ingrese la estacion que desea eliminar: ")
        if nombre in nombreestaciones:
            estaciones = codigo_estacion(archivo)
            codigo = estaciones[nombre]
            registros = cargar_registros(archivo)
            claves = list(registros.keys())
            registro = []
            for i in range(0,len(claves)):
                registro.append(registros[claves[i]][0])   
            verificar = bool 
            for code in registro:
                if str(code) == codigo:
                    verificar = True
                    break
                else:
                    verificar = False 
            if verificar == True:      
               print("No se puede eliminar esta estacion porque tiene valores asociados.")  
            else:
                 x = cargar_archivo(archivo)
                 texto = []
                 for linea in x:
                    if nombre not in linea:
                        texto.append(linea)
                 nuevoregistro = ""
                 for element in texto:
                    for character in element: 
                        nuevoregistro =  nuevoregistro + character
                    nuevoregistro =  nuevoregistro + "\n"
                 x = open(archivo,"w")
                 x.write(nuevoregistro)
                 x.close()
                 print("Estacion eliminada exitosamente.")
                 ciclo = 1
        else:
            print("Ingrese una estacion que este en la lista y hagalo correctamente.")

def cargar_variables(archivo):
    """
    Carga la información de las variables desde el archivo de texto a la memoria del programa.
    Retorna las variables con su rango y unidad.
    """
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

def cargar_registros(archivo):
    """
    Carga la información de los registros desde el archivo de texto a la memoria del programa.
    Retorna los registros con la fecha, código de estación y valores de variables.
    """
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

def crear_registro(archivo,codigo):
    """
    Guarda un nuevo registro en la base de datos.
    Recibe la información del registro: fecha, código de estación y valores de variables.
    """
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

def validar_fecha(fecha):
    
    '''
    Pa una fecha válida (yyyy-mm-dd)
    La fecha es el string a validar
    return -> Boolean (True or False) si es valido o no
    '''

def validar_valor_medida(valor, rango):
    """
    Valida que un valor de medida esté dentro del rango especificado.
    Recibe el valor y un rango en formato (mínimo, máximo).
    Retorna True si el valor está dentro del rango, False si no lo esta.
    """
def procesar_registro():
    """
    Procesa un registro de medidas ingresadas por un operador, incluyendo la validacion de los valores.
    Retorna el registro procesado con los valores validados y 'ND' convertidos a -999.
    """
def generar_reportes(registros_originales, registros_v2):
    """
    Genera dos reportes de registros de medidas: uno con las medidas comunes y otro con todas las medidas.
    Recibe dos listas de registros originales y registros duplicados.
    Retorna los registros comunes y los registros únicos de cada versión.
    """
def mostrar_estadisticas():
    """
    Muestra las estadísticas de las medidas tomadas en las estaciones.
    Recibe los registros de medidas, las variables a analizar, los municipios seleccionados, el periodo de tiempo y el modo de visualización.
    Muestra por pantalla o guarda en un archivo las estadísticas según las especificaciones.
    """