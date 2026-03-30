# servicios.py
# Módulo con funciones CRUD y estadísticas del inventario

def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Agrega un nuevo producto al inventario.
    Parámetros: inventario (list), nombre (str), precio (float), cantidad (int)
    Retorna: None. Modifica el inventario en su lugar.
    """
    # Verificar si el producto ya existe
    if buscar_producto(inventario, nombre):
        print(f"  ⚠ El producto '{nombre}' ya existe. Usa 'Actualizar' para modificarlo.")
        return

    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)
    print(f"  ✓ Producto '{nombre}' agregado correctamente.")


def mostrar_inventario(inventario):
    """
    Muestra todos los productos del inventario en formato tabla.
    Parámetros: inventario (list)
    Retorna: None
    """
    if not inventario:
        print("  El inventario está vacío.")
        return

    # Encabezado de la tabla
    print(f"\n  {'NOMBRE':<20} {'PRECIO':>10} {'CANTIDAD':>10} {'SUBTOTAL':>12}")
    print("  " + "-" * 55)

    # Calcular subtotal con lambda
    subtotal = lambda p: p["precio"] * p["cantidad"]

    for p in inventario:
        print(f"  {p['nombre']:<20} ${p['precio']:>9.2f} {p['cantidad']:>10} ${subtotal(p):>11.2f}")

    print("  " + "-" * 55)


def buscar_producto(inventario, nombre):
    """
    Busca un producto por nombre (sin distinguir mayúsculas).
    Parámetros: inventario (list), nombre (str)
    Retorna: dict del producto o None si no existe.
    """
    nombre_lower = nombre.strip().lower()
    for p in inventario:
        if p["nombre"].lower() == nombre_lower:
            return p
    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """
    Actualiza el precio y/o cantidad de un producto existente.
    Parámetros: inventario (list), nombre (str), nuevo_precio (float), nueva_cantidad (int)
    Retorna: True si se actualizó, False si no se encontró.
    """
    producto = buscar_producto(inventario, nombre)
    if not producto:
        print(f"  ⚠ Producto '{nombre}' no encontrado.")
        return False

    if nuevo_precio is not None:
        producto["precio"] = nuevo_precio
    if nueva_cantidad is not None:
        producto["cantidad"] = nueva_cantidad

    print(f"  ✓ Producto '{nombre}' actualizado.")
    return True


def eliminar_producto(inventario, nombre):
    """
    Elimina un producto del inventario por nombre.
    Parámetros: inventario (list), nombre (str)
    Retorna: True si se eliminó, False si no se encontró.
    """
    producto = buscar_producto(inventario, nombre)
    if not producto:
        print(f"  ⚠ Producto '{nombre}' no encontrado.")
        return False

    inventario.remove(producto)
    print(f"  ✓ Producto '{nombre}' eliminado.")
    return True


def calcular_estadisticas(inventario):
    """
    Calcula estadísticas generales del inventario.
    Parámetros: inventario (list)
    Retorna: dict con unidades_totales, valor_total, producto_mas_caro, producto_mayor_stock
    """
    if not inventario:
        return None

    subtotal = lambda p: p["precio"] * p["cantidad"]

    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(subtotal(p) for p in inventario)
    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": producto_mas_caro,
        "producto_mayor_stock": producto_mayor_stock
    }
