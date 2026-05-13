#Hugo Esteban Barrero Garcia
#Grupo 4
#Haga un algoritmo para calcular el costo de un servicio de video streaming por demanda. El algoritmo recibira el momento en que inicio y termino la reproduccion de
#videos, mediante dos numeros enteros de maximo 6 digitos que representan las horas (00-23), los minutos (00-59) y los segundos (00-59). El costo del servicio es de $2
#pesos por segundo, con un cobro minimo de $1.000 pesos. Por ejemplo, si los tiempos de inicio y fin son 23754 y 130231, el costo del servicio sera de $74.954 pesos.
ti = int(input("Ingrese la hora que marcaba el reloj (sistema horario de 24 horas) al inicio del Stream, como un entero positivo de maximo 6 digitos: "))
#ti es una variable auxiliar de entrada que guarda el valor de la hora inicial del stream. 
hi = ti//10000
#hi es una variable auxiliar que guarda el valor en horas del tiempo de inicio del stream.
mi = (ti-(hi*10000))//100
#mi es una variable auxiliar que guarda el valor en minutos del tiempo de inicio del stream.
si = ti-((hi*10000)+(mi*100))
#si es una variable auxiliar que guarda el valor en segundos del tiempo de inicio del stream.
ti = (hi*3600)+(mi*60)+si
#ti es una variable auxiliar que cambia de valor y ahora es el tiempo de inicio del stream pasado a segundos. 
tf = int(input("Ingrese la hora que marcaba el reloj (sistema horario de 24 horas) al final del Stream, como un entero positivo de maximo 6 digitos: "))
#tf es una variable auxiliar de entrada que guarda el valor de la hora final del stream. 
hf = tf//10000
#hf es una variable auxiliar que guarda el valor en horas del tiempo de fin del stream.
mf = (tf-(hf*10000))//100
#mf es una variable auxiliar que guarda el valor en minutos del tiempo de fin del stream.
sf = tf-((hf*10000)+(mf*100))
#sf es una variable auxiliar que guarda el valor en segundos del tiempo de fin del stream.
tf = (hf*3600)+(mf*60)+sf
#tf es una variable auxiliar que cambia de valor y ahora es el tiempo de fin del stream pasado a segundos. 
t = tf-ti
#t es una variable auxiliar que tiene el valor de la duracion total del stream en segundos. 
costo = t*2
#costo es una variable auxiliar que contiene el valor que costo el uso del stream. 
#Las operaciones aca abajo con las variables h, hr, m, mr, s, se hacen solamente para saber el tiempo que dura el stream. 
h = t//3600
#La variable auxiliar h son las horas que dura el stream. 
hr = t%3600
#La variable auxiliar hr es para hallar los minutos que dura el stream. 
m = hr//60 
#La variable auxiliar h son los minutos que dura el stream. 
mr = hr%60
#La variable auxiliar mr es para hallar los segundos que dura el stream. 
s = mr 
#La variable auxiliar s son los segundos que dura el stream. 
#Se imprimen las variables auxiliares h, m, s y costo como datos de salida. 
if (costo >= 1000):
    print("El tiempo total que duro el stream fue de",h,"horas",m,"minutos y",s,"segundos.")
    print("Y el costo del stream fue de",costo,"pesos.")
else: 
    print("El tiempo total que duro el stream fue de",h,"horas",m,"minutos y",s,"segundos.")
    costo = 1000
    print("Y el costo del stream fue de",costo,"pesos.")
    






