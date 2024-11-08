import random

def determinar_ganador(jugador1, jugador2):
    if jugador1 == jugador2:
        return "Empate"
    elif (jugador1 == "tijera" and jugador2 == "papel") or \
         (jugador1 == "papel" and jugador2 == "piedra") or \
         (jugador1 == "piedra" and jugador2 == "tijera"):
        return jugador1
    else:
        return jugador2

nombre1 = input("Ingresa tu nombre, jugador 1: ")
nombre2 = "la computadora"
lista = ['piedra', 'papel', 'tijera']

while True:
    jugador1 = input(f"Bien, {nombre1}. Escoge tu opción a jugar (piedra, papel, tijera): ").lower()
    jugador2 = random.choice(lista)

    if jugador1 not in lista:
        print("Opción inválida. Por favor, elige entre piedra, papel o tijera.")
        continue

    ganador = determinar_ganador(jugador1, jugador2)
    print(f"{nombre1} eligió: {jugador1}")
    print(f"{nombre2} eligió: {jugador2}")

    if ganador == "Empate":
        print("¡Empate!")
    else:
        print(f"¡El ganador es {ganador}!")

    jugar_de_nuevo = input("¿Quieres jugar otra ronda? (si/no): ").lower()
    if jugar_de_nuevo != "si":
        break
# Usa el código con precaución.

# Explicación de los cambios:

# Función determinar_ganador: Esta función simplifica la lógica para determinar el ganador.
# Conversión a minúsculas: Se utiliza lower() para convertir las opciones a minúsculas.
# Mensajes más detallados: Se muestran las opciones de ambos jugadores y se indica claramente el ganador.
# Bucle while: Permite jugar múltiples rondas.
# Validación de entrada: Se verifica si la opción del jugador es válida.
# Este código mejorado ofrece una experiencia de juego más completa y profesional. Puedes personalizarlo aún más agregando características como un sistema de puntuación, diferentes niveles de dificultad o opciones para jugar contra otro jugador.