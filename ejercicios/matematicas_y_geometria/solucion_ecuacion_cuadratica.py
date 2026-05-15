# ============================================================
# Solucionador de ecuaciones cuadráticas
# ============================================================
# Este programa calcula las posibles soluciones reales de una
# ecuación de segundo grado de la forma:
#
# ax^2 + bx + c = 0
#
# Para resolverla, se calcula primero el discriminante:
# d = b^2 - 4ac
#
# Si el discriminante es mayor o igual que cero, se aplican las
# fórmulas para obtener las dos soluciones reales. Si es negativo,
# se informa que la ecuación no tiene solución en los números reales.
#
# Este ejercicio practica entrada de coeficientes, operaciones
# matemáticas, condicionales y uso de la fórmula cuadrática.
# ============================================================

print("Ingrese los valores de los coeficientes (en forma racional no fraccionaria) de una ecuacion de segundo grado de la forma ax^2+bx+c=0, para darle las posibles soluciones a la ecuacion.")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
#Las variables a, b y c son datos de entrada y variables auxiliares que tienen los valores de los coeficientes y el valor constante c.
d = ((b)**2-(4*a*c))
#La variable auxilar d es el valor del discriminante 
if (d>=0):    
    x1 = ((-b)+(d**0.5))/(2*a)
    x2 = ((-b)-(d**0.5))/(2*a)
#Las variables x1 y x2 son auxiliares y datos de salida que se imprimen en la pantalla. Estos valores se redondean con la funcion round a un decimal porque podrían llegar a tener mas. 
    print("Las soluciones de la ecuacion son", round(x1,1), "y",round(x2,1),".")
#La solucion solo es posible si el discriminante es positivo, si es un numero negativo, los resultados no existen en los numeros reales. 
else: 
#No hay solucion en los reales en caso que el discriminante sea negativo y se imprime esto en pantalla. 
    print("Los valores de esa ecuación no tienen solución en los reales.")
    

