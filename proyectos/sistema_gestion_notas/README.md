# Sistema de Gestión de Notas

Este proyecto implementa un sistema en consola para administrar y analizar las notas de estudiantes de primer semestre de Medicina de la Universidad de Antioquia.

El programa fue desarrollado como una práctica de programación en Python enfocada en:

* Manejo de listas.
* Uso de matrices representadas como listas bidimensionales.
* Programación modular mediante funciones.
* Lectura y escritura de archivos de texto.
* Validación de datos.
* Cálculo de estadísticas académicas.
* Búsqueda de información.
* Implementación de algoritmos de ordenamiento.
* Pruebas de caja negra.
* Análisis de eficiencia en procesos de carga y procesamiento de datos.

---

## Descripción general

El sistema trabaja con tres estructuras de datos principales:

* Una lista de cursos.
* Una lista de estudiantes identificados por documento.
* Una matriz de notas.

Estas estructuras se administran de forma paralela:

* Cada posición de la lista de estudiantes corresponde a una fila de la matriz de notas.
* Cada posición de la lista de cursos corresponde a una columna de la matriz.

De esta forma, la nota ubicada en:

```text
notas[i][j]
```

representa la nota del estudiante `i` en el curso `j`.

---

## Significado de los valores especiales

Dentro de la matriz de notas se usan dos valores especiales:

```text
-1
```

Indica que el estudiante canceló el curso.

```text
-2
```

Indica que el estudiante no está inscrito en el curso.

Estos valores no se tienen en cuenta al calcular promedios.

---

## Funcionalidades

El menú principal del sistema permite:

1. Cargar o recargar datos desde archivo.
2. Eliminar un estudiante.
3. Agregar un estudiante.
4. Ver el promedio de cada estudiante.
5. Ver el promedio de todos los cursos.
6. Ver el promedio de un curso específico.
7. Ver las tres notas mayores de un curso.
8. Ver la menor nota de un estudiante.
9. Ordenar estudiantes por promedio.
10. Ordenar estudiantes por cantidad de cursos matriculados.
11. Guardar cambios y salir.

---

## Funcionalidades detalladas

### Cargar datos desde archivo

El sistema lee un archivo de texto con la información de:

* Cursos.
* Documentos de estudiantes.
* Matriz de notas.

Los datos se cargan en memoria para poder ser consultados y modificados durante la ejecución del programa.

---

### Eliminar estudiante

Permite eliminar un estudiante a partir de su número de documento.

Al hacerlo:

* Se elimina el documento de la lista de estudiantes.
* Se elimina también la fila correspondiente en la matriz de notas.

---

### Agregar estudiante

Permite registrar un nuevo estudiante con:

* Documento válido de 10 dígitos.
* Notas para todos los cursos registrados.

Para cada curso se puede ingresar:

* Una nota entre `0.0` y `5.0`.
* `-1` si canceló el curso.
* `-2` si no está inscrito.

---

### Promedio de estudiantes

Calcula el promedio de cada estudiante ignorando:

* Cursos cancelados (`-1`).
* Cursos no inscritos (`-2`).

El resultado se muestra por pantalla junto al documento de cada estudiante.

---

### Promedio de cursos

Calcula el promedio de cada curso considerando únicamente notas válidas.

No se incluyen en el promedio:

* `-1`
* `-2`

---

### Promedio de un curso específico

Permite seleccionar un curso de la lista y visualizar su promedio individual.

---

### Tres notas mayores de un curso

Solicita un curso y muestra las tres notas más altas registradas.

Si varios estudiantes tienen la misma nota, se reportan todos los documentos asociados a ese valor.

---

### Menor nota de un estudiante

Solicita el documento de un estudiante y muestra:

* Su menor nota válida.
* El curso o los cursos en los que obtuvo ese resultado.

---

### Ordenar estudiantes por promedio

Muestra los estudiantes ordenados de mayor a menor según su promedio académico.

Para cumplir con los requisitos de la práctica, esta funcionalidad usa una estrategia de:

```text
Ordenamiento burbuja
```

---

### Ordenar estudiantes por cantidad de cursos

Muestra los estudiantes ordenados de mayor a menor según la cantidad de cursos matriculados.

No se cuentan como cursos matriculados los valores:

* `-1`
* `-2`

Para cumplir con los requisitos de la práctica, esta funcionalidad usa:

```text
Ordenamiento por selección
```

---

### Guardar cambios y salir

Al finalizar el programa, se actualiza el archivo de datos con los cambios realizados durante la ejecución, como:

