import random 

def obtener_jugada_jugador():
    """
    Pide al jugador que seleccione su jugada (piedra, papel o tijeras) y la devuelve como una cadena.
    """
    jugada_jugador = ""
    while jugada_jugador not in ["piedra", "papel", "tijeras"]:
        jugada_jugador = input("Elige tu jugada (piedra, papel o tijeras): ").lower()
    return jugada_jugador

def obtener_jugada_computadora():
    """
    Genera una jugada aleatoria para la computadora y la devuelve como una cadena.
    """
    jugadas_posibles = ["piedra", "papel", "tijeras"]
    return random.choice(jugadas_posibles)


    
def determinar_ganador(jugada_jugador, jugada_computadora):
    """
    Determina quién gana entre el jugador y la computadora, dados sus jugadas.
    Devuelve "jugador" si el jugador gana, "computadora" si la computadora gana, o "empate" si hay un empate.
    """
    if jugada_jugador == jugada_computadora:
        return "empate"
    elif (jugada_jugador == "piedra" and jugada_computadora == "tijeras") or (jugada_jugador == "papel" and jugada_computadora == "piedra") or (jugada_jugador == "tijeras" and jugada_computadora == "papel"):
        return "jugador"
    else:
        return "computadora"

def jugar():
    """
    Lógica principal del juego. Obtiene la jugada del jugador, la jugada de la computadora, determina quién gana e imprime el resultado.
    """
    jugada_jugador = obtener_jugada_jugador()
    jugada_computadora = obtener_jugada_computadora()
    resultado = determinar_ganador(jugada_jugador, jugada_computadora)
    
    print(f"Jugador: {jugada_jugador}")
    print(f"Computadora: {jugada_computadora}")
    if resultado == "empate":
        print("Empate!")
    else:
        print(f"Gana {resultado}!")
        
jugar()  # Inicia el juego



