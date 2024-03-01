import random

# Función para imprimir el tablero
def imprimir_tablero(tablero):
    # Itera sobre cada fila del tablero
    for i, fila in enumerate(tablero):
        # Imprime los elementos de la fila separados por "|"
        print("|".join(fila))
        # Si no es la última fila, imprime una línea horizontal para separarlas
        if i < 2:
            print("-----")
    print("\n")

# Función para verificar si hay un ganador
def verificar_ganador(tablero, jugador):
    # Verificar filas
    for fila in tablero:
        if all([casilla == jugador for casilla in fila]):
            return True

    # Verificar columnas
    for i in range(3):
        if all([tablero[j][i] == jugador for j in range(3)]):
            return True

    # Verificar diagonales
    if all([tablero[i][i] == jugador for i in range(3)]) or all([tablero[i][2-i] == jugador for i in range(3)]):
        return True

    return False

# Función para la jugada de la máquina
def jugada_maquina(tablero):
    # Buscar una casilla vacía y realizar la jugada
    while True:
        fila = random.randint(0, 2)
        columna = random.randint(0, 2)
        if tablero[fila][columna] == " ":
            tablero[fila][columna] = "O"
            break

# Función principal del juego
def jugar_gato():
    while True:
        # Inicializar el tablero
        tablero = [[" " for _ in range(3)] for _ in range(3)]  # Crear un tablero vacío
        jugador = "X"  # El jugador "X" comienza primero

        # Ciclo principal del juego
        while True:
            imprimir_tablero(tablero)

            # Turno del jugador
            if jugador == "X":
                fila = int(input("Ingresa la fila (0, 1, 2): "))  # Obtener la fila del jugador
                columna = int(input("Ingresa la columna (0, 1, 2): "))  # Obtener la columna del jugador
                # Verificar si la casilla está vacía y realizar la jugada
                if tablero[fila][columna] == " ":
                    tablero[fila][columna] = jugador
                    # Verificar si el jugador ha ganado después de la jugada
                    if verificar_ganador(tablero, jugador):
                        imprimir_tablero(tablero)
                        print("¡Felicidades! ¡Has ganado!")
                        break
                    jugador = "O"  # Cambiar al siguiente jugador
                else:
                    print("Esa casilla ya está ocupada. Intenta de nuevo.")
            # Turno de la máquina
            else:
                print("Turno de la máquina:")
                jugada_maquina(tablero)  # Realizar la jugada de la máquina
                # Verificar si la máquina ha ganado después de la jugada
                if verificar_ganador(tablero, jugador):
                    imprimir_tablero(tablero)
                    print("¡La máquina ha ganado!")
                    break
                jugador = "X"  # Cambiar al siguiente jugador

            # Verificar si hay empate
            if all([casilla != " " for fila in tablero for casilla in fila]):
                imprimir_tablero(tablero)
                print("¡Empate!")
                break
        
        # Preguntar si el jugador quiere jugar nuevamente
        jugar_otra_vez = input("¿Quieres jugar nuevamente? (s/n): ")
        if jugar_otra_vez.lower() != "s":
            print("Gracias por jugar. ¡Hasta luego!")
            break

# Iniciar el juego
jugar_gato()
