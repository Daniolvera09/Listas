
"""
cadenaLarga = 

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi auctor finibus ligula accumsan facilisis. Cras purus tortor, iaculis eget lectus ac, aliquam facilisis mauris. Nam vel elementum tellus. Donec vehicula rhoncus viverra. Duis varius, lorem eget gravida semper, diam orci facilisis nibh, ac tincidunt dui lacus eget turpis. Vestibulum tristique, sapien eu iaculis facilisis, felis lacus dignissim lectus, a dictum felis libero a ipsum. Etiam molestie porta eros, ac scelerisque orci venenatis eget. Vivamus semper erat eu tincidunt viverra. Vivamus lacinia ultrices tellus, a egestas lectus mollis ac. Nam sit amet mauris quis velit vulputate lobortis sed vel leo.

Nullam ut sollicitudin arcu, eu pulvinar augue. Pellentesque maximus faucibus pharetra. Fusce sit amet blandit eros. Donec tristique at tellus id elementum. In imperdiet aliquet ultrices. Nam sit amet pretium velit. Praesent id maximus ante, sit amet tincidunt sem. Quisque massa libero, lacinia a diam et, egestas pulvinar neque. Curabitur interdum sagittis erat, et ornare urna suscipit quis. Nam et sem molestie felis vulputate ornare. Pellentesque tempus dignissim erat, vitae ornare diam commodo sed. Nulla dui ipsum, scelerisque et est nec, facilisis gravida nisl. Integer felis enim, ullamcorper ut tempor sit amet, pellentesque vitae sem.

Mauris varius faucibus quam, ac maximus odio blandit congue. Nam diam leo, ultricies et euismod ac, pharetra et nunc. Etiam non lectus sed elit efficitur vestibulum. Vestibulum mauris arcu, dapibus pretium arcu faucibus, fringilla porttitor lectus. Vivamus auctor, ipsum dapibus lobortis imperdiet, quam tellus aliquam arcu, eget molestie tellus felis id mi. Quisque convallis ut neque ac feugiat. Aliquam arcu tellus, aliquet nec porttitor quis, pharetra nec massa. Aenean quis fermentum justo. Praesent tristique, metus quis eleifend sollicitudin, diam tellus placerat est, eu condimentum lectus arcu non nibh.

Aenean sollicitudin pretium massa, gravida faucibus nunc lobortis vel. Nunc scelerisque congue dui. Morbi eleifend quis orci ac facilisis. Nam eget tincidunt massa. Donec nec augue non felis tempus hendrerit. Nunc maximus ultrices lectus eu vestibulum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis vitae tellus quis lectus gravida semper. Ut ultrices nisl ac sem auctor, vel mattis nisi interdum. Etiam et sapien massa. Vivamus suscipit, sem eu sagittis finibus, risus massa cursus ex, et faucibus lorem dolor ac velit. Nullam vitae finibus purus. Praesent mi turpis, dictum ultrices consectetur nec, venenatis vel dui. Fusce nisl dui, finibus quis sollicitudin vitae, congue pretium dolor. Integer sagittis ac ex vitae auctor. Nam iaculis facilisis felis vitae mattis.

Suspendisse potenti. Aliquam lobortis, nisl nec pretium laoreet, lectus tellus congue lorem, non euismod orci magna eu nulla. Aenean et facilisis orci, vitae elementum lacus. Vestibulum faucibus ligula et arcu porttitor sagittis. Sed vitae rhoncus mi, et ultricies lacus. Aliquam convallis molestie dui non rhoncus. Ut vel dictum lectus, at maximus justo. Fusce eget augue ut augue mattis mollis ac et erat.

"""

"""
print(cadenaLarga)
letras = ['abcdefghijklmnñopqrstuvwxyz']
caracteres = ['a', 'e', 'i', 'o', 'u', '', ',' '.']
Estadisticas = ['Total de caracteres:', 'Total de letras:','Total de vocales a :','Total de vocales e :','Total de vocales i :','Total de vocales o :','Total de vocales u :','Total de espacios :','Total de comas :', 'Total de puntos : ']
Totales = [0,0,0,0,0,0,0,0,0,0]

# Dada una cadena larga (Lorem ipsum de 5 párrafos)
# Presentar un resumen de las estadísticas de los párrafos
Total de caracteres:
Total de letras : 
Total de vocales a : 
Total de vocales e : 
Total de vocales i : 
Total de vocales o : 
Total de vocales u : 
Total de espacios : 
Total de comas : 
Total de puntos :

1. Crear lista cadenaLarga
2. Crear lista caracteres
3. Crear lista de estadisticas
4. Crear lista totales
5. Recorrer cadenaLarga
6. Ir acumulando los valores de totales según caracteres
7. Imprimir totales tomando los valores de las listas estadisticas y totales 
""" 

