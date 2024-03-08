"""
import random
palabras = ['mexico', 'casa', 'inteligencia', 'napoleon', 'amigos', 'impresionante', 'inmaduro', 'preciosa']

palabra = random.choice(palabras)
#print(palabra)
totalLetas = len(palabra)

respuesta = ['-' for _ in range (len(palabra)) ]  # aqui se van almacenar las letras ingresadas
salida = ' '.join(respuesta)
print(salida)

print('Adivina la palabra con ', totalLetas, ' letras')
"""


import random

# Lista de palabras para adivinar
palabras = ['mexico', 'casa', 'inteligencia', 'napoleon', 'amigos', 'impresionante', 'inmaduro', 'preciosa']

# Seleccionar una palabra aleatoria
palabra = random.choice(palabras)

# Crear una lista de guiones para representar las letras no adivinadas
respuesta = ['-' for _ in range(len(palabra))]

# Mostrar la palabra oculta al inicio
print(' '.join(respuesta))
print('Adivina la palabra con', len(palabra), 'letras')

# Contador de intentos
intentos = 0

# Bucle principal para el juego
while intentos < 3:
    # Pedir al usuario que ingrese una letra
    letra = input("Ingresa una letra: ").lower()  # Convertir la entrada a minúsculas para evitar errores
    
    # Verificar si la letra está en la palabra
    if letra in palabra:
        # Actualizar la lista de respuestas con la letra ingresada
        for i in range(len(palabra)):
            if palabra[i] == letra:
                respuesta[i] = letra
        # Mostrar la lista actualizada
        print(' '.join(respuesta))
        
        # Verificar si la palabra se ha adivinado completamente
        if ''.join(respuesta) == palabra:
            print("¡Felicidades! Has adivinado la palabra correctamente.")
            break  # Terminar el juego si se adivina la palabra
        
    else:
        # Incrementar el contador de intentos si la letra no está en la palabra
        intentos += 1
        print("Letra incorrecta. La letra '{}' no está en la palabra. Te quedan {} intentos.".format(letra, 3 - intentos))
        
# Verificar si se agotaron los intentos sin adivinar la palabra
if intentos == 3:
    print("Lo siento, has agotado tus intentos. La palabra era:", palabra)
