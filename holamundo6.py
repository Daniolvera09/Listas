#Alumna: Leydy Daniela Juarez Olvera


#TAREA 1
#Leer una cadena
#Imprimir la cadena
#Imprimir la cadena al revés
#Indicar si es una palabra palindroma

def es_palindromo(cadena):
    # Convertir la cadena a minúsculas y eliminar los espacios en blanco
    cadena = cadena.lower().replace(" ", "")
    # Comparar la cadena con su reverso
    if cadena == cadena[::-1]:
        return True
    else:
        return False

def main():
    # Leer una cadena
    cadena = input("Introduce una cadena: ")

    # Imprimir la cadena
    print("La cadena es:", cadena)

    # Imprimir la cadena al revés
    print("La cadena al revés es:", cadena[::-1])

    # Verificar si es un palíndromo
    if es_palindromo(cadena):
        print("La cadena es un palíndromo.")
    else:
        print("La cadena no es un palíndromo.")

if __name__ == "__main__":
    main()
print("-------------------------------------")


#TAREA 2
#Leer un número entre 1 al 20 
#Imprimir un triangulo de número con la cantidad de renglones que se respondan.

#versión 1:
#ejemplo: ingresa un numero: 6
"""
1
22
333
4444
55555
666666
"""

def imprimir_triangulo_v1(n):
    for i in range(1, n + 1):
        linea = [str(i)] * i
        print(linea)

try:
    num = int(input("Ingresa un número entre 1 y 20: "))
    if num < 1 or num > 20:
        print("Número fuera de rango.")
    else:
        imprimir_triangulo_v1(num)
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número válido.")

print("-------------------------------------")


#versión 2: 
#Ejemplo: ingresa un numero : 6
"""
100
94 94 
89 89 89
85 85 85 85
82 82 82 82 82
80 80 80 80 80 80
"""

def imprimir_triangulo(numero):
    valor = 100
    resta = numero
    for i in range(numero):
        fila = [valor] * (i + 1)
        print(" ".join(map(str, fila)))
        valor -= resta
        resta -= 1

numero = int(input("Ingresa un número para la resta del triángulo: "))
if numero >= 1:
    imprimir_triangulo(numero)
else:
    print("Número inválido.")

print("-------------------------------------")


