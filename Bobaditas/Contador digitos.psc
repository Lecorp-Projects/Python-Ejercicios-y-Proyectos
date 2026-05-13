Algoritmo noje 
	Escribir "Ingrese entero pa sacar sus digitos"
	Leer n
	c <- 0
	Mientras n>0 Hacer
		c <- c+1
		n <- trunc(n/10)
	FinMientras
	Escribir c
FinAlgoritmo
