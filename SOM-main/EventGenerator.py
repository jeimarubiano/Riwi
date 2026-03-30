import random

# ============================================
# OPCIONES DE DECISIÓN PARA EVENTOS
# ============================================

decisiones_eventos = {
    # EVENTOS FÁCILES
    "Light sandstorm": {
        "opciones": [
            {"texto": "Apagar sistemas no esenciales", "battery": -5, "spare_parts": -2, "oxygen": -3},
            {"texto": "Mantener todo encendido", "battery": -10, "spare_parts": -5, "oxygen": -5},
            {"texto": "Activar escudos de emergencia", "battery": -3, "spare_parts": -8, "oxygen": -2}
        ]
    },
    "Minor oxygen system failure": {
        "opciones": [
            {"texto": "Reparación rápida", "battery": -5, "spare_parts": -10, "oxygen": -8},
            {"texto": "Reparación completa", "battery": -10, "spare_parts": -15, "oxygen": -5},
            {"texto": "Usar tanques de reserva", "battery": -3, "spare_parts": -5, "oxygen": -20}
        ]
    },
    "Initial psychological crisis": {
        "opciones": [
            {"texto": "Sesión de terapia grupal", "battery": -5, "spare_parts": -2, "oxygen": -3},
            {"texto": "Día de descanso", "battery": -10, "spare_parts": -3, "oxygen": -5},
            {"texto": "Continuar con las tareas", "battery": -15, "spare_parts": -5, "oxygen": -8}
        ]
    },
    "Micrometeorite impact": {
        "opciones": [
            {"texto": "Reparación de emergencia", "battery": -8, "spare_parts": -20, "oxygen": -5},
            {"texto": "Sellar sección dañada", "battery": -5, "spare_parts": -10, "oxygen": -15},
            {"texto": "Reparación temporal", "battery": -3, "spare_parts": -8, "oxygen": -12}
        ]
    },
    
    # EVENTOS MEDIOS
    "Martian illness": {
        "opciones": [
            {"texto": "Tratamiento médico intensivo", "battery": -10, "spare_parts": -5, "oxygen": -8},
            {"texto": "Cuarentena y reposo", "battery": -20, "spare_parts": 0, "oxygen": -15},
            {"texto": "Medicación básica", "battery": -8, "spare_parts": -3, "oxygen": -12}
        ]
    },
    "Moderate solar flare": {
        "opciones": [
            {"texto": "Apagar todos los sistemas", "battery": -15, "spare_parts": -5, "oxygen": -10},
            {"texto": "Proteger sistemas críticos", "battery": -20, "spare_parts": -10, "oxygen": -5},
            {"texto": "Mantener operaciones mínimas", "battery": -25, "spare_parts": -8, "oxygen": -8}
        ]
    },
    "Secondary reactor explosion": {
        "opciones": [
            {"texto": "Contener la explosión", "battery": -25, "spare_parts": -25, "oxygen": -10},
            {"texto": "Evacuar sección", "battery": -15, "spare_parts": -15, "oxygen": -20},
            {"texto": "Reparación de emergencia", "battery": -30, "spare_parts": -30, "oxygen": -15}
        ]
    },
    "Massive oxygen leak": {
        "opciones": [
            {"texto": "Sellar fuga inmediatamente", "battery": -10, "spare_parts": -20, "oxygen": -15},
            {"texto": "Usar reservas de oxígeno", "battery": -5, "spare_parts": -10, "oxygen": -30},
            {"texto": "Reparación completa", "battery": -15, "spare_parts": -25, "oxygen": -20}
        ]
    },
    
    # EVENTOS DIFÍCILES
    "Solar system collapse": {
        "opciones": [
            {"texto": "Reiniciar sistema completo", "battery": -35, "spare_parts": -20, "oxygen": -10},
            {"texto": "Cambiar a energía de respaldo", "battery": -25, "spare_parts": -25, "oxygen": -15},
            {"texto": "Reparación de emergencia", "battery": -40, "spare_parts": -15, "oxygen": -8}
        ]
    },
    "Direct large meteor impact": {
        "opciones": [
            {"texto": "Reparación estructural completa", "battery": -20, "spare_parts": -35, "oxygen": -15},
            {"texto": "Sellar y aislar área", "battery": -10, "spare_parts": -20, "oxygen": -25},
            {"texto": "Evacuación parcial", "battery": -15, "spare_parts": -15, "oxygen": -30}
        ]
    },
    "Total life support failure": {
        "opciones": [
            {"texto": "Activar sistema de respaldo", "battery": -25, "spare_parts": -15, "oxygen": -25},
            {"texto": "Reparación de emergencia", "battery": -30, "spare_parts": -20, "oxygen": -20},
            {"texto": "Usar trajes espaciales", "battery": -15, "spare_parts": -10, "oxygen": -35}
        ]
    },
    "Extreme solar storm": {
        "opciones": [
            {"texto": "Refugio subterráneo", "battery": -40, "spare_parts": -15, "oxygen": -12},
            {"texto": "Escudos electromagnéticos", "battery": -45, "spare_parts": -25, "oxygen": -10},
            {"texto": "Apagar toda la base", "battery": -30, "spare_parts": -20, "oxygen": -18}
        ]
    },
    
    # EVENTOS PESADILLA
    "Catastrophic system failure": {
        "opciones": [
            {"texto": "Reinicio total de sistemas", "battery": -45, "spare_parts": -35, "oxygen": -20},
            {"texto": "Modo supervivencia", "battery": -35, "spare_parts": -25, "oxygen": -30},
            {"texto": "Reparación desesperada", "battery": -50, "spare_parts": -40, "oxygen": -25}
        ]
    },
    "Massive meteor shower": {
        "opciones": [
            {"texto": "Refugio de emergencia", "battery": -30, "spare_parts": -30, "oxygen": -35},
            {"texto": "Escudos al máximo", "battery": -45, "spare_parts": -40, "oxygen": -25},
            {"texto": "Evacuación de emergencia", "battery": -25, "spare_parts": -35, "oxygen": -40}
        ]
    },
    "Total power grid collapse": {
        "opciones": [
            {"texto": "Generadores de emergencia", "battery": -55, "spare_parts": -30, "oxygen": -15},
            {"texto": "Energía manual", "battery": -40, "spare_parts": -20, "oxygen": -25},
            {"texto": "Reinicio del reactor", "battery": -60, "spare_parts": -35, "oxygen": -20}
        ]
    },
    "Critical life support breach": {
        "opciones": [
            {"texto": "Sellado de emergencia", "battery": -35, "spare_parts": -25, "oxygen": -35},
            {"texto": "Trajes espaciales completos", "battery": -25, "spare_parts": -15, "oxygen": -45},
            {"texto": "Reparación crítica", "battery": -40, "spare_parts": -30, "oxygen": -30}
        ]
    }
}


