# ============================================================
# Cálculo de devueltas en monedas
# ============================================================
# Este programa calcula cómo devolver una cantidad de dinero usando
# la menor cantidad posible de monedas disponibles.
#
# Denominaciones utilizadas:
# - 1000 pesos
# - 500 pesos
# - 200 pesos
# - 100 pesos
# - 50 pesos
#
# El programa va calculando cuántas monedas de cada denominación
# se pueden entregar y cuánto dinero queda como residuo cuando no
# es posible dar una devuelta exacta.
#
# Este ejercicio practica división entera, operador módulo,
# descomposición de cantidades y cálculo de residuos.
# ============================================================

dinero = float(input("Ingrese la cantidad de dinero que desea ser devuelta en monedas: "))
#dinero es una variable auxiliar y un dato de entrada. 
a = dinero//1000
#La variable auxiliar a son la cantidad de monedas de mil que se devuelven. 
a1 = dinero%1000
#La variable auxiliar a1 es la cantidad que sobra despues de saber la cantidad de monedas de mil necesarias. 
b = a1//500
#La variable auxiliar b son la cantidad de monedas de 500 que se devuelven. 
b1 = a1%500
#La variable auxiliar b1 es la cantidad que sobra despues de saber la cantidad de monedas de 500 necesarias. 
c = b1//200
#La variable auxiliar c son la cantidad de monedas de 200 que se devuelven. 
c1 = b1%200
#La variable auxiliar c1 es la cantidad que sobra despues de saber la cantidad de monedas de 200 necesarias. 
d = c1//100
#La variable auxiliar d son la cantidad de monedas de 100 que se devuelven. 
d1 = c1%100
#La variable auxiliar d1 es la cantidad que sobra despues de saber la cantidad de monedas de 100 necesarias. 
e = d1//50
#La variable auxiliar e son la cantidad de monedas de 50 que se devuelven. 
e1 = d1%50
#La variable auxiliar e1 es la cantidad que sobra despues de saber la cantidad de monedas de 50 necesarias. 
r = e1
#Por lo tanto la variable auxiliar r es el residuo, osea lo que llega a faltar para una devuelta mas exacta. 

if (dinero<50 or dinero<0):
    print("Ombe no hay monedas de menos de 50, no te devolvemos nada.")
#Esto es por si al usuario le da por ser charrito y poner valores negativos o muy bajitos. 
else:
#Las variables auxiliares a, b, c, d, e, r se imprimen como datos de salida.
    print('Se le devuelven las siguientes denominaciones de peso en monedas:') 
    print(int(a), "de mil.")
    print(int(b), "de 500.")
    print(int(c), "de 200.")
    print(int(d), "de 100.")
    print(int(e),"de 50.")
    print(int(r),"que resta para dar una devuelta mas exacta.")
	

