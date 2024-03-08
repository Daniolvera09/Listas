
import random 
numero = random.randint(0,11)
print(numero)

#Dada una lista de palabras(12)
palabras = ['Forrar', 'Rojo', 'Equipaje', 'Paleta', 'Mochila', 'Comida', 'Frutas', 'Uva', 'Celular', 'Rosa', 'Peluche', 'Casa', 'Fresa']

palabra = palabras [random.randint(0,11)]
print (palabra)

#Crear una lista que va a tener guiones el numero de letras que tenga la palabra. 
#respuesta = ['_', '_', '_', '_', '_']
palabra = "Tomate"
respuesta = ['_' for _ in palabra] 
print(respuesta)
print("-------------------------------------")

nombre = input("Escribe tu nombre: ")
print(nombre)
print(type(nombre))
edad = int (input ("Escribe tu edad: "))
print (edad)
print(type(edad))
estatura = float(input ("Cuanto mides: "))
print(estatura)
print(type(estatura))
