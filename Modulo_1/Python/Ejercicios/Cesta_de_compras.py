# Programa de menú interactivo para una cesta de la compra

# Creamos una lista vacía para guardar los productos que el usuario agregue
tienda_cesta = []

# Muestra el menú y pide al usuario una opción
def mostrar_menu():
    print('\n"Supermarket Deicel, C.A"')
    print("¿Que deseas hacer?")
    print("1. Agregar un nuevo elemento")
    print("2. Mostrar el contenido de la cesta de la compra")
    print("3. Eliminar un elemento")
    print("4. Calcular el precio total")
    print("5. Renunciar (salir)")
    opcion = input("Elige una opción (1-5): ")
    return opcion

# Agrega un nuevo producto a la cesta
def agregar_elemento():
    nombre = input("Introduce el nombre del producto: ")
    precio = float(input("Introduce el precio del producto: "))
    # Guardamos cada producto como un diccionario con nombre y precio
    tienda_cesta.append({'nombre': nombre, 'precio': precio})
    print(f"Producto '{nombre}' agregado a la cesta.")

# Muestra los productos que hay en la cesta
def mostrar_cesta():
    if not tienda_cesta:
        print("La cesta está vacía.")
    else:
        print("Contenido de la cesta:")
        for i, item in enumerate(tienda_cesta, 1):
            print(f"{i}. {item['nombre']} - ${item['precio']:.2f}")

# Elimina un producto de la cesta según el número que elija el usuario
def eliminar_elemento():
    mostrar_cesta()
    if tienda_cesta:
        indice = int(input("Introduce el número del producto a eliminar: "))
        if 1 <= indice <= len(tienda_cesta):
            eliminado = tienda_cesta.pop(indice - 1)
            print(f"Producto '{eliminado['nombre']}' eliminado de la cesta.")
        else:
            print("Índice no válido.")

# Calcula y muestra el total de los precios de los productos en la cesta
def calcular_total():
    total = sum(item['precio'] for item in tienda_cesta)
    print(f"El total de la cesta es: ${total:.2f}")

# Bucle principal: muestra el menú y ejecuta la opción seleccionada hasta que el usuario elija salir
while True:
    opcion = mostrar_menu()
    if opcion == '1':
        agregar_elemento()
    elif opcion == '2':
        mostrar_cesta()
    elif opcion == '3':
        eliminar_elemento()
    elif opcion == '4':
        calcular_total()
    elif opcion == '5':
        print('Gracias por comprar en "Supermarket Deicel, C.A".')
        break
    else:
        print("Opción no válida. Intenta de nuevo.")