# ============================================================
# Conteo de dígitos de un número entero
# ============================================================
# Este programa permite saber cuántos dígitos tiene un número
# entero ingresado por el usuario.
#
# Para hacerlo, el número se divide sucesivamente entre 10 hasta
# llegar a 0. Cada división representa un dígito contado.
#
# También se contempla el caso del número 0 y de números negativos,
# contando únicamente sus cifras y no el signo.
# ============================================================

#Algoritmo noje 
#	Escribir "Ingrese entero pa sacar sus digitos"
#	Leer n
#	c <- 0
#	Mientras n>0 Hacer
#		c <- c+1
#		n <- trunc(n/10)
#	FinMientras
#	Escribir c
#FinAlgoritmo

def contardigitos(numero):
    if numero < 0:
        numero = numero * -1

    if numero == 0:
        return(1)

    c = 0

    while numero > 0:
        c = c + 1
        numero = numero // 10

    return(c)


print("Este programa funciona para saber cuantos digitos tiene un numero entero.")

n = int(input("Ingrese un numero entero para sacar sus digitos: "))

x = contardigitos(n)

print("El numero", n, "tiene", x, "digitos.")
