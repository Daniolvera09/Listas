

"""
print(cadenaLarga)
caracteres = ['a', 'e', 'i', 'o', 'u', '', ',']

Dada una cadena larga (Lorem ipsum de 5 párrafos)
Presentar un resumen de las estadísticas de los párrafos
Total de caracteres:
Total de letras : 
Total de vocales a : 
Total de vocales e : 
Total de vocales i : 
Total de vocales o : 
Total de vocales u : 
Total de espacios : 
Total de comas : 
Total de palabras :
"""
# Definir la cadena de texto con los 5 párrafos
cadenaLarga = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi auctor finibus ligula accumsan facilisis. Cras purus tortor, iaculis eget lectus ac, aliquam facilisis mauris. Nam vel elementum tellus. Donec vehicula rhoncus viverra. Duis varius, lorem eget gravida semper, diam orci facilisis nibh, ac tincidunt dui lacus eget turpis. Vestibulum tristique, sapien eu iaculis facilisis, felis lacus dignissim lectus, a dictum felis libero a ipsum. Etiam molestie porta eros, ac scelerisque orci venenatis eget. Vivamus semper erat eu tincidunt viverra. Vivamus lacinia ultrices tellus, a egestas lectus mollis ac. Nam sit amet mauris quis velit vulputate lobortis sed vel leo.

Nullam ut sollicitudin arcu, eu pulvinar augue. Pellentesque maximus faucibus pharetra. Fusce sit amet blandit eros. Donec tristique at tellus id elementum. In imperdiet aliquet ultrices. Nam sit amet pretium velit. Praesent id maximus ante, sit amet tincidunt sem. Quisque massa libero, lacinia a diam et, egestas pulvinar neque. Curabitur interdum sagittis erat, et ornare urna suscipit quis. Nam et sem molestie felis vulputate ornare. Pellentesque tempus dignissim erat, vitae ornare diam commodo sed. Nulla dui ipsum, scelerisque et est nec, facilisis gravida nisl. Integer felis enim, ullamcorper ut tempor sit amet, pellentesque vitae sem.

Mauris varius faucibus quam, ac maximus odio blandit congue. Nam diam leo, ultricies et euismod ac, pharetra et nunc. Etiam non lectus sed elit efficitur vestibulum. Vestibulum mauris arcu, dapibus pretium arcu faucibus, fringilla porttitor lectus. Vivamus auctor, ipsum dapibus lobortis imperdiet, quam tellus aliquam arcu, eget molestie tellus felis id mi. Quisque convallis ut neque ac feugiat. Aliquam arcu tellus, aliquet nec porttitor quis, pharetra nec massa. Aenean quis fermentum justo. Praesent tristique, metus quis eleifend sollicitudin, diam tellus placerat est, eu condimentum lectus arcu non nibh.

Aenean sollicitudin pretium massa, gravida faucibus nunc lobortis vel. Nunc scelerisque congue dui. Morbi eleifend quis orci ac facilisis. Nam eget tincidunt massa. Donec nec augue non felis tempus hendrerit. Nunc maximus ultrices lectus eu vestibulum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis vitae tellus quis lectus gravida semper. Ut ultrices nisl ac sem auctor, vel mattis nisi interdum. Etiam et sapien massa. Vivamus suscipit, sem eu sagittis finibus, risus massa cursus ex, et faucibus lorem dolor ac velit. Nullam vitae finibus purus. Praesent mi turpis, dictum ultrices consectetur nec, venenatis vel dui. Fusce nisl dui, finibus quis sollicitudin vitae, congue pretium dolor. Integer sagittis ac ex vitae auctor. Nam iaculis facilisis felis vitae mattis.

Suspendisse potenti. Aliquam lobortis, nisl nec pretium laoreet, lectus tellus congue lorem, non euismod orci magna eu nulla. Aenean et facilisis orci, vitae elementum lacus. Vestibulum faucibus ligula et arcu porttitor sagittis. Sed vitae rhoncus mi, et ultricies lacus. Aliquam convallis molestie dui non rhoncus. Ut vel dictum lectus, at maximus justo. Fusce eget augue ut augue mattis mollis ac et erat.
"""

# Definir los caracteres a analizar
caracteres = ['a', 'e', 'i', 'o', 'u', ' ', ',']

# Inicializar contadores
total_caracteres = len(texto)  # Contador de caracteres en el texto
total_letras = sum(1 for char in texto if char.isalpha())  # Contador de letras en el texto
total_vocales = sum(1 for char in texto if char.lower() in 'aeiou')  # Contador de vocales en el texto
total_vocal_a = sum(1 for char in texto if char.lower() == 'a')  # Contador de la letra 'a'
total_vocal_e = sum(1 for char in texto if char.lower() == 'e')  # Contador de la letra 'e'
total_vocal_i = sum(1 for char in texto if char.lower() == 'i')  # Contador de la letra 'i'
total_vocal_o = sum(1 for char in texto if char.lower() == 'o')  # Contador de la letra 'o'
total_vocal_u = sum(1 for char in texto if char.lower() == 'u')  # Contador de la letra 'u'
total_espacios = sum(1 for char in texto if char == ' ')  # Contador de espacios en el texto
total_comas = sum(1 for char in texto if char == ',')  # Contador de comas en el texto

# Dividir el texto en palabras y contarlas
palabras = texto.split()  # Dividir el texto en una lista de palabras
total_palabras = len(palabras)  # Contar el número total de palabras en el texto


# Imprimir resumen de estadísticas
print("Total de caracteres:", total_caracteres)
print("Total de letras:", total_letras)
print("Total de vocales:", total_vocales)
print("Total de vocales a:", total_vocal_a)
print("Total de vocales e:", total_vocal_e)
print("Total de vocales i:", total_vocal_i)
print("Total de vocales o:", total_vocal_o)
print("Total de vocales u:", total_vocal_u)
print("Total de espacios:", total_espacios)
print("Total de comas:", total_comas)
print("Total de palabras:", total_palabras)