def mostrar_opciones_evento(evento_nombre):
    """Muestra las opciones disponibles para un evento y retorna la decisión del jugador"""
    
    if evento_nombre not in decisiones_eventos:
        # Si el evento no tiene decisiones, retornar valores por defecto
        return {"battery": 0, "spare_parts": 0, "oxygen": 0}
    
    opciones = decisiones_eventos[evento_nombre]["opciones"]
    
    print("\n" + "="*60)
    print("⚠️ ¡DECISIÓN CRÍTICA REQUERIDA!")
    print("="*60)
    print("\n¿Cómo deseas responder a este evento?\n")
    
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion['texto']}")
        print(f"   Impacto: Batería {opcion['battery']:+d}, Repuestos {opcion['spare_parts']:+d}, Oxígeno {opcion['oxygen']:+d}")
        print()
    
    # Solicitar decisión del jugador
    while True:
        try:
            eleccion = input(f"Elige tu decisión (1-{len(opciones)}): ").strip()
            eleccion_num = int(eleccion)
            
            if 1 <= eleccion_num <= len(opciones):
                decision = opciones[eleccion_num - 1]
                print(f"\n✓ Has elegido: {decision['texto']}")
                return decision
            else:
                print(f"⚠️ Por favor, elige un número entre 1 y {len(opciones)}")
        except ValueError:
            print("⚠️ Por favor, ingresa un número válido")


# ============================================
# EVENTOS Y GENERADOR
# ============================================

