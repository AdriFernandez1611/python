nombre1 = input("ingresa tu nombre, jugador 1: ")
nombre2  = input("ingresa tu nombre, jugador 2: ")

print ("¡Bienvenidos al juego de piedra, papel o tijera!")
print ("Introduce tu opcion a jugar en minusculas y singular")
jugador1 = input("Bien, " + nombre1 +". Escoge tu opcion a jugar: ")
jugador2 = input("ahora, " + nombre2 + ". Escoge tu opcion a jugar: ")

if (jugador1 != jugador2):
    #tijera Vs papel
    if (jugador1== "tijera") and (jugador2 == "papel"):
        print("¡El ganador es "+ nombre1 + "!")
    elif (jugador2== "tijera") and (jugador1 == "papel"):
        print("¡El ganador es "+ nombre2 + "!")
     #papel vs piedra
    elif (jugador1== "papel") and (jugador2 == "piedra"):
        print("¡El ganador es "+ nombre1 + "!")
    elif (jugador2== "papel") and (jugador1 == "piedra"):
        print("¡El ganador es "+ nombre2 + "!")
    #piedra vs tijera
    elif (jugador1== "piedra") and (jugador2 == "tijera"):
        print("¡El ganador es "+ nombre1 + "!")
    elif (jugador2== "piedra") and (jugador1 == "tijera"):
        print("¡El ganador es "+ nombre2 + "!")
    #detector de error
    else:
        print("Error al introducir datos. Por favor, reinicie el programa.")
else:
    print("Tenemos un empate")
