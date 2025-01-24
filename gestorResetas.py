import json

FILE_NAME = "recetas.json"


def cargar_recetas():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("archivo no encontrado")
        return []  


def guardar_recetas(recetas):
    with open(FILE_NAME, "w") as file:
        json.dump(recetas, file, indent=4)


def agregar_receta():
    nombre = input("Ingresa el nombre de la receta: ")
    ingredientes = input("Ingresa los ingredientes separados por comas: ").split(",")
    instrucciones = input("Ingrese las Instrucciones para preparar la receta: ")

    receta = {
        "nombre": nombre.strip(),
        "ingredientes": [ingrediente.strip() for ingrediente in ingredientes],
        "instrucciones": instrucciones.strip()
    }
    recetas.append(receta)
    guardar_recetas(recetas)
    print("Receta agregada con éxito!")


def listar_recetas():
    if not recetas:
        print("No hay recetas guardadas.")
        return
    print("\nRecetas guardadas:")
    for indice, receta in enumerate(recetas, start=1):
        print(f"{indice}. {receta['nombre']}")


def ver_receta():
    listar_recetas()
    try:
        indice = int(input("\nSelecciona el número de la receta para ver los detalles: ")) - 1
        receta = recetas[indice]
        print(f"\nNombre: {receta['nombre']}")
        print("Ingredientes:")
        for ingrediente in receta["ingredientes"]:
            print(f"  - {ingrediente}")
        print(f"instrucciones: {receta['instrucciones']}")
    except (IndexError, ValueError):
        print("Selección inválida.")


def modificar_receta():
    listar_recetas()
    try:
        indice = int(input("\nSelecciona el número de la receta a modificar: ")) - 1
        receta = recetas[indice]
        print(f"\nModificando receta: {receta['nombre']}")
        receta["nombre"] = input("Nuevo nombre: ").strip() or receta["nombre"]
        ingredientes = input("Nuevos ingredientes, separados por comas: ")
        if ingredientes:
            receta["ingredientes"] = [ingrediente.strip() for ingrediente in ingredientes.split(",")]
        receta["instrucciones"] = input("Nuevas instrucciones: ").strip() or receta["instrucciones"]
        guardar_recetas(recetas)
        print("Receta modificada con éxito!")
    except (IndexError, ValueError):
        print("Selección inválida.")


def eliminar_receta():
    listar_recetas()
    try:
        indice = int(input("\nSelecciona el número de la receta para eliminar: ")) - 1
        receta = recetas.pop(indice)
        guardar_recetas(recetas)
        print(f"Receta '{receta['nombre']}' eliminada con éxito!")
    except (IndexError, ValueError):
        print("Selección inválida.")


def menu():
    opciones = {
        "1": agregar_receta,
        "2": listar_recetas,
        "3": ver_receta,
        "4": modificar_receta,
        "5": eliminar_receta,
        "6": salir
    }
    while True:
        print("\n--- Aplicación de Recetas ---")
        print("1. Agregar receta")
        print("2. Listar recetas")
        print("3. Ver receta")
        print("4. Modificar receta")
        print("5. Eliminar receta")
        print("6. Salir")
        opcion = input("Selecciona una opción: ").strip()
        accion = opciones.get(opcion)
        if accion:
            accion()
        else:
            print("Opción no válida. Intenta de nuevo.")


def salir():
    print("¡Gracias por usar la aplicación de recetas!")
    exit()


recetas = cargar_recetas()

menu()
