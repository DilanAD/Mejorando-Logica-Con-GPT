import re
import unicodedata

def es_palindromo(frase):
    # Normalizar el texto: eliminar diacríticos, convertir a minúsculas y eliminar caracteres no alfanuméricos
    frase = unicodedata.normalize('NFD', frase)
    frase_limpia = re.sub(r'[^a-zA-Z0-9]', '', frase).lower()
    # Verificar si es un palíndromo
    return frase_limpia == frase_limpia[::-1]

while True:
    frase = input("Ingresa una frase para verificar si es un palíndromo: ")
    if frase.strip():
        break
    print("Error: Por favor, ingresa una frase no vacía.")

# Evaluar la frase y mostrar el resultado
if es_palindromo(frase):
    print(f"La frase '{frase}' es un palíndromo.")
else:
    print(f"La frase '{frase}' no es un palíndromo.")
