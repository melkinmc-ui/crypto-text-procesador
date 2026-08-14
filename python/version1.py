# -----------------------------------------------------------------
# 0. Guardar en un diccionario cada caracter individual
# y su caracter equivalente asociado (mapeo de sustitución).
# -----------------------------------------------------------------
diccionario_cifrado = {
    'a': '@', 'b': '8', 'c': '(', 'd': ']', 'e': '3',
    'f': '}', 'g': '9', 'h': '#', 'i': '!', 'j': '1',
    'k': '<', 'l': 'L', 'm': 'M', 'n': '^', 'o': '0',
    'p': '?', 'q': '9', 'r': '4', 's': '$', 't': '+',
    'u': 'v', 'v': 'V', 'w': 'w', 'x': '%', 'y': '&',
    'z': '2'
}

# -----------------------------------------------------------------
# 1. Mostrar mensaje de bienvenida
# -----------------------------------------------------------------
print("=== ¡BIENVENIDO AL CRIPTO-PROCESADOR DE TEXTO ===")
print("Este programa convertirá tu texto plano a un texto cifrado.\n")

# -----------------------------------------------------------------
# 2 y 3. Solicitar y guardar en una variable el mensaje digitado
# -----------------------------------------------------------------
texto_plano = input("Digite el texto plano a cifrar: ")

# -----------------------------------------------------------------
# 4. Guardar en una lista el texto dividido en caracteres individuales
# (Convertimos todo a minúsculas para coincidir con el diccionario)
# -----------------------------------------------------------------
caracteres_individuales = list(texto_plano.lower())

# Crear lista para almacenar los nuevos caracteres cifrados
caracteres_cifrados = []

# -----------------------------------------------------------------
# 5. Verificamos si el caracter individual existe en el diccionario
# -----------------------------------------------------------------
for caracter in caracteres_individuales:
    # 5.1 Si existe, sustituye por el equivalente y lo agrega a la nueva lista
    if caracter in diccionario_cifrado:
        caracteres_cifrados.append(diccionario_cifrado[caracter])
    else:
        # 5.2 Si no existe (espacios, números o símbolos), conserva el original
        caracteres_cifrados.append(caracter)

# -----------------------------------------------------------------
# 6. Guardamos en una variable la unión de cada caracter individual
# -----------------------------------------------------------------
texto_final = "".join(caracteres_cifrados)

# -----------------------------------------------------------------
# 7. Mostramos en pantalla el mensaje con el texto cifrado
# -----------------------------------------------------------------
print(f"\nEl texto encriptado es: {texto_final}")