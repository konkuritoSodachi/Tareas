#!/usr/bin/env python3

#Simón David Del Pozo Núñez
#Paradigma 2018
#Tarea Adivina un número


'''
Escribir un programa en Python que realice lo siguiente:
- Solicitar al usuario un número que definirá el rango dentro del cual el
programa elegirá un número al azar.
- Solicitar al usuario un número que definirá la cantidad de oportunidades que
tiene el usuario para adivinar el número elegido por el programa.
- En base a los datos obtenidos, ejecutar un ciclo solicitando al usuario un
número, y finalizando cuando se agoten las oportunidades o el usuario adivine
el número.
Para obtener el número al azar, se recomienda usar el módulo random de la
biblioteca estándar de Python
'''

import random


titulo = " Adivina el número"
print(titulo, "\n", "-"*len(titulo), "\n")

maximo = intentos = 0
maximo = int(input("Elige el número limite del rango a adivinar: "))
intentos = int(input("Cantidad máxima de intentos: "))


repetir = "s"

while repetir == "s":

    secreto = random.randint(1, maximo)
    apuesta = 0
    intento = 0

    print("\nEstoy pensando en un número del 1 al {}.".format(maximo))
    print("Tienes", intentos, "oportunidades para adivinar, buena suerte.")


    while (secreto != apuesta) and (intento < intentos):

        apuesta = int(input("\n¿Cuál  es? "))
        intento += 1
        if secreto != apuesta:
            if secreto > apuesta:
                print("Es mayor.")
            else:
                print("Es menor.")
            print("Cantidad de intentos: ", intento)

    if intento <= intentos:
        print("\n¡Felicidades! Lo conseguiste en", intento, "intentos.")
    else:
        print("\nLo siento, perdiste.")

    repetir = input("\n¿Jugamos de nuevo? (S/N) ").lower()

print("Chau!")


