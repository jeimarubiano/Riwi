# Calcular consumo base diario (con multiplicador de dificultad)
def calculate_base_consumption(multiplier):
    oxygen_consumption = int(5 * multiplier)
    battery_consumption = int(5 * multiplier)
    spare_parts_consumption = int(2 * multiplier)  # repuestos se consumen menos
    return oxygen_consumption, battery_consumption, spare_parts_consumption


# Aplicar consumo base a los recursos
def apply_base_consumption(oxygen, batteries, spare_parts, multiplier):

    oxygen_consumption, battery_consumption, spare_parts_consumption = calculate_base_consumption(multiplier)

    oxygen -= oxygen_consumption
    batteries -= battery_consumption
    spare_parts -= spare_parts_consumption

    print("\n--- CONSUMO DIARIO ---")
    print("Oxígeno consumido:", oxygen_consumption)
    print("Baterías consumidas:", battery_consumption)
    print("Repuestos consumidos:", spare_parts_consumption)

    return oxygen, batteries, spare_parts


# Mostrar estado actual de recursos
def show_status(oxygen, batteries, spare_parts):

    print("\n--- ESTADO ACTUAL ---")
    print("Oxígeno restante:", oxygen, "%")
    print("Baterías restantes:", batteries, "%")
    print("Repuestos restantes:", spare_parts, "Unidades")


# Verificar colapso del sistema
def check_collapse(oxygen, batteries, spare_parts):

    if oxygen <= 0:
        print("\n⚠ Oxígeno agotado. Misión abortada.")
        return True

    if batteries <= 0:
        print("\n⚠ Baterías agotadas. Misión abortada.")
        return True

    if spare_parts <= 0:
        print("\n⚠ Repuestos agotados. Misión abortada.")
        return True

    return False
