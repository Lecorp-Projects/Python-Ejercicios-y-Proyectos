# ============================================================
# Cálculo de cambios de aceite por kilometraje
# ============================================================
# Este programa calcula cuántos cambios de aceite ha necesitado
# un carro según la cantidad total de kilómetros recorridos.
#
# La regla usada es que el carro requiere un cambio de aceite cada
# 5678 kilómetros recorridos.
#
# Funcionalidades principales:
# - Solicitar el kilometraje total recorrido.
# - Usar división entera para calcular la cantidad de cambios.
# - Mostrar un mensaje diferente según si no hubo cambios, hubo
#   uno solo o hubo varios.
#
# Este ejercicio practica división entera, condicionales y salida
# de mensajes según el resultado obtenido.
# ============================================================

k = float(input("Ingrese el valor recorrido en kilometros como un valor positivo: "))
#La variable k es auxiliar y es un dato de entrada. 
c = k//5678
#c es una variable auxiliar que al hacer la division entera entre 5678 que es cada vez que se cambia el aceite, nos dice cuantos cambios tuvieron que hacerse. 
if (c==0):
#Si c es cero entonces se imprime en pantalla lo siguiente. 
    print("En su recorrido no tuvo que hacer cambio de aceite.")
elif(c==1):
#Si c es uno entonces se imprime en pantalla lo siguiente. 
    print ("En su recorrido tuvo que hacer cambio de aceite una vez.")
else: 
#Se imprime el valor de la variable c como dato de salida. 
    print("En su recorrido tuvo que hacer cambio de aceite " ,int(c), " veces.")

  