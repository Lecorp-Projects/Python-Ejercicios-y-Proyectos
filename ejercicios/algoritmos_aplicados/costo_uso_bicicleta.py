# ============================================================
# Cálculo de cobro por uso de bicicleta pública
# ============================================================
# Este programa calcula el valor que debe pagar un usuario por el
# uso de una bicicleta pública según el tiempo total utilizado.
#
# El usuario puede ingresar el tiempo de dos formas:
# - Directamente en minutos.
# - Separado en horas y minutos.
#
# Reglas principales:
# - Hasta 100 minutos se cobra una tarifa base por minuto.
# - Después de 100 minutos se aplica un sobrecargo por tiempo extra.
# - Si el uso supera las 24 horas, se aplica un sobrecargo fijo.
#
# Este ejercicio practica condicionales, conversión de horas a
# minutos, operaciones aritméticas y cálculo de tarifas.
# ============================================================

x = int(input("Ingrese el tiempo que hizo uso de la bicicleta para calcular lo que debe pagar, si el tiempo lo va a ingresar en minutos, ingrese 0, si lo va a hacer en horas y minutos, ingrese 1: "))
#La variable x es un valor de entrada para ver el usuario como prefiere ingresar los datos. 
if(x==1): 
#Si ingresan 1 ahora se le pediran los valores de uso en horas y en minutos.
   t = int(input("Ingrese las horas de uso: "))
#t es una variable de entrada y auxiliar que guarda el valor de las horas de uso. 
   h = t*60
#h es una variable auxiliar que convierte el valor ingresado en horas y lo pasa a minutos. 
   m = int(input("Ingrese los minutos de uso: "))
#m es una variable de entrada y auxiliar que guarda el valor de los minutos de uso. 
   m = m + h 
#m es una variable de entrada que almacena todo el tiempo de uso, convertido a minutos.
elif (x==0):
#Si ingresan 0 ahora se le pediran el valor de uso en minutos.
       m = int(input("Ingrese los minutos de uso: "))
#m es una variable de entrada y auxiliar que guarda el valor de los minutos de uso. 
else:
       print("Se le pidio que ingrese un valor entre 0 y 1")
#Esto aparece en caso que ingresen un valor incorrecto en el primer input
if (m<=100):
#100 es el tiempo maximo de uso en minutos sin un cobro de sobrecosto. 
    costo = m*7 
#La variable auxiliar costo es el valor total que debe pagar si el uso fue menor o igual a 100 minutos. 
elif (m>100 and m<=1440):
#Esta condicion es para el cobro del sobrecargo, si el tiempo es mayor a 100 minutos se cobra un sobrecargo de 50 por minuto, si el tiempo sobrepasa las 24 horas o los 1440 minutos, el sobrecargo es de 96mil pesos.
    costo = 700+((m-100)*57)    
#La variable auxiliar costo es el valor total que debe pagar si el uso fue mayor a 100 minutos y menor o igual a 1440 minutos. Los 700 pesos es el costo y lo que se le suma es el valor de sobrecosto.  
else: 
    costo = 700+((m-100)*7)+96000
#La variable auxiliar costo es el valor total que debe pagar si el uso fue mayor a 1440 minutos. Los 700 pesos es el costo y lo que se le suma es el valor de sobrecosto. 
print(costo)
#La variable auxiliar costo, tambien es un valor de salida y es el que se muestra en pantalla. 
  
    

        