import random

# NOMBRE DEL SIMULADOR:
print("======================================")
print("         SURVIVAL ON MARS 🚀         ")
print("======================================")


# PEDIR NOMBRE AL JUGADOR
# input() LE PREGUNTA ALGO AL USUARIO Y GUARDO SU RESPUESTA EN LA VARIABLE "name".
name = input("Ingrese el nombre de la Estacion Espacial: ") #CAMBIO DE COMANDANTE A ESTACION ESPACIAL PARA MAYOR COHERENCIA CON EL SIMULADOR.
print("======================================")


# VALIDACION DE ENTRADA: SI EL USUARIO NO INGRESA NADA, SE LE PEDIRÁ QUE INGRESE UN NOMBRE VÁLIDO.
while name.strip() == "": # strip() ELIMINA ESPACIOS EN BLANCO. SI EL USUARIO SOLO PRESIONA ENTER, EL while LO OBLIGA A ESCRIBIR ALGO.
    print("⚠ El nombre no puede estar vacío.")
    name = input("Ingresa el nombre de la Estacion Espacial: ")
    print("======================================")


# SALUDO INICIAL
print("Bienvenido a la Estacion Espacial:", name) #CAMBIO DE COMANDANTE A ESTACION ESPACIAL PARA MAYOR COHERENCIA CON EL SIMULADOR.
print("======================================")


# NIVEL DE DIFICULTAD
print("Seleccione nivel de dificultad:")
print("\n1. Fácil     (recursos abundantes, 10% eventos críticos)") #AGREGE INFO SOBRE EL NIVEL FACIL.
print("2. Medio     (recursos estándar, 20% eventos críticos)") #AGREGE INFO SOBRE EL NIVEL MEDIO.
print("3. Difícil   (recursos al límite, 40% eventos críticos)") #AGREGE INFO SOBRE EL NIVEL DIFICIL.
print("4. Pesadilla (¡Solo para valientes!, 70% eventos críticos)") #AGREGADO EL NIVEL PESADILLA

difficulty = input("\nIngrese el número de la dificultad: ")
print("======================================")


#VALIDACION DE ENTRADA: SI EL USUARIO NO INGRESA NADA O INGRESA UNA OPCIÓN INVÁLIDA, SE LE PEDIRÁ QUE INGRESE UNA OPCIÓN VÁLIDA.
while difficulty.strip() == "" or difficulty not in ["1", "2", "3", "4"]:  # not in ["1", "2", "3", "4"]: SIGNIFICA: "SI LO QUE INGRESA NO ES 1, 2, 3 NI 4"
    print("⚠ Opción inválida. Escribe solo 1, 2, 3 o 4.")
    difficulty = input("\nIngrese el número de la dificultad: ")
    print("======================================")


# ASIGNAR RECURSOS INICIALES SEGÚN DIFICULTAD
if difficulty == "1": # FACIL
    oxygen = 100.0
    batteries = 100.0
    spare_parts = 50.0
    level = "Fácil"
    multiplier = 1.0 #MULTIPLICADOR DE CONSUMO DIARIO

elif difficulty == "2": # MEDIO
    oxygen = 80.0
    batteries = 80.0
    spare_parts = 40.0
    level = "Normal"
    multiplier = 1.3 #MULTIPLICADOR DE CONSUMO DIARIO

elif difficulty == "3": # DIFICIL
    oxygen = 60.0
    batteries = 60.0
    spare_parts = 30.0
    level = "Difícil"
    multiplier = 1.6 #MULTIPLICADOR DE CONSUMO DIARIO

elif difficulty == "4": # PESADILLA
    oxygen = 40.0
    batteries = 40.0
    spare_parts = 20.0
    level = "Pesadilla"
    multiplier = 2.0 #MULTIPLICADOR DE CONSUMO DIARIO


# MOSTRAR NIVEL ESCOGIDO Y RECURSOS INICIALES.
print("Has seleccionado la dificultad:", level)
print("======================================")
print("\nRecursos iniciales.")
print("Oxígeno:", oxygen)
print("Baterías:", batteries)
print("Repuestos:", spare_parts)


# SECCIÓN 5: COMANDANTE Y TRIPULACIÓN INICIAL.
# EL COMANDANTE EMPIEZA CON 100% DE SALUD SIN IMPORTAR LA DIFICULTAD.
# LA DIFICULTAD AFECTA RECURSOS INICIALES, NO LA SALUD INICIAL.
commander = 100.0   # FICTIZEN.
crew = random.randint(2, 6)  # TRIPULACIÓN ALEATORIA ENTRE 2 Y 6 PERSONAS


#SECCIÓN 6: RESUMEN VISUAL DE INICIO
levels = {1: "Fácil", 2: "Medio", 3: "Difícil", 4: "Pesadilla"} # DICCIONARIO QUE RELACIONA EL NÚMERO DE DIFICULTAD CON SU NOMBRE EN TEXTO.(PARA MOSTRSLO EN EL RESUMEN INICIAL)  
print()# LÍNEA EN BLANCO PARA DAR ESPACIO VISUAL ANTES DEL RESUMEN.
print("==============================================")  # LÍNEA DECORATIVA DE APERTURA.
print(f"  Bienvenido a Marte Nave {name}!")  # SALUDO PERSONALIZADO CON EL NOMBRE QUE INGRESÓ EL USUARIO.
print(f"  Nivel seleccionado : {levels[int(difficulty)]}")  # MUESTRA EL NOMBRE DE LA DIFICULTAD. int() CONVIERTE "1","2"... A NÚMERO PARA BUSCAR EN EL DICCIONARIO.
print("==============================================")  
print(f"  Oxígeno inicial    : {oxygen:.1f}%")  # MUESTRA EL OXÍGENO ASIGNADO SEGÚN LA DIFICULTAD.
print(f"  Baterías iniciales : {batteries:.1f}%")  # MUESTRA LAS BATERÍAS ASIGNADAS SEGÚN LA DIFICULTAD.
print(f"  Repuestos iniciales: {spare_parts:.1f} Unds")  # MUESTRA LOS REPUESTOS ASIGNADOS SEGÚN LA DIFICULTAD.
print(f"  Multiplicador      : x{multiplier:.1f}")  # MUESTRA EL MULTIPLICADOR DE CONSUMO. EL DEV 4 LO USARÁ PARA CALCULAR EL GASTO DIARIO.
print("----------------------------------------------")  # LÍNEA DECORATIVA QUE SEPARA RECURSOS DE TRIPULACIÓN.
print("  TRIPULACIÓN:")  # ENCABEZADO DE LA SECCIÓN DE TRIPULACIÓN.
print(f"  Comandante: FICTIZEN       | {commander:.1f}% salud")  # ESTADO INICIAL DEL COMANDANTE.
print(f"  Total tripulación: {crew} personas")  # MUESTRA LA TRIPULACIÓN ALEATORIA.
print("==============================================")

print()  # LÍNEA EN BLANCO PARA DAR ESPACIO VISUAL.
print("\nLa misión comienza. ¡Buena suerte!")  # MENSAJE FINAL QUE INDICA QUE EL JUEGO ESTÁ POR COMENZAR.
print()  # LÍNEA EN BLANCO FINAL ANTES DE QUE EL DEV 2 TOME EL CONTROL CON motor.py.