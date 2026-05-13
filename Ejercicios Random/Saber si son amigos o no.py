# ============================================================
# Verificador de números amigos
# ============================================================
# Este programa permite comprobar si dos números son amigos.
#
# Dos números se consideran amigos cuando la suma de los divisores
# propios de cada uno da como resultado el otro número.
# Por ejemplo, 220 y 284 son números amigos.
#
# Funcionalidades principales:
# - Calcular la suma de los divisores propios de un número.
# - Verificar si una pareja de números cumple la condición de amistad.
# - Permitir analizar varias parejas de números ingresadas por el usuario.
# ============================================================

def sumadivisores(numero):
    divisores = 0 
    limite = numero -1 
    for divisor in range (limite, 0, -1):
        if numero%divisor == 0 :
            divisores = divisores + divisor
    return(divisores)
def sonAmigos(numero1, numero2):
    a = sumadivisores(numero1)
    b = sumadivisores(numero2)
    if a == numero2 and b == numero1:
        return(True)
print("Este programa funciona para saber si dos numeros son o no son amigos.")
n = int(input("Cuantas parejas de numeros va a ingresar: "))
p = 0
for i in range(n):
    p = p + 1
    print("Pareja",p)
    num1 = int(input("Ingrese el numero 1: "))
    num2 = int(input("Ingrese el numero 2: "))
    x = sonAmigos(num1,num2)
    if x == True:
        print(num1," y ",num2,":",sep="")
        print("Son amigos")
    else:
        print(num1," y ",num2,":",sep="")
        print("No son amigos")
        
        
    
