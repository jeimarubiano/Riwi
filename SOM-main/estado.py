# ============================================
# ESTADO DEL JUEGO - GESTIÓN DE RECURSOS
# ============================================

import random

class GameState:
    """Clase para gestionar el estado completo del juego"""
    
    def __init__(self, name, oxygen, batteries, spare_parts, multiplier, level, commander, crew):
        self.name = name
        self.oxygen = float(oxygen)
        self.batteries = float(batteries)
        self.spare_parts = float(spare_parts)
        self.multiplier = float(multiplier)
        self.level = level
        self.commander = float(commander)
        self.crew = crew
        self.day = 1
        self.total_days = 10
        self.mission_active = True
        
        # Días de la semana
        self.week_days = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        self.start_week_day = random.randint(0, 6)  # Día aleatorio de inicio
        
    def get_week_day(self):
        """Retorna el día de la semana actual"""
        index = (self.start_week_day + self.day - 1) % 7
        return self.week_days[index]
    
    def get_day_multiplier(self):
        """Retorna el multiplicador según el día de la semana"""
        current_day = self.get_week_day()
        
        if current_day in ["Sábado", "Domingo"]:
            return 1.2  # Fin de semana consume más
        elif current_day in ["Lunes", "Martes"]:
            return 0.8  # Inicio de semana consume menos
        else:
            return 1.0  # Días normales
    
    def update_resources(self, oxygen=None, batteries=None, spare_parts=None):
        """Actualiza los recursos del juego"""
        if oxygen is not None:
            self.oxygen = max(0.0, float(oxygen))
        if batteries is not None:
            self.batteries = max(0.0, float(batteries))
        if spare_parts is not None:
            self.spare_parts = max(0.0, float(spare_parts))
    
    def advance_day(self):
        """Avanza al siguiente día"""
        self.day += 1
    
    def check_critical_resources(self):
        """Verifica si algún recurso está en nivel crítico"""
        alerts = []
        
        if self.oxygen <= 0:
            alerts.append("💀 OXÍGENO AGOTADO - Misión fallida")
            self.mission_active = False
        elif self.oxygen < 20:
            alerts.append("🚨 OXÍGENO CRÍTICO (< 20%)")
        
        if self.batteries <= 0:
            alerts.append("💀 BATERÍAS AGOTADAS - Misión fallida")
            self.mission_active = False
        elif self.batteries < 20:
            alerts.append("🚨 BATERÍAS CRÍTICAS (< 20%)")
        
        if self.spare_parts <= 0:
            alerts.append("💀 REPUESTOS AGOTADOS - Misión fallida")
            self.mission_active = False
        elif self.spare_parts < 10:
            alerts.append("🚨 REPUESTOS ESCASOS (< 10)")
        
        return alerts
    
    def mission_completed(self):
        """Verifica si la misión fue completada exitosamente"""
        return self.day > self.total_days and self.mission_active
    
    def get_state(self):
        """Retorna un diccionario con el estado actual"""
        return {
            "name": self.name,
            "day": self.day,
            "total_days": self.total_days,
            "level": self.level,
            "oxygen": self.oxygen,
            "batteries": self.batteries,
            "spare_parts": self.spare_parts,
            "commander": self.commander,
            "crew": self.crew,
            "multiplier": self.multiplier,
            "mission_active": self.mission_active
        }
    
    def show_summary(self):
        """Muestra un resumen del estado actual"""
        print("\n" + "="*50)
        print(f"  ESTACIÓN: {self.name}")
        print(f"  DÍA: {self.day}/{self.total_days} ({self.get_week_day()})")
        print(f"  DIFICULTAD: {self.level}")
        print("="*50)
        print(f"  Oxígeno:   {self.oxygen:.1f}%")
        print(f"  Baterías:  {self.batteries:.1f}%")
        print(f"  Repuestos: {self.spare_parts:.1f} unidades")
        print(f"  Tripulación: {self.crew} personas")
        print(f"  Comandante: {self.commander:.1f}% salud")
        print("="*50)
