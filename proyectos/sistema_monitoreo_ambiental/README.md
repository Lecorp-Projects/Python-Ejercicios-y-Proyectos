````markdown
# Sistema de Monitoreo Ambiental

Este proyecto implementa un sistema de información en consola para administrar estaciones de monitoreo ambiental y registrar mediciones de variables relacionadas con calidad del aire y condiciones climáticas.

El programa fue desarrollado como una práctica de programación en Python enfocada en el uso de:

- Cadenas de texto.
- Listas.
- Diccionarios.
- Funciones.
- Programación modular.
- Lectura y escritura de archivos de texto.
- Validación de datos ingresados por teclado.

---

## Descripción general

El sistema simula una plataforma de monitoreo ambiental en la que existen:

- Usuarios visitantes.
- Usuarios registrados.
- Administradores.
- Operadores.
- Municipios.
- Estaciones de monitoreo.
- Variables ambientales.
- Registros de mediciones.

Toda la información se almacena de forma persistente en un archivo de texto llamado:

```text
registros_.txt
````

El programa lee este archivo, carga la información en memoria mediante estructuras de datos y actualiza el archivo cuando se crean, editan o eliminan datos.

---

## Funcionalidades

### Usuario visitante

Puede consultar estadísticas de las mediciones registradas.

El visitante puede:

* Seleccionar un periodo de análisis:

  * Últimos 7 días.
  * Últimos 30 días.
  * Rango de fechas manual.
* Elegir una, varias o todas las variables.
* Elegir uno, varios o todos los municipios.
* Visualizar los resultados por pantalla o guardarlos en un archivo `Estadisticas.txt`.

Las estadísticas calculadas son:

* Valor mínimo.
* Estación y fecha del valor mínimo.
* Valor máximo.
* Estación y fecha del valor máximo.
* Promedio.

---

### Usuario operador

Debe autenticarse con documento y contraseña.

Puede:

* Seleccionar un municipio.
* Elegir una estación perteneciente a ese municipio.
* Consultar las medidas registradas para la estación.
* Ingresar nuevas medidas.

Al ingresar medidas:

* La fecha y hora se toman automáticamente.
* Cada valor se valida según el rango permitido para su variable.
* Si una medición no está disponible, se puede ingresar `ND`, y el sistema la guarda como `-999.0`.

---

### Usuario administrador

Debe autenticarse con documento y contraseña.

Puede:

#### Gestionar usuarios

* Crear usuarios.
* Editar usuarios.
* Eliminar usuarios, excepto el usuario que tiene la sesión activa.

Las validaciones aplicadas son:

* Documento de exactamente 10 dígitos numéricos.
* Nombre compuesto solo por letras y espacios.
* Contraseña de mínimo 4 caracteres.
* Confirmación de contraseña.
* Rol válido: `Administrador` u `Operador`.

#### Gestionar estaciones

* Crear estaciones.
* Editar estaciones.
* Eliminar estaciones únicamente si no tienen registros asociados.

Al crear una estación:

* Se genera automáticamente un código incremental.
* Se debe seleccionar uno de los municipios disponibles.

#### Depurar registros duplicados

El sistema puede comparar el archivo principal con una segunda versión llamada:

```text
registros_v2.txt
```

A partir de esa comparación genera:

* Un reporte con los registros comunes en ambos archivos.
* Un reporte con la unión de los registros, sin repetirlos.

---

## Estructura de archivos

```text
Sistema de Monitoreo Ambiental/
│
├── Main.py
├── funciones.py
├── utilidades.py
├── registros_.txt
├── registros_v2.txt
└── README.md
```

---

## Descripción de los archivos

### `Main.py`

Contiene:

* El menú inicial.
* La navegación de usuarios visitantes, operadores y administradores.
* La conexión entre las opciones del menú y las funciones del sistema.
* La construcción de rutas para localizar correctamente los archivos `.txt` desde la carpeta del proyecto.

### `funciones.py`

Contiene la lógica principal del proyecto:

* Carga y escritura del archivo de datos.
* Autenticación.
* Gestión de usuarios.
* Gestión de estaciones.
* Registro de medidas.
* Estadísticas.
* Comparación y depuración de registros.

### `utilidades.py`

Contiene funciones de apoyo:

* Validación de nombres.
* Validación de documentos.
* Validación de fechas.
* Verificación de años bisiestos.
* Impresión de tablas en consola.
* Limpieza visual de pantalla.

### `registros_.txt`

Es la base de datos en texto plano del sistema. Contiene:

* Usuarios registrados.
* Lista de municipios.
* Estaciones de monitoreo.
* Variables ambientales.
* Registros de mediciones.

### `registros_v2.txt`

Es una segunda versión del archivo de datos utilizada para probar la funcionalidad de depuración de registros. Contiene una estructura equivalente a `registros_.txt`, pero con diferencias en algunos registros de mediciones.

---

## Formato del archivo de datos

El archivo `registros_.txt` sigue esta estructura:

```text
<DOCUMENTO;NOMBRE_COMPLETO;CONTRASEÑA;ROL>
:MUNICIPIO1,MUNICIPIO2,MUNICIPIO3
CODIGO_ESTACION,NOMBRE_ESTACION,MUNICIPIO
VARIABLE[MINIMO:MAXIMO,UNIDAD];VARIABLE[MINIMO:MAXIMO,UNIDAD]
YYYY-MM-DD HH:MM:SS;CODIGO_ESTACION;{VALOR1,VALOR2,VALOR3}
```

Ejemplo:

```text
<1010101010;Mariana Montoya;1234;Administrador>
<1111111111;Elkin Perez;1234;Operador>
:Medellin,Bello,Itagui,Caldas,La Estrella,Barbosa
1,Universidad San Buenaventura,Medellin
PM10[0.0:100.0,ug/m3];Temperatura[-20.0:50.0,°C]
2019-07-01 00:00:00;1;{3.5,27.0}
```

---

## Ejecución

Para iniciar el programa, ejecutar:

```bash
python Main.py
```

El programa puede ejecutarse desde VS Code, Spyder o una terminal.
Las rutas de los archivos de datos se construyen a partir de la ubicación de `Main.py`, por lo que el sistema busca correctamente `registros_.txt` y `registros_v2.txt` dentro de la misma carpeta del proyecto.

---

## Usuarios disponibles en el archivo base

El archivo `registros_.txt` incluye usuarios de prueba que permiten ingresar al sistema:

| Documento  | Nombre          | Contraseña | Rol           |
| ---------- | --------------- | ---------- | ------------- |
| 1010101010 | Mariana Montoya | 1234       | Administrador |
| 1111111111 | Elkin Perez     | 1234       | Operador      |
| 1212121212 | Camila Serna    | 1234       | Administrador |
| 1313131313 | Oscar Jaramillo | 1234       | Operador      |

---

## Observaciones

* El programa modifica `registros_.txt` al crear, editar o eliminar usuarios, estaciones o registros.
* Para hacer pruebas sin alterar la base original, se recomienda conservar una copia del archivo inicial.
* Las estadísticas de “últimos 7 días” y “últimos 30 días” dependen de que existan registros recientes en el archivo. Si se usa el archivo base original, puede ser más útil probar la opción de fechas manuales.
* La opción de depuración requiere el archivo adicional `registros_v2.txt`.
* Si el usuario guarda estadísticas en archivo, se genera un documento llamado `Estadisticas.txt`.

---

## Propósito del proyecto

Este proyecto busca aplicar de manera integrada conceptos fundamentales de programación en Python, construyendo un sistema funcional con:

* Modularidad.
* Persistencia básica de datos.
* Validaciones.
* Menús interactivos.
* Procesamiento de registros.
* Generación de reportes.

```
```
