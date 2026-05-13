#Hugo Esteban Barrero Garci�a
#Grupo 4
#Haga un algoritmo que muestre en pantalla las soluciones de la ecuacion ax2+bx+c=0, dados valores para los coeficientes a, b y la constante c.
#Ejemplo1: a = 1, b = -5, c = 6.Entonces las soluciones son x1 = 3, x2 = 2. 
#Ejemplo2: a = 2, b = 4, y c = -6.Entonces las soluciones son x1 = 1, x2 = -3. 
#Ejemplo3: a = 3, b = 2, c = 1. La solucion no existe en los reales. 
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
    

