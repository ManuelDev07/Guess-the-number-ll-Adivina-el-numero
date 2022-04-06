"""

#Ejercicio Nro7 - Realizar un juego para adivinar un número. Para ello generar un numero aleatorio
entre 0-100, y luego ir pidiendo números indicando "es mayor" o "es menor" según sea mayor o menor 
con respecto a N. El proceso termina cuándo el usuario acierta y mostrar el número de intentos:

"""

#--------------------------------------------------------En este bloque se genera el numero aleatorio:-------------------------------------------------------
import random

aleatorio = random.randint(0, 100) #Aqui se indica con 'randint' que será un número entero y en paréntesis se especifica el rango de los numeros (inicio, final)

#------------------------------------------------------------------------------------------------------------------------------------------------------------

intentos = 0

while True:
    num = int(input("Ingrese un numero 👀: "))
    intentos += 1
    if num > aleatorio:
        print("Debe ser menor")
    elif num < aleatorio:
        print("Debe ser mayor")
    else:
        print("GANADOR!!!  :D")
        break

print(f"El numero de intentos fue: {intentos}") 
