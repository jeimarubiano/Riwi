#DEV 2 (MOTOR)
import random
import inicio

# Obtener variables de inicio.py
day = 1
total_days = 10
oxygen = inicio.oxygen
batteries = inicio.batteries
spare_parts = inicio.spare_parts
multiplier = inicio.multiplier
difficulty = inicio.difficulty

# Probabilidad de evento negativo según dificultad elegida en DEV1
if difficulty == "1":
    event_percentage = 10
elif difficulty == "2":
    event_percentage = 20
elif difficulty == "3":
    event_percentage = 40
elif difficulty == "4":
    event_percentage = 70
else:
    event_percentage = 20

while day <= total_days and oxygen > 0 and batteries > 0 and spare_parts > 0:
    print("\n" + "="*45)
    print("DIA " + str(day) + " DE " + str(total_days) + " EN MARTE")
    print("ESTADO ACTUAL: O2: " + str(oxygen) + "% | Energia: " + str(batteries) + "% | Repuestos: " + str(spare_parts))
    print("="*45)

    # MENSAJE DE PROBABILIDAD
    print("Probabilidad de evento negativo hoy:", str(event_percentage) + "%")

    number = random.randint(1, 100)

    if number <= event_percentage:

        event = random.randint(1, 12)

        if event == 1:
            print("\nEVENTO: Tormenta de arena leve")
            batteries -= 10
            spare_parts -= 5
            print("Afectacion: Bateria -10, Repuestos -5")

        elif event == 2:
            print("\nEVENTO: Falla critica de oxigeno menor")
            oxygen -= 15
            print("Afectacion: Oxigeno -15")

        elif event == 3:
            print("\nEVENTO: Crisis psicologica inicial")
            batteries -= 10
            print("Afectacion: Bateria -10")

        elif event == 4:
            print("\nEVENTO: Impacto de micrometeorito")
            spare_parts -= 15
            oxygen -= 10
            print("Afectacion: Repuestos -15, Oxigeno -10")

        elif event == 5:
            print("\nEVENTO: Enfermedad marciana")
            oxygen -= 10
            batteries -= 15
            print("Afectacion: Oxigeno -10, Bateria -15")

        elif event == 6:
            print("\nEVENTO: Oleada solar moderada")
            batteries -= 20
            spare_parts -= 10
            print("Afectacion: Bateria -20, Repuestos -10")

        elif event == 7:
            print("\nEVENTO: Explosion en reactor secundario")
            batteries -= 20
            spare_parts -= 20
            oxygen -= 15
            print("Afectacion: Bateria -20, Repuestos -20, Oxigeno -15")

        elif event == 8:
            print("\nEVENTO: Fuga masiva de oxigeno")
            oxygen -= 25
            spare_parts -= 15
            print("Afectacion: Oxigeno -25, Repuestos -15")

        elif event == 9:
            print("\nEVENTO: Colapso del sistema solar")
            batteries -= 30
            spare_parts -= 15
            print("Afectacion: Bateria -30, Repuestos -15")

        elif event == 10:
            print("\nEVENTO: Impacto directo de meteorito grande")
            spare_parts -= 25
            oxygen -= 20
            batteries -= 15
            print("Afectacion: Repuestos -25, Oxigeno -20, Bateria -15")

        elif event == 11:
            print("\nEVENTO: Evento nulo")
            print("Afectacion: Ninguna")

        elif event == 12:
            print("\nEVENTO: Sistema recuperado")
            oxygen += 10
            batteries += 10
            print("Afectacion: Oxigeno +10, Bateria +10")

    else:
        print("\nEVENTO: Evento nulo")
        print("Afectacion: Ninguna")

    print(f"ESTADO ACTUAL: O2: {oxygen:.1f}% | Energía: {batteries:.1f}% | Repuestos: {spare_parts:.1f}")

    # LOGICA CONDICIONAL GRUPO 2: Priorizacion
    if oxygen < 20:
        print("AVISO: Oxigeno bajo el 20%. Luces e investigacion APAGADAS.")

    # CONSUMO DIARIO
    oxygen -= 5.0 * multiplier
    batteries -= 5.0 * multiplier

    # VALIDACION
    if oxygen <= 0 or batteries <= 0 or spare_parts <= 0:
        print("\nMISION ABORTADA: Se han agotado los recursos vitales.")
    else:
        day += 1
        input("\nPresiona Enter para terminar el dia...")

if day > total_days:
    print("\nMISION EXITOSA: Has sobrevivido los 10 dias en Marte.")