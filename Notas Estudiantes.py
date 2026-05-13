menu = """
Opcion 1) Ingresar datos.
Opcion 2) Ver analisis.
Opcion 3) Salir.
"""
opcion = 0
def estudiantes ():
    numero = int(input("Cuantos estudiantes desea registrar: "))
    return(numero)

def datos():
    numero = estudiantes()
    x = ""
    for i in range(numero):
        print("Estudiante ", i+1)
        nombre = input("Ingrese el nombre del estudiante: ")
        while True:
            try:
                nota = float(input("Ingrese la nota del estudiante: "))
                if nota < 0 or nota > 10:
                    print("Ingrese una nota valida (entre 0 y 10)")
                    continue
                break
            except ValueError:
                print("Ingrese un numero valido para la nota")
        x = x + nombre + str(i) + str(nota) 
    return(x,numero)

def comparaciones(registro, numero):
    mayor = -1
    menor = 10
    for i in range(numero):
        nota = float(registro[registro.find(str(i))+len(str(i)):registro.find(str(i))+len(str(i))+3])
        if nota > mayor:
            mayor = nota
        if nota < menor:
            menor = nota
    print("La nota mayor es: ", mayor)
    print("La nota menor es: ", menor)

while opcion != 3:
    print(menu)
    opcion = input("Ingrese un numero el 1 y 3 (1,2 o 3), para ver que opcion quiere escoger: ")
    if opcion == "1":
        registro, numero = datos()

    elif opcion == "2":
        comparaciones(registro, numero)
        

    elif opcion == "3":
        break

    else:
        print("Ingrese un dato valido")