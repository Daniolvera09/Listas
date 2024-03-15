cadenaLarga = """

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi auctor finibus ligula accumsan facilisis. Cras purus tortor, iaculis eget lectus ac, aliquam facilisis mauris. Nam vel elementum tellus. Donec vehicula rhoncus viverra. Duis varius, lorem eget gravida semper, diam orci facilisis nibh, ac tincidunt dui lacus eget turpis. Vestibulum tristique, sapien eu iaculis facilisis, felis lacus dignissim lectus, a dictum felis libero a ipsum. Etiam molestie porta eros, ac scelerisque orci venenatis eget. Vivamus semper erat eu tincidunt viverra. Vivamus lacinia ultrices tellus, a egestas lectus mollis ac. Nam sit amet mauris quis velit vulputate lobortis sed vel leo.

Nullam ut sollicitudin arcu, eu pulvinar augue. Pellentesque maximus faucibus pharetra. Fusce sit amet blandit eros. Donec tristique at tellus id elementum. In imperdiet aliquet ultrices. Nam sit amet pretium velit. Praesent id maximus ante, sit amet tincidunt sem. Quisque massa libero, lacinia a diam et, egestas pulvinar neque. Curabitur interdum sagittis erat, et ornare urna suscipit quis. Nam et sem molestie felis vulputate ornare. Pellentesque tempus dignissim erat, vitae ornare diam commodo sed. Nulla dui ipsum, scelerisque et est nec, facilisis gravida nisl. Integer felis enim, ullamcorper ut tempor sit amet, pellentesque vitae sem.

"""


print(cadenaLarga)
letras = ['abcdefghijklmnñopqrstuvwxyz']
caracteres = ['a', 'e', 'i', 'o', 'u', '', ',' '.', 'p']
estadisticas = ['Total de caracteres:', 'Total de letras:','Total de vocales a :','Total de vocales e :','Total de vocales i :','Total de vocales o :','Total de vocales u :','Total de espacios :','Total de comas :', 'Total de puntos : ']
totales = [0] * len(estadisticas)

#Contar el número de caracteres de la cadena larga.
totales[0] = len(cadenaLarga)
print(totales[0])
#Contar el número de caracteres de la cadena larga.
for i in cadenaLarga:
    if i.lower() in letras[0].lower(): 
        totales[1] += 1
    for j in range(2, len(estadisticas)):
            if i.lower() in caracteres[j-2]:
                totales[j] += 1

print("Estadisticas")
for i in range(len(estadisticas)):
    print(estadisticas[i], ' : ',totales[i])