* Estudiantes agregados.
* Estudiantes eliminados.
* Nuevas notas asociadas.

---

## Estructura del proyecto

```text
sistema_gestion_notas/
│
├── main.py
├── funciones.py
├── database_p7.txt
├── pruebas_caja_negra.py
└── README.md
```

De manera opcional, puede conservarse una carpeta de documentación:

```text
documentacion/
└── informe_eficiencia_y_pruebas.docx
```

---

## Descripción de los archivos

### `main.py`

Contiene:

* El flujo principal del programa.
* El menú interactivo.
* La carga inicial de datos.
* La conexión entre las opciones del usuario y las funciones del sistema.
* La construcción de la ruta del archivo `database_p7.txt`.

---

### `funciones.py`

Contiene toda la lógica del proyecto:

* Lectura y escritura del archivo de datos.
* Validación de documentos y notas.
* Agregar y eliminar estudiantes.
* Cálculo de promedios.
* Búsqueda de notas.
* Ordenamiento por burbuja y por selección.
* Funciones auxiliares de impresión y procesamiento.

---

### `database_p7.txt`

Contiene la base de datos inicial del sistema.

Guarda:

* La lista de cursos.
* La lista de documentos de estudiantes.
* La matriz de notas.

---

### `pruebas_caja_negra.py`

Contiene pruebas automáticas sencillas para verificar funciones importantes del sistema, tales como:

* Validación de documentos.
* Cálculo de promedio de cursos.
* Identificación de las tres notas mayores.
* Ordenamiento de datos con volumen mayor.

---

## Formato del archivo de datos

El archivo `database_p7.txt` tiene la siguiente estructura:

```text
Curso1, Curso2, Curso3, Curso4, Curso5
Documento1 Documento2 Documento3 Documento4

NotaE1C1 NotaE1C2 NotaE1C3 NotaE1C4 NotaE1C5
NotaE2C1 NotaE2C2 NotaE2C3 NotaE2C4 NotaE2C5
NotaE3C1 NotaE3C2 NotaE3C3 NotaE3C4 NotaE3C5
```

Ejemplo:

```text
Curso1, Curso2, Curso3, Curso4, Curso5
1033492448 1032090603 1002152167 1028854736 1014191590 1024351175

-1 1.1 4.8 4.2 1.5
0.4 4.4 -1 4.5 3.3
2.1 3.1 2.5 1.8 2.8
3.4 3.7 4.2 -2 3.4
4.6 4.9 4.4 1.6 3.2
4 2.4 2.3 0.1 4.1
```

---

## Ejecución

Para iniciar el programa, ejecutar:

```bash
python main.py
```

Al comenzar, el sistema muestra el menú principal.

Para cargar la base de datos inicial:

1. Elegir la opción `1`.
2. Presionar `Enter` cuando se solicite el archivo para usar el archivo predeterminado:

```text
database_p7.txt
```

El programa construye la ruta del archivo a partir de la ubicación de `main.py`, por lo que puede localizarlo correctamente aunque se ejecute desde VS Code, Spyder o una terminal.

---

## Ejecución de pruebas

Para ejecutar las pruebas de caja negra:

```bash
python pruebas_caja_negra.py
```

Si todas las pruebas se ejecutan correctamente, se mostrará un mensaje final indicando que finalizaron sin errores.

---

## Validaciones implementadas

El programa valida:

### Documento

* Debe tener exactamente 10 dígitos.
* Solo puede contener números.

### Nota

Debe ser uno de estos valores:

* Número entre `0.0` y `5.0`.
* `-1` para curso cancelado.
* `-2` para estudiante no inscrito.

### Selección de opciones

El programa valida que las opciones elegidas por el usuario correspondan a valores disponibles dentro del menú o de las listas mostradas.

---

## Algoritmos de ordenamiento utilizados

### Burbuja

Se usa para ordenar estudiantes por promedio de mayor a menor.

### Selección

Se usa para ordenar estudiantes por cantidad de cursos matriculados.

Estas implementaciones se realizaron manualmente, sin usar funciones avanzadas de ordenamiento, de acuerdo con los requisitos de la práctica.

---

## Propósito del proyecto

Este proyecto integra conceptos fundamentales de programación estructurada en Python mediante la construcción de un sistema funcional de gestión académica.

Permite practicar:

* Modularidad.
* Persistencia de datos en archivos.
* Trabajo coordinado entre listas y matrices.
* Validación de entradas.
* Cálculo de estadísticas.
* Búsqueda de información.
* Implementación manual de algoritmos de ordenamiento.
* Diseño de pruebas para verificar el funcionamiento del código.
