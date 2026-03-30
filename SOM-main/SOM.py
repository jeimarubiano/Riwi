# ============================================
# SURVIVAL ON MARS - MAIN GAME LOOP
# ============================================

import inicio
import EventGenerator
import consumo
import Interfaz
import estado

# ============================================
# INICIALIZAR ESTADO DEL JUEGO
# ============================================

# Crear objeto de estado con las variables de inicio.py
game = estado.GameState(
    name=inicio.name,
    oxygen=inicio.oxygen,
    batteries=inicio.batteries,
    spare_parts=inicio.spare_parts,
    multiplier=inicio.multiplier,
    level=inicio.level,
    commander=inicio.commander,
    crew=inicio.crew
)

# ============================================
# CONFIGURACIÓN DEL JUEGO
# ============================================

# Mapear nivel a formato de EventGenerator
level_map = {
    "Fácil": "easy",
    "Normal": "medium",
    "Difícil": "hard",
    "Pesadilla": "nightmare"
}

event_level = level_map.get(game.level, "medium")

# ============================================
# BUCLE PRINCIPAL DEL JUEGO
# ============================================

print("\n🚀 La misión comienza ahora...\n")
input("Presiona Enter para comenzar el Día 1...")

while game.day <= game.total_days and game.mission_active:
    
    # Obtener día de la semana y multiplicador
    week_day = game.get_week_day()
    day_multiplier = game.get_day_multiplier()
    
    # Mostrar interfaz del día
    print("\n" + "="*50)
    print(f"  DÍA {game.day}/10 - {week_day}")
    print(f"  ESTACIÓN: {game.name}")
    print(f"  DIFICULTAD: {game.level}")
    print("="*50)
    print(f"  [O2] Oxígeno:   {game.oxygen:.1f}%")
    print(f"  [⚡] Energía:   {game.batteries:.1f}%")
    print(f"  [⚙] Repuestos: {game.spare_parts:.1f} unidades")
    print(f"  [👥] Tripulación: {game.crew} personas")
    print("="*50)
    
    # Mostrar multiplicador del día
    if day_multiplier == 1.2:
        print(f"  🔴 {week_day}: Consumo aumentado (x1.2)")
    elif day_multiplier == 0.8:
        print(f"  🟢 {week_day}: Consumo reducido (x0.8)")
    else:
        print(f"  🟡 {week_day}: Consumo normal (x1.0)")
    print("="*50)
    
    # Generar evento aleatorio del día
    print(f"\n📡 Analizando condiciones del Día {game.day}...")
    event, new_batteries, new_spare_parts, new_oxygen = EventGenerator.generate_event(
        event_level, 
        game.batteries, 
        game.spare_parts, 
        game.oxygen
    )
    
    # Actualizar recursos después del evento inicial
    game.update_resources(new_oxygen, new_batteries, new_spare_parts)
    
    # Mostrar evento
    if event == "No event":
        print("✅ EVENTO: Día tranquilo - Sin incidentes")
        print("   La tripulación puede descansar hoy.")
    else:
        print(f"\n⚠️ ¡EVENTO CRÍTICO DETECTADO!")
        print(f"   {event}")
        print("\n   Estado antes del evento:")
        print(f"   Oxígeno: {game.oxygen:.1f}% | Baterías: {game.batteries:.1f}% | Repuestos: {game.spare_parts:.1f}")
        
        # Solicitar decisión del jugador
        decision = EventGenerator.mostrar_opciones_evento(event)
        
        # Aplicar consecuencias de la decisión
        game.update_resources(
            game.oxygen + decision["oxygen"],
            game.batteries + decision["battery"],
            game.spare_parts + decision["spare_parts"]
        )
    
    # Mostrar estado después del evento
    print("\n--- ESTADO DESPUÉS DEL EVENTO ---")
    print(f"Oxígeno: {game.oxygen:.1f}%")
    print(f"Baterías: {game.batteries:.1f}%")
    print(f"Repuestos: {game.spare_parts:.1f} unidades")
    
    # Aplicar consumo diario base con multiplicador del día
    print("\n⏳ Consumiendo recursos del día...")
    total_multiplier = game.multiplier * day_multiplier
    consumed_oxygen, consumed_batteries, consumed_spare_parts = consumo.apply_base_consumption(
        game.oxygen, 
        game.batteries, 
        game.spare_parts, 
        total_multiplier
    )
    
    # Actualizar recursos después del consumo
    game.update_resources(consumed_oxygen, consumed_batteries, consumed_spare_parts)
    
    # Verificar alertas y estado crítico
    alerts = game.check_critical_resources()
    
    if alerts:
        print("\n" + "="*50)
        for alert in alerts:
            print(alert)
        print("="*50)
    
    # Si la misión falló, terminar
    if not game.mission_active:
        print("\n" + "="*50)
        print("💀 MISIÓN FALLIDA")
        print(f"La Estación {game.name} no pudo sobrevivir.")
        print(f"Días sobrevividos: {game.day}/{game.total_days}")
        print("="*50)
        break
    
    # Avanzar al siguiente día
    game.advance_day()
    
    if game.day <= game.total_days:
        input(f"\n▶️ Presiona Enter para continuar al Día {game.day}...")

# ============================================
# RESULTADO FINAL
# ============================================

if game.mission_completed():
    print("\n" + "="*50)
    print("🎉 ¡MISIÓN EXITOSA!")
    print(f"La Estación {game.name} ha sobrevivido los {game.total_days} días en Marte.")
    print("\nRECURSOS FINALES:")
    print(f"  Oxígeno: {game.oxygen:.1f}%")
    print(f"  Baterías: {game.batteries:.1f}%")
    print(f"  Repuestos: {game.spare_parts:.1f} unidades")
    print(f"  Tripulación: {game.crew} personas (todos sobrevivieron)")
    print(f"\nDificultad completada: {game.level}")
    print("="*50)
    print("\n🚀 ¡Felicidades, Comandante! La humanidad está orgullosa.")
    print("="*50)
