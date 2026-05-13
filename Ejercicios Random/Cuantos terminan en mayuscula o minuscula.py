#Lea nombres y calcule cuantos finalizan en letra mayuscula y cuantos en letra minuscula.
def terminacion(palabra):
    ultimaletra = palabra[len(palabra)-1]
    if ultimaletra == ultimaletra.lower():
        return(True)
def cuantosterminan(numero):
    terminamin = 0
    terminamay = 0
    x = 0
    for i in numero :
        x = x + 1
        nombre = input("Ingrese nombre",x)
        if terminacion(nombre) == True:
            terminamin = terminamin + 1
        else:
            terminamay = terminamay +1
    return(terminamay,terminamin)
n = int(input("Ingrese cuantos nombres va a ingresar"))
a = cuantosterminan(n)
print("Mayusculas:",a,"Minusculas",a )
        
            
    


        
