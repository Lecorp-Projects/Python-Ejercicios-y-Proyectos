# ============================================================
# Verificación de palabras palíndromas por inversión
# ============================================================
# Este programa solicita una palabra y determina si es palíndroma,
# es decir, si se lee igual de izquierda a derecha y de derecha
# a izquierda.
#
# Para realizar la verificación:
# - La palabra se convierte a minúsculas.
# - Se construye una nueva palabra recorriendo la original al revés.
# - Se comparan ambas cadenas para saber si son iguales.
#
# Este ejercicio practica recorridos de cadenas, uso de índices,
# ciclos while y construcción progresiva de texto.
# ============================================================

palabra = str(input("Ingrese una palabra para ver si esta es palindroma: "))
palabra = palabra.lower()
#Pa tenerlo todo en minusculas
palabrados = ""
i = 0
f = len(palabra) - 1
while i < len(palabra):
    palabrados = palabrados + palabra[f]
    i = i+1
    f = f-1
if palabra == palabrados:
    print("Es palindroma")
else:
    print("No es palindroma")