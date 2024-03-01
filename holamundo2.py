# while
print("while")
print("Elementos de la lista2")
lista2 = ["Pantalla", "teclado", "bocinas", "mouse", "usb", "cd", "quemador", "impresora", "microfono", "webcam"]
print(lista2)

# Recorrer la lista2 con while
i = 0
while i < len(lista2):
    print(i, ":", lista2[i])
    i=i+1

# Acceder a los elementos de la lista2 por medio de índices. 
print("La lista2 tiene ", len(lista2), " elementos")
print("Todos los elementos 0-9 ", lista2[0:10])
print("Elementos del 2-6 ", lista2[2:7])
print("Elementos desde el 5 hasta el último ", lista2[5:])
print("Imprimir los primeros 3 elementos ", lista2[:3])

#1. Extraer 'mouse', 'usb', 'cd', 'quemador', 'impresora', con indices. 
print("Elementos del 3-7 ", lista2[3:8])

#2. Extraer 'mouse', 'usb', 'cd', 'quemador', 'impresora', 'microfono', 'webcam'
print("Elementos del 3-9 ", lista2[3:10])

#3. Extraer 'pantalla', 'teclado', 'bocinas', 'mouse', 'usb', 'cd', 'quemador', 'impresora'
print("Elementos del 0-7 ", lista2[0:8])

#4. Extraer 'pantalla', 'bocinas',  'usb', 'quemador', 'microfono'
print("Elementos del 0-2-4-6-8 ", lista2[::2])

# 5. Programar para extraer de la lista2, la sublista equipo = ['mouse', 'cd', 'microfono', 'cargador'], que aparezca su número de índice de cada una.
# Resultado esperado: 
# Indice 3 : mouse
# Indice 5 : cd
# Indice 8 : microfono
# Cargador No encontrado en lista2

print("Resultado esperado: ")
lista2 = ["Pantalla", "teclado", "bocinas", "mouse", "usb", "cd", "quemador", "impresora", "microfono", "webcam"]
equipo = ['mouse', 'cd', 'microfono', 'cargador']
for elemento in equipo:
    if elemento in lista2:  # Verifica si el elemento está presente en "lista2"
        indice = lista2.index(elemento)  # Si está presente, encuentra su índice en "lista2" y lo imprime junto con el elemento
        print("Indice", indice, ":", elemento)
    else: 
        print(elemento, "No encontrado en la lista2")
