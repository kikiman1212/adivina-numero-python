# juego de adivinar el numero
import random


def juego_adivina():
    # generar un numero del 1 al 100
    numero = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("¡Bienvenido al juego de adivinanza de número!")
    print("Debes adivinar un número entre el 1 al 100")
    print("!Intenta adivinarlo")
    nombre = input("Ingresa tu nombre\n")

    while not adivinado:
        adivinanza = input("inserta un numero\n")

        if adivinanza.isdigit():
            adivinanza = int(adivinanza)
            intentos += 1

            if adivinanza < numero:
                print("Enumero es mayor al que insertaste")
                print(f"intentos:{intentos}")
            elif adivinanza > numero:
                print("el numero es menor al que insertaste")
                print(f"intentos:{intentos}")
            else:
                adivinanza == numero
                print(f"¡¡¡Adivinaste el Número: {numero} en {intentos} - Felicidades {nombre} 💥🎈✨🏆!!!")
                break


juego_adivina()
