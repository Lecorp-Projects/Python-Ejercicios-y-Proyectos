#Hugo Esteban Barrero Garci­a 
#Grupo 4
#Dado el valor de los lados de un triangulo Isosceles, haga un algoritmo que calcule su peri­metro, su altura y su area.
#Ejemplo: a = 5, b = 8, entonces altura = 3, area = 12 y perimetro = 18.
print("Para hallar el valor del area, peri­metro y altura de un triangulo isosceles ingrese los valores de los lados como numeros enteros:")
a = float(input("Ingrese el valor de los lados iguales "))
# a es una variable de entrada y auxiliar que va a guardar los valores de los lados iguales del triangulo. 
b = float(input("Ingrese el valor de la base o el lado diferente "))
# a es una variable de entrada y auxiliar que va a guardar el valor de la base del triangulo. 
if (a < 0 or b<0):
    print("Los lados de un triangulo no deben ser negativos, ingrese otro valor")
    a = float(input("Ingrese el valor de los lados iguales "))
    b = float(input("Ingrese el valor de la base o el lado diferente "))
    #Esto es en caso que se lleguen a ingresar valores negativos. 
h = float((((a)**2)-((b**2)/4))**0.5)
#Ahora se halla la altura con esa operacion y se denomina con la variable auxiliar: h. 
p = (2*a)+b 
#Ahora se halla el peri­metro con esa operacion y se denomina con la variable auxiliar: p. 
A = (b*h)/2
#Ahora se halla el area con esa operacion y se denomina como la variable auxiliar: A. 
print ("La altura del triangulo es ",  round(h,2))
print ("El area del triangulo es ", round(A,2))
print ("Y el perimetro del triangulo es ", round(p,2))
#Ahora se imprimen los valores de las variables h, p y A, como datos de salida. Estos valores se redondean con la funcion round a dos decimales porque podrian llegar a tener mas. 
 


