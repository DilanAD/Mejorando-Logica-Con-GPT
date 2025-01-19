while True:
    try:
        numero1 = int(input("Ingres el primer numero: "))
        numero2 = int(input("Ingres el segundo numero: "))
        break
    except ValueError:
        print("El dato ingresado no es valido, por favor intente nuevamente")
        print("------------------------------------------------------------")
        
def calculadora():
    
    print("1: Sumar")
    print("2: Restar")
    print("3: Multiplicar")
    print("4: Dividir")
        
    opcion = int(input("Introduce la operación que deseas realizar:"))

    match opcion:
        
        case 1:
            print(f"Reasultado de la suma: {numero1 +  numero2}")
        case 2:
            print(f"Resultado de la resta: {numero1 - numero2}")
        case 3:
            print(f"Resultado de la multiplicación: {numero1 * numero2}")
        case 4:
            try:
                print(f"Resultado de la división: {numero1 / numero2}")
            except ZeroDivisionError: 
                print("Error: División por cero no permitida.")
                
        case _:
            print("Opción inválida. Por favor, elige una opción entre 1 y 4.")
            
calculadora();
        
        



    
    