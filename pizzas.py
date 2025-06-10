import os

catalogo_pizzas = []
pedidos_realizados = []

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    limpiar_pantalla()
    print("🍕 Sistema de Gestión de Pedidos de Pizzería 🍕")
    print("-" * 40)
    print("1. Registrar nueva pizza")
    print("2. Ver catálogo de pizzas")
    print("3. Realizar un pedido")
    print("4. Ver pedidos realizados")
    print("5. Salir del sistema")
    print("-" * 40)

def registrar_pizza():
    limpiar_pantalla()
    print("--- Registrar Nueva Pizza ---")
    codigo = input("Ingrese el código de la pizza: ").strip().upper()

    if any(pizza['codigo'] == codigo for pizza in catalogo_pizzas):
        print(f"Error: Ya existe una pizza con el código '{codigo}'.")
    else:
        nombre = input("Ingrese el nombre de la pizza: ").strip().title()
        tipo_masa = input("Ingrese el tipo de masa (ej. delgada, gruesa): ").strip().capitalize()

        while True:
            try:
                precio = float(input("Ingrese el precio unitario de la pizza: "))
                if precio <= 0:
                    print("El precio debe ser mayor que cero.")
                else:
                    break
            except ValueError:
                print("Entrada inválida. Ingrese un número.")

        while True:
            try:
                stock = int(input("Ingrese el stock disponible: "))
                if stock < 0:
                    print("El stock no puede ser negativo.")
                else:
                    break
            except ValueError:
                print("Entrada inválida. Ingrese un número entero.")

        catalogo_pizzas.append({
            'codigo': codigo,
            'nombre': nombre,
            'tipo_masa': tipo_masa,
            'precio_unitario': precio,
            'stock_disponible': stock
        })
        print(f"\nPizza '{nombre}' registrada exitosamente.")

    input("Presione Enter para continuar...")

def ver_catalogo():
    limpiar_pantalla()
    print("--- Catálogo de Pizzas ---")
    if not catalogo_pizzas:
        print("El catálogo está vacío.")
    else:
        for pizza in catalogo_pizzas:
            print(f"Código: {pizza['codigo']}")
            print(f"Nombre: {pizza['nombre']}")
            print(f"Tipo de Masa: {pizza['tipo_masa']}")
            print(f"Precio: ${pizza['precio_unitario']:.2f}")
            print(f"Stock: {pizza['stock_disponible']}")
            print("-" * 20)
    input("Presione Enter para continuar...")

def realizar_pedido():
    limpiar_pantalla()
    print("--- Realizar un Pedido ---")
    if not catalogo_pizzas:
        print("No hay pizzas disponibles en el catálogo.")
        input("Presione Enter para continuar...")
        return

    nombre_cliente = input("Ingrese el nombre del cliente: ").strip().title()

    print("\nCatálogo de Pizzas Disponibles:")
    for i, pizza in enumerate(catalogo_pizzas):
        print(f"{i+1}. {pizza['nombre']} (Código: {pizza['codigo']}) - ${pizza['precio_unitario']:.2f} - Stock: {pizza['stock_disponible']}")
    print("-" * 40)

    while True:
        try:
            opcion = int(input("Ingrese el número de la pizza deseada: "))
            if 1 <= opcion <= len(catalogo_pizzas):
                pizza = catalogo_pizzas[opcion - 1]
                break
            else:
                print("Opción inválida.")
        except ValueError:
            print("Entrada inválida. Ingrese un número.")

    if pizza['stock_disponible'] == 0:
        print(f"La pizza '{pizza['nombre']}' está agotada.")
        input("Presione Enter para continuar...")
        return

    while True:
        try:
            cantidad = int(input(f"Ingrese la cantidad de '{pizza['nombre']}' a pedir: "))
            if cantidad <= 0:
                print("La cantidad debe ser mayor que cero.")
            elif cantidad > pizza['stock_disponible']:
                print(f"Stock insuficiente. Disponible: {pizza['stock_disponible']}")
            else:
                break
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")

    total = pizza['precio_unitario'] * cantidad
    pizza['stock_disponible'] -= cantidad

    pedidos_realizados.append({
        'cliente': nombre_cliente,
        'pizza': pizza['nombre'],
        'cantidad': cantidad,
        'total_pagado': total
    })

    print(f"\nPedido registrado: '{pizza['nombre']}' x {cantidad} para {nombre_cliente}. Total: ${total:.2f}")
    input("Presione Enter para continuar...")

def ver_pedidos():
    limpiar_pantalla()
    print("--- Pedidos Realizados ---")
    if not pedidos_realizados:
        print("No hay pedidos realizados aún.")
    else:
        for i, pedido in enumerate(pedidos_realizados):
            print(f"Pedido #{i+1}")
            print(f"Cliente: {pedido['cliente']}")
            print(f"Pizza: {pedido['pizza']}")
            print(f"Cantidad: {pedido['cantidad']}")
            print(f"Total Pagado: ${pedido['total_pagado']:.2f}")
            print("-" * 20)
    input("Presione Enter para continuar...")

def ejecutar_sistema():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Ingrese su opción: "))
            if opcion == 1:
                registrar_pizza()
            elif opcion == 2:
                ver_catalogo()
            elif opcion == 3:
                realizar_pedido()
            elif opcion == 4:
                ver_pedidos()
            elif opcion == 5:
                limpiar_pantalla()
                print("¡Gracias por usar el sistema! 🍕 ¡Hasta pronto!")
                break
            else:
                print("Opción fuera de rango.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número del 1 al 5.")

ejecutar_sistema()
