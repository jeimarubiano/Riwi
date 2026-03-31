# =============================================================================
# M1S2 - Control de flujo y manejo de listas en el inventario
# Sistema de gestión de inventario con menú interactivo
# =============================================================================

# Lista global que almacena todos los productos como diccionarios
inventario = []


# -----------------------------------------------------------------------------
# TASK 1 & 2: Validación de datos y registro de productos
# -----------------------------------------------------------------------------
def agregar_producto():
    """
    Solicita al usuario los datos de un nuevo producto,
    valida las entradas y lo agrega al inventario como diccionario.
    """
    print("\n--- Agregar Producto ---")

    # Validar nombre (no puede estar vacío)
    nombre = input("Nombre del producto: ").strip()
    if not nombre:
        print("⚠ El nombre no puede estar vacío.")
        return

    # Validar precio (debe ser un número positivo)
    try:
        precio = float(input("Precio del producto: "))
        if precio < 0:
            print("⚠ El precio no puede ser negativo.")
            return
    except ValueError:
        print("⚠ El precio debe ser un número válido.")
        return

    # Validar cantidad (debe ser un entero positivo)
    try:
        cantidad = int(input("Cantidad en inventario: "))
        if cantidad < 0:
            print("⚠ La cantidad no puede ser negativa.")
            return
    except ValueError:
        print("⚠ La cantidad debe ser un número entero.")
        return

    # Crear diccionario del producto y agregarlo a la lista
    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)

    print(f"✔ Producto '{nombre}' agregado exitosamente.")


# -----------------------------------------------------------------------------
# TASK 3: Mostrar todos los productos del inventario
# -----------------------------------------------------------------------------
def mostrar_inventario():
    """
    Recorre la lista de inventario con un bucle for
    y muestra cada producto con formato claro.
    """
    print("\n--- Inventario Actual ---")

    # Verificar si el inventario está vacío
    if not inventario:
        print("El inventario está vacío. Agrega productos primero.")
        return

    # Recorrer e imprimir cada producto
    for i, producto in enumerate(inventario, start=1):
        print(
            f"{i}. Producto: {producto['nombre']} | "
            f"Precio: {producto['precio']:.2f} | "
            f"Cantidad: {producto['cantidad']}"
        )


# -----------------------------------------------------------------------------
# TASK 4: Calcular estadísticas básicas del inventario
# -----------------------------------------------------------------------------
def calcular_estadisticas():
    """
    Calcula y muestra:
    - El valor total del inventario (suma de precio × cantidad).
    - La cantidad total de productos registrados.
    """
    print("\n--- Estadísticas del Inventario ---")

    # Verificar si hay productos registrados
    if not inventario:
        print("No hay productos en el inventario para calcular estadísticas.")
        return

    # Calcular valor total usando bucle for
    valor_total = 0
    for producto in inventario:
        valor_total += producto["precio"] * producto["cantidad"]

    # Cantidad total de tipos de productos registrados
    total_productos = len(inventario)

    # Mostrar resultados
    print(f"📦 Total de productos registrados : {total_productos}")
    print(f"💰 Valor total del inventario     : {valor_total:.2f}")


# -----------------------------------------------------------------------------
# TASK 1 & 2: Menú principal envuelto en bucle while
# -----------------------------------------------------------------------------
def menu_principal():
    """
    Muestra el menú interactivo en un bucle while hasta que
    el usuario elija salir. Usa if/elif/else para procesar opciones.
    """
    print("=" * 45)
    print("   Bienvenido al Sistema de Inventario")
    print("=" * 45)

    # Bucle principal: continúa hasta que el usuario elija salir
    while True:
        # Mostrar opciones del menú
        print("\n¿Qué deseas hacer?")
        print("  1. Agregar producto")
        print("  2. Mostrar inventario")
        print("  3. Calcular estadísticas")
        print("  4. Salir")

        opcion = input("\nElige una opción (1-4): ").strip()

        # Procesar la opción con condicionales
        if opcion == "1":
            agregar_producto()

        elif opcion == "2":
            mostrar_inventario()

        elif opcion == "3":
            calcular_estadisticas()

        elif opcion == "4":
            # Salir del bucle y terminar el programa
            print("\n¡Hasta luego! Cerrando el sistema de inventario.")
            break

        else:
            # Opción inválida: mostrar error sin cerrar el programa
            print("⚠ Opción inválida. Por favor elige un número del 1 al 4.")


# -----------------------------------------------------------------------------
# Punto de entrada del programa
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    menu_principal()

# =============================================================================
# RESUMEN M1S2:
# Se aplicaron estructuras condicionales (if/elif/else) y bucles (while/for)
# para construir un sistema de inventario interactivo. Los productos se
# almacenan en una lista de diccionarios, se validan las entradas del usuario
# y se calculan estadísticas básicas. El código está modularizado en funciones
# documentadas y legibles.
# =============================================================================
