
# Esta es mi primera aplicación en python
print("Hola mundo")
print("Bienvenido a Python")
print("____________________")
print("Variables en Python")

#Tipos de datos en variables

nombre = "Daniela" # cadena
edad = 20  # númerico entero
correo = "09daniolvera@gmail.com" #cadena
promedio = 8.6 # númerico de punto flotante 
beca = False #Booleano

#Imprimir los datos

print("nombre :",nombre)
print("edad :",edad)
print("correo :",correo)
print("promedio :",promedio)
print("beca :",beca)


#Imprimir los datos

print("nombre :",nombre)
print("Tipo de dato de la variable Nombre : ",type(nombre))

print("edad :",edad)
print("Tipo de dato de la variable Edad : ",type(edad))

print("promedio :",promedio)
print("Tipo de dato de la variable Promedio : ",type(promedio))

print("beca :",beca)
print("Tipo de dato de la variable Beca : ",type(beca))

#Operaciones: +, -, *, /, % (Residuo), // (División entera), **(Exponente)
potencia2 = 2**10
residuo = 105 % 6

print(potencia2)
print(residuo)

# Condiciones if-else (operaciones ==, >, >=, !=)
edad= 12
if edad >= 18:
    print("Puede votar")
    print("Espero verte este 6 de junio")
else:
    print("No puede votar")
    print("Tan pronto tengas la edad, solicita tu INE")

# Listas en python
# Es un arreglo de elementos del cual la lista puede ser actualiza
alumnos = ["Valentin","Rosendo","Jeudiel","Lilia","Dani","Alan","Jonathan","Manzo",]
print(type(alumnos))

print(alumnos)

#Imprimir elementos individuales, con el iniciando desde 0
print(alumnos[0])
print(alumnos[3])
print(alumnos[4])
print(alumnos[5])
print("-------------------")


#Imprimir los elementos en un ciclo, recorrer la lista
for elemento in alumnos: 
    print(i,":",elemento)
    i=i+1

    for i in range (100,110,2):
        print(i)

# Hacer el juego del Gato en Python, usando una lista para almacenar las posiciones de los jugadores. 
# Versión 1: 2 jugadores
# Versión 2: Jugar vs maquina. 


print("Resultado esperado: ")
lista2 = ["Pantalla", "teclado", "bocinas", "mouse", "usb", "cd", "quemador", "impresora", "microfono", "webcam"]
equipo = ['mouse', 'cd', 'microfono', 'cargador']
for elemento in equipo:
    if elemento in lista2:
        indice = lista2.index(elemento)
        print("Indice", indice, ":", elemento)
    else:
        print(elemento, "No encontrado en lista2")