import random

day = 1
alive = True

oxygen = 100
battery = 100
spare_parts = 100

def check_death(oxygen, battery, spare_parts):
    """Verificar si algún recurso llegó a cero."""

    causes = [
        (oxygen, "💀 SIN OXÍGENO!", "La tripulación no puede respirar. Misión fallida."),
        (battery, "💀 SIN BATERÍA!", "La base perdió energía. Misión fallida."),
        (spare_parts, "💀 SIN REPUESTOS!", "Los sistemas críticos no pueden ser reparados. Misión fallida."),
    ]

    for resource, title, message in causes:
        if resource <= 0:
            print("\n" + "=" * 60)
            print(title)
            print(message)
            print("=" * 60)
            return False

    return True


while day <= 10 and alive:

    print(f"\nDÍA {day}")

    # Evento de ejemplo
    oxygen -= random.randint(5, 15)
    battery -= random.randint(5, 10)
    spare_parts -= random.randint(3, 8)

    print(f"Oxígeno: {oxygen}")
    print(f"Batería: {battery}")
    print(f"Repuestos: {spare_parts}")

    alive = check_death(oxygen, battery, spare_parts)

    day += 1
