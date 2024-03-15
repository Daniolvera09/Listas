#Elabora una lista con el código aeronáutico
#codigo = [['A','ALFA'], ['B','BRAVO'], ['C','CHARLIE'], .........]
#Ahora deberás leer un código desde el teclado , por ejemplo: Ingrese el código : BAZU
#Y la aplicación debe mostrar el código aeronáutico extendido, para el ejemplo debe mostrar: BRAVO ALFA ZULU UNIFORM
#Es importante el uso de las listas y subir al mismo repositorio de github de la entrega anterior. 
#Entregar el link del repositorio


# Definir el código aeronáutico
codigo = [['A', 'ALFA'], ['B', 'BRAVO'], ['C', 'CHARLIE'], ['D', 'DELTA'], ['E', 'ECHO'], ['F', 'FOXTROT'], ['G', 'GOLF'], ['H', 'HOTEL'], ['I', 'INDIA'], ['J', 'JULIETT'], ['K', 'KILO'], ['L', 'LIMA'], ['M', 'MIKE'], ['N', 'NOVEMBER'], ['O', 'OSCAR'], ['P', 'PAPA'], ['Q', 'QUEBEC'], ['R', 'ROMEO'], ['S', 'SIERRA'], ['T', 'TANGO'], ['U', 'UNIFORM'], ['V', 'VICTOR'], ['W', 'WHISKEY'], ['X', 'XRAY'], ['Y', 'YANKEE'], ['Z', 'ZULU']]

#Leer un código desde el teclado
codigo_teclado = input("Ingrese el código: ").upper()

#Buscar el código aeronáutico y agregar la palabra al resultado
resultado = []
for letra_usuario in codigo_teclado:
    for letra, palabra in codigo:
        if letra == letra_usuario:
            resultado.append(palabra)
            break
    else:
        resultado.append(letra_usuario)

# Mostrar el resultado al usuario
print(" ".join(resultado))
