import re

# Diccionarios para convertir números en texto
dic_0_9 = {0: "", 1: "uno", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco", 6: "seis", 7: "siete", 8: "ocho", 9: "nueve"}
dic_10_19 = {10: "diez", 11: "once", 12: "doce", 13: "trece", 14: "catorce", 15: "quince", 16: "dieciséis", 17: "diecisiete", 18: "dieciocho", 19: "diecinueve"}
dic_20_90 = {20: "veinte", 30: "treinta", 40: "cuarenta", 50: "cincuenta", 60: "sesenta", 70: "setenta", 80: "ochenta", 90: "noventa"}
dic_100_900 = {100: "cien", 200: "doscientos", 300: "trescientos", 400: "cuatrocientos", 500: "quinientos", 600: "seiscientos", 700: "setecientos", 800: "ochocientos", 900: "novecientos"}

def convertir_a_texto(num):
    if num == 0:
        return "cero"

    partes = []
    
    # Miles
    if num >= 1000:
        miles = num // 1000
        partes.append(f"{dic_0_9[miles]} mil")
        num %= 1000

    # Centenas
    if num >= 100:
        centenas = num // 100 * 100
        if num == 100:
            partes.append("cien")  # Caso especial
        else:
            partes.append(dic_100_900[centenas])
        num %= 100

    # Decenas
    if num >= 20:
        decenas = num // 10 * 10
        partes.append(dic_20_90[decenas])
        num %= 10
    elif 10 <= num <= 19:
        partes.append(dic_10_19[num])
        num = 0

    # Unidades
    if num > 0:
        partes.append(dic_0_9[num])

    return " ".join(partes).strip()

# Solicitar número al usuario
while True:
    try:
        numero = int(input("Introduce un número entero positivo de 1 a 9999: "))
        if 1 <= numero <= 9999:
            break
        else:
            print("Error: El número debe estar entre 1 y 9999.")
    except ValueError:
        print("Error: Debes ingresar un número entero.")

# Mostrar el resultado
print(f"{numero} en texto es: '{convertir_a_texto(numero)}'")
