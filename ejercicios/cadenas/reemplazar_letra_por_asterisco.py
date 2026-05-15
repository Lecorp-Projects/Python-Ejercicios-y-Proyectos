# ============================================================
# Ocultamiento de letras en una frase
# ============================================================
# Este programa solicita una palabra o frase y luego pide una letra.
# Cada vez que esa letra aparece dentro del texto, se reemplaza por
# un asterisco, manteniendo intactos los demás caracteres.
#
# Funcionalidades principales:
# - Recorrer una frase carácter por carácter.
# - Comparar cada carácter con la letra indicada por el usuario.
# - Construir un nuevo texto reemplazando coincidencias por "*".
# - Mostrar el resultado final en pantalla.
#
# Este ejercicio practica recorridos sobre cadenas de texto,
# condicionales dentro de ciclos y construcción progresiva de strings.
# ============================================================

frase = str(input("Ingrese una palabra o frase: "))
letra = str(input("Ahora ingrese una letra y todas las veces que este esa letra en la frase se van a cambiar por un asterisco: "))
secreta = ""
for i in frase: 
    if i == letra:
        secreta = secreta + "*"
    else: 
        secreta = secreta + i 
print (secreta)
    
    
                  