events = {

    "easy": {

        "negative": {

            "Light sandstorm": {
                "battery": -10,
                "spare_parts": -5,
                "oxygen": 0
            },

            "Minor oxygen system failure": {
                "battery": 0,
                "spare_parts": 0,
                "oxygen": -15
            },

            "Initial psychological crisis": {
                "battery": -10,
                "spare_parts": 0,
                "oxygen": 0
            },

            "Micrometeorite impact": {
                "battery": 0,
                "spare_parts": -15,
                "oxygen": -10
            }
        },

        "null": {

            "No event": {
                "battery": 0,
                "spare_parts": 0,
                "oxygen": 0
            }

        }

    },

    "medium": {

        "negative": {

            "Martian illness": {
                "battery": -15,
                "spare_parts": 0,
                "oxygen": -10
            },

            "Moderate solar flare": {
                "battery": -20,
                "spare_parts": -10,
                "oxygen": 0
            },

            "Secondary reactor explosion": {
                "battery": -20,
                "spare_parts": -20,
                "oxygen": -15
            },

            "Massive oxygen leak": {
                "battery": 0,
                "spare_parts": -15,
                "oxygen": -25
            }
        },

        "null": {

            "No event": {
                "battery": 0,
                "spare_parts": 0,
                "oxygen": 0
            }
        }
    },

    "hard": {

        "negative": {

            "Solar system collapse": {
                "battery": -30,
                "spare_parts": -15,
                "oxygen": 0
            },

            "Direct large meteor impact": {
                "battery": -15,
                "spare_parts": -25,
                "oxygen": -20
            },

            "Total life support failure": {
                "battery": -20,
                "spare_parts": 0,
                "oxygen": -30
            },

            "Extreme solar storm": {
                "battery": -35,
                "spare_parts": -20,
                "oxygen": 0
            }
        },

        "null": {

            "No event": {
                "battery": 0,
                "spare_parts": 0,
                "oxygen": 0
            }
        }
    },

    "nightmare": {

        "negative": {

            "Catastrophic system failure": {
                "battery": -40,
                "spare_parts": -30,
                "oxygen": -25
            },

            "Massive meteor shower": {
                "battery": -35,
                "spare_parts": -35,
                "oxygen": -30
            },

            "Total power grid collapse": {
                "battery": -50,
                "spare_parts": -25,
                "oxygen": -20
            },

            "Critical life support breach": {
                "battery": -30,
                "spare_parts": -20,
                "oxygen": -40
            }
        },

        "null": {

            "No event": {
                "battery": 0,
                "spare_parts": 0,
                "oxygen": 0
            }
        }
    }
}

import random

probabilities = {
    "easy": 0.10,      # 10% eventos críticos
    "medium": 0.20,    # 20% eventos críticos
    "hard": 0.40,      # 40% eventos críticos
    "nightmare": 0.70  # 70% eventos críticos
}

def generate_event(level, battery, spare_parts, oxygen):

    negative_probability = probabilities[level]

    number = random.random()

    if number <= negative_probability:
        event = random.choice(
            list(events[level]["negative"].keys())
        )
        data = events[level]["negative"][event]

    else:
        event = "No event"
        data = events[level]["null"][event]

    battery += data["battery"]
    spare_parts += data["spare_parts"]
    oxygen += data["oxygen"]

    battery = max(0, battery)
    spare_parts = max(0, spare_parts)
    oxygen = max(0, oxygen)

    return event, battery, spare_parts, oxygen


# TESTER

if __name__ == "__main__":

    level = input("Choose level (easy / medium / hard): ").lower()

    while level not in events:
        print("Invalid level.")
        level = input("Choose level (easy / medium / hard): ").lower()

    battery = 100
    spare_parts = 100
    oxygen = 100

    print("\n🚀 Mars survival begins...\n")

    for day in range(1, 11):  # 10 days

        print(f"--- Day {day} ---")

        event, battery, spare_parts, oxygen = generate_event(
            level,
            battery,
            spare_parts,
            oxygen
        )

        print("Event:", event)
        print("Battery:", battery)
        print("Spare parts:", spare_parts)
        print("Oxygen:", oxygen)
        print()

        # Lose condition
        if oxygen == 0:
            print("💀 You ran out of oxygen. Game over.")
            break

    else:
        print("🎉 You survived the 10 days!")