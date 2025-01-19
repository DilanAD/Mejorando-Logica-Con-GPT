while True:
    try:
        numero = int(input("Introduce un número entero positivo: "))
        if numero > 0:
            break
        else:
            print("Error: El número debe ser mayor que cero")
    except ValueError:
        print("Error: Debes ingresar un número entero")
        
print(numero)

def numero_Primo(num):
    lista = []
    for i in range(1, num +1):
        divi = num / i
        if divi.is_integer():
            lista.append(int(divi))
    if len(lista) == 2:
        print(f"el numeroo es primo y sus divisores son {lista}")
    else:
        print(f"el numero no es primo y sus divisores son: {lista}")
    

numero_Primo(numero)