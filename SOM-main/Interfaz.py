def start_interface():
    print("starting interface")
    
# ==========================================================
# DEV 6 - CONSOLE INTERFACE (File: interface.py)
# ==========================================================

# 1. DEFINICIÓN DE FUNCIÓN (Petición del supervisor)
def show_interface(day, name, level, oxygen, energy, spares):
    
    print("\n" + "===========================================")
    print(f"  DÍA {day}/10 | ESTACIÓN: {name}")
    print(f"  DIFICULTAD: {level}")
    print("===========================================")
    
    print("  RECURSOS:")
    print(f" [O2] Oxígeno:   {oxygen}%")
    print(f" [⚡] Energía:   {energy}%")
    print(f" [⚙] Repuestos: {spares} unidades")
    print("-------------------------------------------")

    # Alerta visual simple
    if oxygen < 20 or energy < 20:
        print(" ⚠️ ALERTA: Suministros en nivel crítico ⚠️")
    else:
        print(" ✓ Sistemas operando correctamente ✓ ")
    print("===========================================\n")
