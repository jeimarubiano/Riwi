# archivos.py
# Módulo para guardar y cargar el inventario en archivos CSV

import csv
import os


def guardar_csv(inventario, ruta, incluir_header=True):
    """
    Guarda el inventario en un archivo CSV.
    Parámetros: inventario (list), ruta (str), incluir_header (bool)
    Retorna: True si se guardó correctamente, False si hubo error.
    """
    # Verificar que el inventario no esté vacío
    if not inventario:
        print("  ⚠ El inventario está vacío. No hay nada que guardar.")
        return False

    try:
        with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)

            # Escribir encabezado si se solicita
            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])

            # Escribir cada producto
            for p in inventario:
                writer.writerow([p["nombre"], p["precio"], p["cantidad"]])

        print(f"  ✓ Inventario guardado en: {ruta}")
        return True

    except PermissionError:
        print(f"  ✗ Sin permisos para escribir en: {ruta}")
    except OSError as e:
        print(f"  ✗ Error al guardar el archivo: {e}")

    return False


def cargar_csv(ruta):
    """
    Carga productos desde un archivo CSV con validaciones por fila.
    Parámetros: ruta (str)
    Retorna: (list de productos válidos, int de filas inválidas)
    """
    productos = []
    filas_invalidas = 0

    try:
        with open(ruta, mode="r", newline="", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)

            # Leer y validar encabezado
            try:
                encabezado = next(reader)
            except StopIteration:
                print("  ✗ El archivo está vacío.")
                return [], 0

            # Normalizar encabezado (quitar espacios y pasar a minúsculas)
            encabezado_norm = [col.strip().lower() for col in encabezado]
            if encabezado_norm != ["nombre", "precio", "cantidad"]:
                print(f"  ✗ Encabezado inválido: {encabezado}")
                print("     Se esperaba: nombre,precio,cantidad")
                return [], 0

            # Leer cada fila y validar
            for num_fila, fila in enumerate(reader, start=2):

                # Validar que tenga exactamente 3 columnas
                if len(fila) != 3:
                    filas_invalidas += 1
                    continue

                nombre, precio_str, cantidad_str = fila

                # Validar que nombre no esté vacío
                nombre = nombre.strip()
                if not nombre:
                    filas_invalidas += 1
                    continue

                # Convertir y validar precio
                try:
                    precio = float(precio_str)
                    if precio < 0:
                        raise ValueError("precio negativo")
                except ValueError:
                    filas_invalidas += 1
                    continue

                # Convertir y validar cantidad
                try:
                    cantidad = int(cantidad_str)
                    if cantidad < 0:
                        raise ValueError("cantidad negativa")
                except ValueError:
                    filas_invalidas += 1
                    continue

                productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})

    except FileNotFoundError:
        print(f"  ✗ Archivo no encontrado: {ruta}")
        return [], 0
    except UnicodeDecodeError:
        print("  ✗ Error de codificación. Asegúrate de que el archivo sea UTF-8.")
        return [], 0
    except Exception as e:
        print(f"  ✗ Error inesperado al leer el archivo: {e}")
        return [], 0

    return productos, filas_invalidas


def fusionar_inventarios(inventario_actual, productos_nuevos):
    """
    Fusiona productos nuevos en el inventario actual.
    Política: si el nombre ya existe, suma la cantidad y actualiza el precio.
    Parámetros: inventario_actual (list), productos_nuevos (list)
    Retorna: None. Modifica inventario_actual en su lugar.
    """
    print("\n  Política de fusión: si el producto ya existe,")
    print("  se suma la cantidad y se actualiza el precio al nuevo valor.\n")

    for nuevo in productos_nuevos:
        # Buscar si ya existe en el inventario actual
        existente = None
        for p in inventario_actual:
            if p["nombre"].lower() == nuevo["nombre"].lower():
                existente = p
                break

        if existente:
            # Sumar cantidad y actualizar precio
            existente["cantidad"] += nuevo["cantidad"]
            existente["precio"] = nuevo["precio"]
        else:
            # Agregar como nuevo
            inventario_actual.append(nuevo)
