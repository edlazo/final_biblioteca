import json

# Cargar o inicializar el inventario desde un archivo JSON
try:
    with open("inventario_libros.json", "r") as file:
        inventario = json.load(file)
except FileNotFoundError:
    # Libros disponibles en la biblioteca
    inventario = {
        "1234567890": {
            "titulo": "Cien años de soledad",
            "autor": "Gabriel García Márquez",
            "ubicacion": "Estantería A",
            "disponible": True,
            "reservas": []
        },
        "0987654321": {
            "titulo": "1984",
            "autor": "George Orwell",
            "ubicacion": "Estantería B",
            "disponible": True,
            "reservas": []
        },
        
    }

# Función para mostrar los libros disponibles
def mostrar_libros_disponibles():
    print("Libros disponibles:")
    print("------------------")
    for isbn, libro in inventario.items():
        if libro["disponible"]:
            print(f"ISBN: {isbn} - Título: {libro['titulo']} - Autor: {libro['autor']} - Ubicación: {libro['ubicacion']}")
    print("------------------")

# Función para mostrar los libros reservados
def mostrar_libros_reservados():
    print("Libros reservados:")
    print("-----------------")
    reservados = False
    for isbn, libro in inventario.items():
        if not libro["disponible"]:
            reservados = True
            print(f"ISBN: {isbn} - Título: {libro['titulo']} - Autor: {libro['autor']}")
            print("Reservas:")
            for reserva in libro["reservas"]:
                print(f"Nombre: {reserva['nombre']} - Correo: {reserva['correo']}")
            print("-----------------")
    if not reservados:
        print("No hay libros reservados.")
    print("-----------------")

# Función para reservar un libro
def reservar_libro(isbn, nombre, correo):
    if isbn in inventario and inventario[isbn]["disponible"]:
        inventario[isbn]["disponible"] = False
        inventario[isbn]["reservas"].append({"nombre": nombre, "correo": correo})
        with open("inventario_libros.json", "w") as file:
            json.dump(inventario, file)
        print(f"¡Has reservado el libro '{inventario[isbn]['titulo']}' con éxito!")
    else:
        print("El libro no está disponible para reserva.")

# Interfaz
while True:
    print("\nBienvenido a la Biblioteca")
    print("1. Ver libros disponibles")
    print("2. Ver libros reservados")
    print("3. Reservar un libro")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        mostrar_libros_disponibles()
    elif opcion == "2":
        mostrar_libros_reservados()
    elif opcion == "3":
        isbn = input("Ingresa el ISBN del libro que quieres reservar: ")
        nombre = input("Ingresa tu nombre: ")
        correo = input("Ingresa tu correo electrónico: ")
        reservar_libro(isbn, nombre, correo)
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elige una opción válida.")
