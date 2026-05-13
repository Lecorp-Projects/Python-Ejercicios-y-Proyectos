def cargar_archivo(archivo):
    """
    Esta funcion es pa abrir un archivo de texto, leerlo y poner los datos como tipos de datos establecidos.
    """
    abrir = open(archivo, "r")
    texto = []
    for char in abrir:
        char = char.strip()
        texto.append(char)
    return(texto)

def cargar_cursos_viejito(lista):
    curso = ""
    contador = 0 
    for element in lista:
        if "," in element: 
            for char in element:
                contador += 1
                curso = curso + char
            cursos = curso.split(", ")
            print(contador)
            return(cursos)
        
def cargar_cursos(lista):
    contador = 0 
    for element in lista:
        contador += 1
        if "," in element:
            cursos = element.split(",")
            print(contador)
            return(cursos)
archivo = "database_p7.txt"
lista = cargar_archivo(archivo)
print("Iteraciones version 1.")
cargar_cursos_viejito(lista)
print("Iteraciones version 2.")
cargar_cursos(lista)