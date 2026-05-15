# Python - Ejercicios, Proyectos y Documentación

Este repositorio reúne ejercicios, prácticas, proyectos y documentos de consulta desarrollados durante mi proceso de aprendizaje de Python.

El contenido está organizado para mostrar una evolución progresiva:

* Ejercicios iniciales de lógica y fundamentos.
* Prácticas enfocadas en cadenas, listas, matemáticas, patrones y algoritmos.
* Proyectos más completos con módulos, archivos, menús y procesamiento de datos.
* Manuales de referencia para repasar conceptos de Python Core.

---

## Estructura general del repositorio

```text
Python-Ejercicios-y-Proyectos/
│
├── documentos/
│   ├── Manual_de_Referencia_Python_Core.pdf
│   └── Manual_de_Referencia_Python_Core_Completo.pdf
│
├── ejercicios/
│   ├── algoritmos_aplicados/
│   ├── cadenas/
│   ├── fundamentos/
│   ├── juegos/
│   ├── listas/
│   ├── matematicas_y_geometria/
│   └── patrones_en_consola/
│
├── proyectos/
│   ├── analizador_calificaciones/
│   ├── sistema_inventario/
│   ├── sistema_monitoreo_ambiental/
│   └── sistema_gestion_notas/
│
└── README.md
```

---

# Documentación

La carpeta `documentos/` contiene manuales de consulta y repaso de Python.

## `Manual_de_Referencia_Python_Core.pdf`

Manual estructurado de repaso sobre conceptos centrales de Python, incluyendo:

* Objetos, nombres, variables y tipos.
* Tipos de datos básicos.
* Entrada y salida por consola.
* Operadores.
* Condicionales.
* Cadenas y Unicode.
* Indexación y slicing.
* F-strings.
* Ciclos.
* Colecciones.
* Diccionarios.
* Funciones.
* Scope y namespaces.
* Módulos e imports.
* Programación orientada a objetos.
* Excepciones.
* Archivos.
* Módulos estándar.
* Buenas prácticas y glosario técnico.

## `Manual_de_Referencia_Python_Core_Completo.pdf`

Versión ampliada y más explicativa del manual de referencia, pensada como documento de consulta más detallado.

Además de conservar los contenidos anteriores, profundiza en temas como:

* Parámetros opcionales y `None`.
* `print(..., end="")`.
* Formateo avanzado de texto y números.
* Slicing con índices positivos y negativos.
* Uso de `range()` con paso y recorridos inversos.
* Rutas de archivos y construcción de paths.
* Estructura de programas con `main()`.
* Explicaciones más intuitivas de conceptos técnicos que suelen generar dudas.

---

# Ejercicios

La carpeta `ejercicios/` contiene programas pequeños y medianos organizados por temática.

---

## `ejercicios/fundamentos/`

Ejercicios iniciales para practicar estructuras básicas de Python:

```text
contador_digitos.py
contrasena.py
dias_semana.py
elegibilidad_programador.py
numeros_pares.py
par_o_impar.py
practica_inicial_(primer_python).py
suma_numeros_anteriores.py
```

Temas trabajados:

* Entrada y salida de datos.
* Condicionales.
* Ciclos `for` y `while`.
* Acumuladores.
* Validaciones simples.
* Operadores aritméticos.
* Programas introductorios.

---

## `ejercicios/cadenas/`

Ejercicios centrados en manipulación de texto:

```text
codificador_por_desplazamiento.py
contar_mayusculas_minusculas.py
palindromo_comparando_extremos.py
palindromo_invirtiendo.py
reemplazar_letra_por_asterisco.py
vocal_o_consonante.py
```

Temas trabajados:

* Recorrido de strings.
* Comparación de caracteres.
* Conversión a minúsculas.
* Construcción progresiva de cadenas.
* Palíndromos.
* Búsqueda de letras.
* Reemplazo de caracteres.
* Codificación sencilla por desplazamiento alfabético.

---

## `ejercicios/juegos/`

Pequeños programas de interacción con el usuario:

```text
adivinar_numero.py
adivinar_numero_1-100.py
```

Temas trabajados:

* Números aleatorios.
* Ciclos hasta acertar.
* Comparaciones.
* Mensajes de orientación al usuario.
* Lógica de juego sencilla.

---

## `ejercicios/listas/`

Funciones creadas para comprender internamente operaciones básicas sobre listas:

```text
funciones.py
prueba_funciones.py
```

Se implementan prácticas relacionadas con:

* Contar elementos.
* Insertar valores.
* Agregar una lista al final de otra.
* Eliminar elementos por valor.
* Eliminar elementos por posición.
* Buscar posiciones.
* Invertir listas.
* Imprimir listas de diferentes formas.

El propósito de esta carpeta es practicar la lógica que hay detrás de métodos comunes como:

```python
.count()
.insert()
.extend()
.remove()
.index()
.reverse()
```

---

## `ejercicios/matematicas_y_geometria/`

Ejercicios numéricos, geométricos y matemáticos:

