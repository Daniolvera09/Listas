def imprimir_tablero(tablero):
    # Función para imprimir el tablero actualizado.
    for fila in tablero:
        print("|".join(fila))  # Imprime cada fila del tablero separada por "|"
        print("-----") # Imprime una línea horizontal para separar las filas

def verificar_ganador(tablero, jugador):
 
    #Función para verificar si un jugador ha ganado.
    # Verificar filas
    for fila in tablero:
        if all(posicion == jugador for posicion in fila): # Comprueba si todas las posiciones en la fila son del mismo jugador
            return True
    # Verificar columnas
    for i in range(3):
        if all(tablero[j][i] == jugador for j in range(3)):  # Comprueba si todas las posiciones en la columna son del mismo jugador
            return True
    # Verificar diagonales
    if all(tablero[i][i] == jugador for i in range(3)) or all(tablero[i][2-i] == jugador for i in range(3)): # Comprueba las dos diagonales
        return True
    return False  # Retorna False si no hay ganador

def jugar_gato():

    # Función principal para jugar al gato.
    while True: # Bucle para jugar múltiples partidas
        tablero = [[" " for _ in range(3)] for _ in range(3)]  # Inicializar el tablero con espacios en vacios
        jugadores = ["X", "O"]  # Símbolos de los jugadores
        jugador_actual = 0  # Índice del jugador actual

        for _ in range(9):  # 9 turnos posibles
            imprimir_tablero(tablero)
            print(f"Turno del jugador {jugador_actual + 1} ({jugadores[jugador_actual]})")
            fila = int(input("Ingresa el número de fila (0, 1, 2): ")) # Pedir al jugador que ingrese la fila
            columna = int(input("Ingresa el número de columna (0, 1, 2): "))  # Pedir al jugador que ingrese la columna

            if tablero[fila][columna] != " ":  # Verificar si la posición está ocupada
                print("¡Esa posición ya está ocupada! ¡Pierdes tu turno!")
            else:
                tablero[fila][columna] = jugadores[jugador_actual] # Colocar el símbolo del jugador en la posición seleccionada
                if verificar_ganador(tablero, jugadores[jugador_actual]):  # Verificar si hay un ganador
                    imprimir_tablero(tablero)
                    print(f"¡El jugador {jugador_actual + 1} ({jugadores[jugador_actual]}) ha ganado!")
                    break # Salir del bucle si hay un ganador

                jugador_actual = (jugador_actual + 1) % 2  # Cambiar al siguiente jugador

        else:  # Si se completan los 9 turnos sin un ganador, es un empate
            imprimir_tablero(tablero)
            print("¡Empate!")

        jugar_nuevamente = input("¿Quieres jugar de nuevo? (s/n): ")
        if jugar_nuevamente.lower() != 's': # Si la respuesta no es 's' (sí), salir del bucle y terminar el juego
            print("Gracias por jugar. ¡Hasta luego!")
            break

if __name__ == "__main__":
    jugar_gato() # Iniciar el juego del gato
