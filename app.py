# app.py
# Archivo principal: menú de inventario con persistencia CSV
# Ejecutar con: python app.py

from servicios import (
    agregar_producto,
    mostrar_inventario,
    buscar_producto,
    actualizar_producto,
    eliminar_producto,
    calcular_estadisticas
)
from archivos import guardar_csv, cargar_csv, fusionar_inventarios


# ─── Helpers de entrada ────────────────────────────────────────────────────────

def pedir_float(mensaje):
    """Pide un número decimal positivo al usuario, repite hasta que sea válido."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("  ⚠ El valor no puede ser negativo.")
            else:
                return valor
        except ValueError:
            print("  ⚠ Ingresa un número válido (ej: 15.99).")


def pedir_int(mensaje):
    """Pide un número entero positivo al usuario, repite hasta que sea válido."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("  ⚠ La cantidad no puede ser negativa.")
            else:
                return valor
        except ValueError:
            print("  ⚠ Ingresa un número entero válido (ej: 10).")


def pedir_nombre(mensaje):
    """Pide un nombre no vacío."""
    while True:
        nombre = input(mensaje).strip()
        if nombre:
            return nombre
        print("  ⚠ El nombre no puede estar vacío.")


# ─── Opciones del menú ────────────────────────────────────────────────────────

def menu_agregar(inventario):
    print("\n── Agregar producto ──")
    nombre   = pedir_nombre("  Nombre   : ")
    precio   = pedir_float ("  Precio   : $")
    cantidad = pedir_int   ("  Cantidad : ")
    agregar_producto(inventario, nombre, precio, cantidad)


def menu_mostrar(inventario):
    print("\n── Inventario actual ──")
    mostrar_inventario(inventario)


def menu_buscar(inventario):
    print("\n── Buscar producto ──")
    nombre = pedir_nombre("  Nombre a buscar: ")
    producto = buscar_producto(inventario, nombre)
    if producto:
        print(f"\n  Encontrado → Nombre: {producto['nombre']}  "
              f"Precio: ${producto['precio']:.2f}  "
              f"Cantidad: {producto['cantidad']}")
    else:
        print(f"  ⚠ '{nombre}' no está en el inventario.")


def menu_actualizar(inventario):
    print("\n── Actualizar producto ──")
    nombre = pedir_nombre("  Nombre del producto: ")

    if not buscar_producto(inventario, nombre):
        print(f"  ⚠ '{nombre}' no encontrado.")
        return

    print("  Deja en blanco si no quieres cambiar ese campo.")

    # Precio (opcional)
    nuevo_precio = None
    entrada = input("  Nuevo precio (o Enter para omitir): $").strip()
    if entrada:
        try:
            nuevo_precio = float(entrada)
            if nuevo_precio < 0:
                print("  ⚠ Precio negativo ignorado.")
                nuevo_precio = None
        except ValueError:
            print("  ⚠ Precio inválido, se omite.")

    # Cantidad (opcional)
    nueva_cantidad = None
    entrada = input("  Nueva cantidad (o Enter para omitir): ").strip()
    if entrada:
        try:
            nueva_cantidad = int(entrada)
            if nueva_cantidad < 0:
                print("  ⚠ Cantidad negativa ignorada.")
                nueva_cantidad = None
        except ValueError:
            print("  ⚠ Cantidad inválida, se omite.")

    actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)


def menu_eliminar(inventario):
    print("\n── Eliminar producto ──")
    nombre = pedir_nombre("  Nombre del producto: ")
    confirmar = input(f"  ¿Seguro que quieres eliminar '{nombre}'? (S/N): ").strip().upper()
    if confirmar == "S":
        eliminar_producto(inventario, nombre)
    else:
        print("  Eliminación cancelada.")