# Paso 1: Crear lista cadenaLarga
cadenaLarga = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi auctor finibus ligula accumsan facilisis. Cras purus tortor, iaculis eget lectus ac, aliquam facilisis mauris. Nam vel elementum tellus. Donec vehicula rhoncus viverra. Duis varius, lorem eget gravida semper, diam orci facilisis nibh, ac tincidunt dui lacus eget turpis. Vestibulum tristique, sapien eu iaculis facilisis, felis lacus dignissim lectus, a dictum felis libero a ipsum. Etiam molestie porta eros, ac scelerisque orci venenatis eget. Vivamus semper erat eu tincidunt viverra. Vivamus lacinia ultrices tellus, a egestas lectus mollis ac. Nam sit amet mauris quis velit vulputate lobortis sed vel leo.

Nullam ut sollicitudin arcu, eu pulvinar augue. Pellentesque maximus faucibus pharetra. Fusce sit amet blandit eros. Donec tristique at tellus id elementum. In imperdiet aliquet ultrices. Nam sit amet pretium velit. Praesent id maximus ante, sit amet tincidunt sem. Quisque massa libero, lacinia a diam et, egestas pulvinar neque. Curabitur interdum sagittis erat, et ornare urna suscipit quis. Nam et sem molestie felis vulputate ornare. Pellentesque tempus dignissim erat, vitae ornare diam commodo sed. Nulla dui ipsum, scelerisque et est nec, facilisis gravida nisl. Integer felis enim, ullamcorper ut tempor sit amet, pellentesque vitae sem.

Mauris varius faucibus quam, ac maximus odio blandit congue. Nam diam leo, ultricies et euismod ac, pharetra et nunc. Etiam non lectus sed elit efficitur vestibulum. Vestibulum mauris arcu, dapibus pretium arcu faucibus, fringilla porttitor lectus. Vivamus auctor, ipsum dapibus lobortis imperdiet, quam tellus aliquam arcu, eget molestie tellus felis id mi. Quisque convallis ut neque ac feugiat. Aliquam arcu tellus, aliquet nec porttitor quis, pharetra nec massa. Aenean quis fermentum justo. Praesent tristique, metus quis eleifend sollicitudin, diam tellus placerat est, eu condimentum lectus arcu non nibh.

Aenean sollicitudin pretium massa, gravida faucibus nunc lobortis vel. Nunc scelerisque congue dui. Morbi eleifend quis orci ac facilisis. Nam eget tincidunt massa. Donec nec augue non felis tempus hendrerit. Nunc maximus ultrices lectus eu vestibulum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis vitae tellus quis lectus gravida semper. Ut ultrices nisl ac sem auctor, vel mattis nisi interdum. Etiam et sapien massa. Vivamus suscipit, sem eu sagittis finibus, risus massa cursus ex, et faucibus lorem dolor ac velit. Nullam vitae finibus purus. Praesent mi turpis, dictum ultrices consectetur nec, venenatis vel dui. Fusce nisl dui, finibus quis sollicitudin vitae, congue pretium dolor. Integer sagittis ac ex vitae auctor. Nam iaculis facilisis felis vitae mattis.

Suspendisse potenti. Aliquam lobortis, nisl nec pretium laoreet, lectus tellus congue lorem, non euismod orci magna eu nulla. Aenean et facilisis orci, vitae elementum lacus. Vestibulum faucibus ligula et arcu porttitor sagittis. Sed vitae rhoncus mi, et ultricies lacus. Aliquam convallis molestie dui non rhoncus. Ut vel dictum lectus, at maximus justo. Fusce eget augue ut augue mattis mollis ac et erat.
"""
# Paso 2: Crear lista caracteres
letras = 'abcdefghijklmnñopqrstuvwxyz'
caracteres = ['a', 'e', 'i', 'o', 'u', ' ', ',', '.']

# Paso 3: Crear lista de estadísticas
estadisticas = ['Total de caracteres:', 'Total de letras:', 'Total de vocales a:', 'Total de vocales e:', 'Total de vocales i:', 'Total de vocales o:', 'Total de vocales u:', 'Total de espacios:', 'Total de comas:', 'Total de puntos:']

# Paso 4: Crear lista totales
totales = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Paso 5: Recorrer cadenaLarga
for caracter in cadenaLarga:
    # Paso 6: Ir acumulando los valores de totales según caracteres
    totales[0] += 1  # Total de caracteres
    if caracter.lower() in letras:  # Verificar si el caracter es una letra
        totales[1] += 1  # Total de letras
        if caracter.lower() == 'a': 
            totales[2] += 1
        elif caracter.lower() == 'e':
            totales[3] += 1
        elif caracter.lower() == 'i':
            totales[4] += 1
        elif caracter.lower() == 'o':
            totales[5] += 1
        elif caracter.lower() == 'u':
            totales[6] += 1
    elif caracter == ' ':
        totales[7] += 1
    elif caracter == ',':
        totales[8] += 1
    elif caracter == '.':
        totales[9] += 1
  

# Paso 7: Imprimir totales tomando los valores de las listas 'estadísticas' y 'totales'
print("Resumen de estadisticas:")
for i in range(len(estadisticas)):
    print(estadisticas[i], totales[i])

