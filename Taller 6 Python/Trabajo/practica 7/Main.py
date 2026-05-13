#Jose Gabriel Giraldo F
#Hugo Esteban Barrero 
#Grupo 4

from Funciones import *
archivo = input("Ingrese el nombre del archivo de la base de datos sobre la que se desea trabajar: ")
lista = cargar_archivo(archivo)
estudiantes = cargar_estudiantes(lista)
notas = cargar_notas(lista)
cursos = cargar_cursos(lista)
notasfloat(notas)
print('')
print("BIENVENIDO AL SISTEMA DE GESTION DE NOTAS DE LA UNIVERSIDAD DE ANTIOQUIA.")
print('')
while True:
        menu()
        print('')
        opcion = input("Ingrese el número de la opción deseada: ")
        if opcion == '1':
            eliminar_estudiante(estudiantes, notas)
            print('')
        elif opcion == '2':
            agregar_estudiante(estudiantes,notas,cursos)
            notasfloat(notas)
            print('')
        elif opcion == '3':
            promedio_estudiantes_print(estudiantes,notas)
            print('')
        elif opcion == '4':
            promedio_cursos(cursos,notas)
            print('')
        elif opcion == '5':
            promedio_curso(cursos, notas)
            print('')
        elif opcion == '6':
            tresNotasMayores(estudiantes,cursos,notas)
            print('')
        elif opcion == '7':
            menorNotaEstudiante(estudiantes,cursos,notas)
            print('')
        elif opcion == '8':
            ordenarPromedioEstudiantes(estudiantes,notas)
            print('')
        elif opcion == '9':
            ordenarEstudiantesCantidadCursos(estudiantes,notas)
            print('')
        elif opcion == '10':
            print("Gracias por usar el sistema. ¡Hasta luego!")
            escribir_codigo(archivo, estudiantes, notas, cursos)
            break
        else:
            print("Por favor ingrese un numero valido entre 1 y 10.")