def menu_estadisticas(inventario):
    print("\n── Estadísticas del inventario ──")
    stats = calcular_estadisticas(inventario)
    if not stats:
        print("  El inventario está vacío.")
        return

    print(f"  Unidades totales   : {stats['unidades_totales']}")
    print(f"  Valor total        : ${stats['valor_total']:.2f}")
    print(f"  Producto más caro  : {stats['producto_mas_caro']['nombre']} "
          f"(${stats['producto_mas_caro']['precio']:.2f})")
    print(f"  Mayor stock        : {stats['producto_mayor_stock']['nombre']} "
          f"({stats['producto_mayor_stock']['cantidad']} unidades)")


def menu_guardar(inventario):
    print("\n── Guardar CSV ──")
    ruta = input("  Ruta del archivo (ej: inventario.csv): ").strip()
    if not ruta:
        ruta = "inventario.csv"
    guardar_csv(inventario, ruta)


def menu_cargar(inventario):
    print("\n── Cargar CSV ──")
    ruta = input("  Ruta del archivo CSV: ").strip()
    if not ruta:
        print("  ⚠ Ruta vacía, operación cancelada.")
        return

    # Cargar y validar el archivo
    productos, filas_invalidas = cargar_csv(ruta)

    if not productos and filas_invalidas == 0:
        # Hubo un error crítico (archivo no encontrado, etc.)
        return

    print(f"\n  Productos válidos encontrados : {len(productos)}")
    print(f"  Filas inválidas omitidas      : {filas_invalidas}")

    if not productos:
        print("  No hay productos válidos para cargar.")
        return

    # Preguntar acción
    accion = input("\n  ¿Sobrescribir inventario actual? (S/N): ").strip().upper()

    if accion == "S":
        # Reemplazar inventario
        inventario.clear()
        inventario.extend(productos)
        print(f"\n  ✓ Inventario reemplazado con {len(productos)} producto(s).")
    else:
        # Fusionar
        fusionar_inventarios(inventario, productos)
        print(f"  ✓ Fusión completada. Inventario ahora tiene {len(inventario)} producto(s).")

    # Resumen final
    print(f"\n  ── Resumen de carga ──")
    print(f"  Acción            : {'Reemplazo' if accion == 'S' else 'Fusión'}")
    print(f"  Productos cargados: {len(productos)}")
    print(f"  Filas inválidas   : {filas_invalidas}")


# ─── Menú principal ───────────────────────────────────────────────────────────

def mostrar_menu():
    print("\n" + "═" * 40)
    print("       SISTEMA DE INVENTARIO")
    print("═" * 40)
    print("  1. Agregar producto")
    print("  2. Mostrar inventario")
    print("  3. Buscar producto")
    print("  4. Actualizar producto")
    print("  5. Eliminar producto")
    print("  6. Estadísticas")
    print("  7. Guardar CSV")
    print("  8. Cargar CSV")
    print("  9. Salir")
    print("═" * 40)


def main():
    # Inventario en memoria: lista de diccionarios
    inventario = []

    print("\n  Bienvenido al Sistema de Inventario")

    while True:
        mostrar_menu()

        opcion = input("  Selecciona una opción (1-9): ").strip()

        # Validar que sea un número del 1 al 9
        if not opcion.isdigit() or not (1 <= int(opcion) <= 9):
            print("  ⚠ Opción inválida. Ingresa un número del 1 al 9.")
            continue

        opcion = int(opcion)

        try:
            if   opcion == 1: menu_agregar(inventario)
            elif opcion == 2: menu_mostrar(inventario)
            elif opcion == 3: menu_buscar(inventario)
            elif opcion == 4: menu_actualizar(inventario)
            elif opcion == 5: menu_eliminar(inventario)
            elif opcion == 6: menu_estadisticas(inventario)
            elif opcion == 7: menu_guardar(inventario)
            elif opcion == 8: menu_cargar(inventario)
            elif opcion == 9:
                print("\n  ¡Hasta luego!\n")
                break

        except Exception as e:
            # Captura cualquier error inesperado sin cerrar el programa
            print(f"  ✗ Error inesperado: {e}. Volviendo al menú...")


if __name__ == "__main__":
    main()
