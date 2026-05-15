# ============================================================
# Verificación de palabras palíndromas por comparación de extremos
# ============================================================
# Este programa solicita una palabra y determina si es palíndroma,
# comparando sus letras desde los extremos hacia el centro.
#
# Para realizar la verificación:
# - La palabra se convierte a minúsculas.
# - Se compara la primera letra con la última, la segunda con la
#   penúltima, y así sucesivamente.
# - Si alguna pareja de letras no coincide, se concluye que la
#   palabra no es palíndroma.
#
# Este ejercicio practica manejo de índices, ciclos while,
# condicionales y uso de break y else en ciclos.
# ============================================================

palabra = str(input("Ingrese una palabra para ver si esta es palindroma: "))
palabra = palabra.lower()
#Pa tenerlo todo en minusculas
i = 0
f = len(palabra)-1
while i < f:
    if palabra[i] != palabra[f]:
        print("La palabra no es palindroma.")
        break 
    i = i + 1 
    f = f - 1
else:
    print("La palabra es palindroma.")
    
        
        
        
    