```text
maximo_comun_divisor.py
numeros_amigos.py
radianes_a_grados.py
solucion_ecuacion_cuadratica.py
triangulo_isosceles.py
volumen_caneca.py
```

Temas trabajados:

* Algoritmo de Euclides.
* Números amigos.
* Conversión de unidades.
* Fórmula cuadrática.
* Geometría.
* Uso de `math`.
* Cálculo de áreas, volúmenes y medidas derivadas.

---

## `ejercicios/algoritmos_aplicados/`

Ejercicios con situaciones contextualizadas:

```text
cambio_aceite.py
costo_streaming.py
costo_uso_bicicleta.py
maquina_expendedora.py
```

Temas trabajados:

* Tarifas por consumo.
* Conversión de horas a minutos o segundos.
* Condicionales encadenados.
* División entera y módulo.
* Descomposición de cantidades.
* Aplicaciones prácticas de lógica algorítmica.

---

## `ejercicios/patrones_en_consola/`

Generación de figuras usando texto:

```text
patron_asteriscos.py
patron_cruces.py
```

Temas trabajados:

* Ciclos `while`.
* Contadores.
* Repetición de cadenas.
* Patrones crecientes y decrecientes.
* Construcción visual en consola.

---

# Proyectos

La carpeta `proyectos/` contiene programas más completos y estructurados.

---

## `proyectos/analizador_calificaciones/`

Programa para registrar estudiantes y analizar sus notas.

Permite:

* Ingresar varios estudiantes.
* Registrar nombres y calificaciones.
* Calcular el promedio general.
* Contar aprobados y reprobados.
* Identificar la mejor nota.
* Mostrar estudiantes en recuperación.
* Trabajar mediante menú.

Este proyecto fue desarrollado teniendo como restricción evitar estructuras de datos más avanzadas y practicar el manejo manual de información.

---

## `proyectos/sistema_inventario/`

Proyecto de inventario desarrollado como práctica de organización y control de información.

Su propósito es aplicar lógica de programación para registrar, consultar y administrar datos asociados a productos o elementos almacenados.

---

## `proyectos/sistema_monitoreo_ambiental/`

Sistema modular en consola para administrar estaciones de monitoreo ambiental.

Incluye:

* Usuarios visitantes.
* Usuarios operadores.
* Usuarios administradores.
* Gestión de usuarios.
* Gestión de estaciones.
* Registro de mediciones.
* Consulta de datos por estación.
* Estadísticas por variables, municipios y periodos.
* Depuración de registros entre dos versiones de archivo.
* Persistencia de información en archivos `.txt`.

Estructura principal:

```text
sistema_monitoreo_ambiental/
│
├── main.py
├── funciones.py
├── utilidades.py
├── registros_.txt
├── registros_v2.txt
└── README.md
```

Este proyecto tiene documentación propia dentro de su carpeta.

---

## `proyectos/sistema_gestion_notas/`

Sistema de gestión y análisis de notas académicas para estudiantes de primer semestre de Medicina.

Incluye:

* Carga de datos desde archivo.
* Agregar y eliminar estudiantes.
* Promedio de estudiantes.
* Promedio de cursos.
* Promedio de un curso específico.
* Tres notas mayores por curso.
* Menor nota de un estudiante.
* Ordenamiento de estudiantes por promedio usando burbuja.
* Ordenamiento por cantidad de cursos usando selección.
* Guardado de cambios en archivo.
* Pruebas de caja negra.

Estructura principal:

```text
sistema_gestion_notas/
│
├── main.py
├── funciones.py
├── database_p7.txt
├── pruebas_caja_negra.py
└── README.md
```

Este proyecto también cuenta con documentación propia dentro de su carpeta.

---

# Ejecución de los programas

Para ejecutar un archivo individual:

```bash
python nombre_del_archivo.py
```

Ejemplo:

```bash
python ejercicios/fundamentos/par_o_impar.py
```

Para los proyectos con archivo principal `main.py`:

```bash
python main.py
```

Ejemplo:

```bash
cd proyectos/sistema_monitoreo_ambiental
python main.py
```

o:

```bash
cd proyectos/sistema_gestion_notas
python main.py
```

---

# Objetivo del repositorio

Este repositorio funciona como registro de aprendizaje y práctica en Python, desde ejercicios básicos hasta proyectos modulares más completos.

Busca reflejar el desarrollo progresivo de habilidades en:

* Pensamiento algorítmico.
* Resolución de problemas.
* Programación estructurada.
* Modularidad.
* Manejo de archivos.
* Validación de entradas.
* Procesamiento de datos.
* Ordenamiento y búsqueda.
* Diseño de menús interactivos.
* Documentación de código.
* Pruebas y revisión de funcionamiento.

---

# Nota

Los ejercicios conservan el enfoque con el que fueron desarrollados en cada momento del proceso de aprendizaje. Algunos programas son deliberadamente simples, mientras que otros muestran una mayor organización, modularidad y complejidad técnica.
