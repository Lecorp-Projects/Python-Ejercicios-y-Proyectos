# ============================================================
# Conteo de nombres según su letra final
# ============================================================
# Este programa solicita varios nombres y analiza la última letra
# de cada uno para determinar si termina en mayúscula o en minúscula.
#
# Funcionalidades principales:
# - Pedir al usuario la cantidad de nombres que desea ingresar.
# - Revisar la última letra de cada nombre.
# - Contar cuántos nombres terminan en letra mayúscula.
# - Contar cuántos nombres terminan en letra minúscula.
#
# El programa utiliza funciones para separar la verificación de la
# letra final y el conteo general de los nombres ingresados.
# ============================================================


def terminacion(palabra):
    ultima_letra = palabra[len(palabra) - 1]

    if ultima_letra == ultima_letra.lower():
        return True
    else:
        return False


def cuantosterminan(numero):
    terminan_minuscula = 0
    terminan_mayuscula = 0

    for i in range(numero):
        while True:
            nombre = input("Ingrese el nombre " + str(i + 1) + ": ").strip()

            if nombre == "":
                print("Ingrese un nombre valido.")
            elif not nombre[len(nombre) - 1].isalpha():
                print("El nombre debe terminar en una letra.")
            else:
                break

        if terminacion(nombre) == True:
            terminan_minuscula += 1
        else:
            terminan_mayuscula += 1

    return terminan_mayuscula, terminan_minuscula


print("Este programa cuenta cuántos nombres terminan en mayúscula y cuántos en minúscula.")

while True:
    try:
        n = int(input("Ingrese cuántos nombres va a registrar: "))

        if n > 0:
            break
        else:
            print("Ingrese un número mayor que 0.")

    except ValueError:
        print("Ingrese un número entero válido.")


mayusculas, minusculas = cuantosterminan(n)

print("\n--- RESULTADOS ---")
print("Nombres que terminan en mayúscula:", mayusculas)
print("Nombres que terminan en minúscula:", minusculas)
            
    


        
