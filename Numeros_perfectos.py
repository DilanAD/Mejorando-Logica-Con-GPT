def es_numero_Perfecto(num):
    lista = []
    divisores = [i for i in range(1, num // 2 +1) if num % i == 0] 
    suma_divisores = sum(divisores)
    
    # Mostrar los divisores y su suma
    print(f"Divisores propios de {num}: {divisores}")
    print(f"Suma de divisores: {suma_divisores}")
    return suma_divisores == num

# Solicitar un número entero positivo al usuario
while True:
    try:
        numero = int(input("Introduce un número entero positivo: "))
        if numero > 0:
            break
        else:
            print("Error: El número debe ser mayor que cero")
    except ValueError:
        print("Error: Debes ingresar un número entero")
        



# Evaluar si el número es perfecto  
if es_numero_Perfecto(numero):
    print(f"El número {numero} es perfecto")
else:
    print(f"El numero {numero} no es perfecto")


