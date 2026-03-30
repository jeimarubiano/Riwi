"""
================================================================================
                    GUÍA COMPLETA DE DICCIONARIOS EN PYTHON
================================================================================

Este archivo contiene TODO lo que necesitas saber sobre diccionarios en Python,
desde lo más básico hasta estructuras complejas anidadas.

Autor: Guía educativa completa
Fecha: 2026
================================================================================
"""

# ==============================================================================
# 1. ¿QUÉ ES UN DICCIONARIO?
# ==============================================================================

"""
Un diccionario es una estructura de datos que almacena pares de CLAVE-VALOR.
- Es MUTABLE (se puede modificar después de crearlo)
- Es DESORDENADO (aunque desde Python 3.7+ mantiene el orden de inserción)
- Las CLAVES deben ser únicas e inmutables (strings, números, tuplas)
- Los VALORES pueden ser de cualquier tipo (números, strings, listas, otros diccionarios, etc.)

Sintaxis básica: {clave: valor, clave2: valor2}
"""

# ==============================================================================
# 2. CREACIÓN DE DICCIONARIOS
# ==============================================================================

# Diccionario vacío
diccionario_vacio = {}
otro_vacio = dict()

# Diccionario simple con diferentes tipos de datos
persona = {
    "nombre": "Juan",
    "edad": 25,
    "altura": 1.75,
    "es_estudiante": True
}

# Diccionario con claves numéricas
codigos = {
    1: "Producto A",
    2: "Producto B",
    3: "Producto C"
}

# Diccionario con tuplas como claves (las tuplas son inmutables)
coordenadas = {
    (0, 0): "Origen",
    (1, 2): "Punto A",
    (3, 4): "Punto B"
}

print("=" * 80)
print("DICCIONARIOS BÁSICOS")
3
print("=" * 80)
print(f"Persona: {persona}")
print(f"Nombre: {persona['nombre']}, Edad: {persona['edad']}")
print()

# ==============================================================================
# 3. ACCESO A VALORES
# ==============================================================================

# Forma 1: Usando corchetes [] - Da error si la clave no existe
nombre = persona["nombre"]
print(f"Acceso con []: {nombre}")

# Forma 2: Usando .get() - Retorna None si la clave no existe (más seguro)
apellido = persona.get("apellido")  # Retorna None
print(f"Acceso con .get() (clave inexistente): {apellido}")

# .get() con valor por defecto
apellido = persona.get("apellido", "Sin apellido")
print(f"Acceso con .get() y valor por defecto: {apellido}")
print()

# ==============================================================================
# 4. MODIFICACIÓN Y ADICIÓN DE ELEMENTOS
# ==============================================================================

# Agregar un nuevo par clave-valor
persona["apellido"] = "Pérez"
print(f"Después de agregar apellido: {persona}")

# Modificar un valor existente
persona["edad"] = 26
print(f"Después de modificar edad: {persona}")

# Agregar múltiples elementos con .update()
persona.update({"ciudad": "Madrid", "profesion": "Ingeniero"})
print(f"Después de .update(): {persona}")
print()

# ==============================================================================
# 5. ELIMINACIÓN DE ELEMENTOS
# ==============================================================================

# Crear un diccionario de prueba
prueba = {"a": 1, "b": 2, "c": 3, "d": 4}

# Forma 1: del - Elimina una clave específica
del prueba["a"]
print(f"Después de del: {prueba}")

# Forma 2: .pop() - Elimina y retorna el valor
valor_eliminado = prueba.pop("b")
print(f"Valor eliminado con .pop(): {valor_eliminado}")
print(f"Diccionario después de .pop(): {prueba}")

# Forma 3: .popitem() - Elimina y retorna el último par clave-valor
ultimo = prueba.popitem()
print(f"Último elemento eliminado: {ultimo}")
print(f"Diccionario después de .popitem(): {prueba}")

# Forma 4: .clear() - Vacía todo el diccionario
prueba.clear()
print(f"Después de .clear(): {prueba}")
print()

# ==============================================================================
# 6. MÉTODOS IMPORTANTES DE DICCIONARIOS
# ==============================================================================

estudiante = {
    "nombre": "Ana",
    "edad": 22,
    "carrera": "Informática",
    "semestre": 5
}

print("=" * 80)
print("MÉTODOS DE DICCIONARIOS")
print("=" * 80)

# .keys() - Obtiene todas las claves
claves = estudiante.keys()
print(f"Claves: {list(claves)}")

# .values() - Obtiene todos los valores
valores = estudiante.values()
print(f"Valores: {list(valores)}")

# .items() - Obtiene pares (clave, valor) como tuplas
items = estudiante.items()
print(f"Items: {list(items)}")

# Iterar sobre un diccionario
print("\nIterando sobre claves:")
for clave in estudiante:
    print(f"  {clave}: {estudiante[clave]}")

print("\nIterando sobre items (forma recomendada):")
for clave, valor in estudiante.items():
    print(f"  {clave} = {valor}")

# Verificar si una clave existe
if "nombre" in estudiante:
    print(f"\nLa clave 'nombre' existe: {estudiante['nombre']}")

if "apellido" not in estudiante:
    print("La clave 'apellido' NO existe")
print()

# ==============================================================================
# 7. DICCIONARIOS ANIDADOS (DICCIONARIO DENTRO DE DICCIONARIO)
# ==============================================================================

print("=" * 80)
print("DICCIONARIOS ANIDADOS - NIVEL 1")
print("=" * 80)

"""
Los diccionarios pueden contener otros diccionarios como valores.
Esto es útil para representar estructuras de datos complejas.
"""

# Ejemplo: Base de datos de empleados
empresa = {
    "empleado_001": {
        "nombre": "Carlos López",
        "edad": 30,
        "puesto": "Desarrollador",
        "salario": 45000
    },
    "empleado_002": {
        "nombre": "María García",
        "edad": 28,
        "puesto": "Diseñadora",
        "salario": 42000
    },
    "empleado_003": {
        "nombre": "Pedro Martínez",
        "edad": 35,
        "puesto": "Gerente",
        "salario": 60000
    }
}

# Acceder a valores en diccionarios anidados
print(f"Nombre del empleado 001: {empresa['empleado_001']['nombre']}")
print(f"Salario del empleado 002: {empresa['empleado_002']['salario']}")
print(f"Puesto del empleado 003: {empresa['empleado_003']['puesto']}")

# Modificar valores en diccionarios anidados
empresa["empleado_001"]["salario"] = 48000
print(f"\nNuevo salario de empleado 001: {empresa['empleado_001']['salario']}")

# Agregar un nuevo empleado
empresa["empleado_004"] = {
    "nombre": "Laura Sánchez",
    "edad": 27,
    "puesto": "Analista",
    "salario": 40000
}

# Iterar sobre diccionarios anidados
print("\nTodos los empleados:")
for id_empleado, datos in empresa.items():
    print(f"\n{id_empleado}:")
    for campo, valor in datos.items():
        print(f"  {campo}: {valor}")
print()

# ==============================================================================
# 8. DICCIONARIOS ANIDADOS - NIVEL 2 (Diccionario dentro de diccionario dentro de diccionario)
# ==============================================================================

print("=" * 80)
print("DICCIONARIOS ANIDADOS - NIVEL 2")
print("=" * 80)

"""
Podemos tener múltiples niveles de anidación.
Ejemplo: Una escuela con cursos, y cada curso tiene estudiantes con sus datos.
"""

escuela = {
    "matematicas": {
        "profesor": "Dr. Ramírez",
        "aula": "101",
        "estudiantes": {
            "est_001": {
                "nombre": "Sofía",
                "nota": 9.5,
                "asistencia": 95
            },
            "est_002": {
                "nombre": "Diego",
                "nota": 8.7,
                "asistencia": 90
            }
        }
    },
    "fisica": {
        "profesor": "Dra. Torres",
        "aula": "202",
        "estudiantes": {
            "est_003": {
                "nombre": "Elena",
                "nota": 9.0,
                "asistencia": 98
            },
            "est_004": {
                "nombre": "Roberto",
                "nota": 7.5,
                "asistencia": 85
            }
        }
    }
}

# Acceder a valores en 3 niveles de profundidad
print(f"Profesor de matemáticas: {escuela['matematicas']['profesor']}")
print(f"Nota de Sofía en matemáticas: {escuela['matematicas']['estudiantes']['est_001']['nota']}")
print(f"Asistencia de Elena en física: {escuela['fisica']['estudiantes']['est_003']['asistencia']}")

# Modificar valores en estructuras profundamente anidadas
escuela["matematicas"]["estudiantes"]["est_001"]["nota"] = 10.0
print(f"\nNueva nota de Sofía: {escuela['matematicas']['estudiantes']['est_001']['nota']}")

# Agregar un nuevo estudiante a un curso
escuela["matematicas"]["estudiantes"]["est_005"] = {
    "nombre": "Carmen",
    "nota": 9.2,
    "asistencia": 92
}

# Iterar sobre estructuras anidadas complejas
print("\nInformación completa de la escuela:")
for materia, info_materia in escuela.items():
    print(f"\n📚 MATERIA: {materia.upper()}")
    print(f"   Profesor: {info_materia['profesor']}")
    print(f"   Aula: {info_materia['aula']}")
    print(f"   Estudiantes:")
    for id_est, datos_est in info_materia["estudiantes"].items():
        print(f"      • {datos_est['nombre']} ({id_est})")
        print(f"        Nota: {datos_est['nota']}, Asistencia: {datos_est['asistencia']}%")
print()

# ==============================================================================
# 9. DICCIONARIOS ANIDADOS - NIVEL 3 (Aún más profundo)
# ==============================================================================

print("=" * 80)
print("DICCIONARIOS ANIDADOS - NIVEL 3")
print("=" * 80)

"""
Ejemplo: Sistema de gestión de una universidad con facultades, carreras, 
cursos y estudiantes.
"""

universidad = {
    "ingenieria": {
        "decano": "Dr. Fernández",
        "carreras": {
            "informatica": {
                "coordinador": "Ing. Ruiz",
                "cursos": {
                    "programacion_1": {
                        "creditos": 6,
                        "estudiantes": {
                            "2024001": {"nombre": "Luis", "nota": 8.5},
                            "2024002": {"nombre": "Ana", "nota": 9.0}
                        }
                    }
                }
            }
        }
    }
}

# Acceder a valores en 5 niveles de profundidad
nota_luis = universidad["ingenieria"]["carreras"]["informatica"]["cursos"]["programacion_1"]["estudiantes"]["2024001"]["nota"]
print(f"Nota de Luis en Programación 1: {nota_luis}")

# Forma más segura usando .get() para evitar errores
nota_segura = (universidad
               .get("ingenieria", {})
               .get("carreras", {})
               .get("informatica", {})
               .get("cursos", {})
               .get("programacion_1", {})
               .get("estudiantes", {})
               .get("2024001", {})
               .get("nota", "No encontrado"))
print(f"Acceso seguro con .get(): {nota_segura}")
print()

# ==============================================================================
# 10. LISTAS DENTRO DE DICCIONARIOS
# ==============================================================================

print("=" * 80)
print("LISTAS DENTRO DE DICCIONARIOS")
print("=" * 80)

"""
Los valores de un diccionario pueden ser listas, lo cual es muy útil
para almacenar múltiples elementos relacionados con una clave.
"""

# Ejemplo: Estudiante con múltiples calificaciones
estudiante_completo = {
    "nombre": "Roberto",
    "edad": 20,
    "calificaciones": [8.5, 9.0, 7.5, 9.5, 8.0],  # Lista de notas
    "materias": ["Matemáticas", "Física", "Química", "Historia", "Inglés"],
    "hobbies": ["Fútbol", "Lectura", "Videojuegos"]
}

print(f"Estudiante: {estudiante_completo['nombre']}")
print(f"Calificaciones: {estudiante_completo['calificaciones']}")
print(f"Primera calificación: {estudiante_completo['calificaciones'][0]}")
print(f"Última calificación: {estudiante_completo['calificaciones'][-1]}")

# Calcular promedio de calificaciones
promedio = sum(estudiante_completo["calificaciones"]) / len(estudiante_completo["calificaciones"])
print(f"Promedio: {promedio:.2f}")

# Agregar una nueva calificación
estudiante_completo["calificaciones"].append(9.8)
print(f"Calificaciones actualizadas: {estudiante_completo['calificaciones']}")

# Iterar sobre listas dentro del diccionario
print("\nMaterias del estudiante:")
for i, materia in enumerate(estudiante_completo["materias"], 1):
    print(f"  {i}. {materia}")
print()

# ==============================================================================
# 11. LISTAS DE DICCIONARIOS
# ==============================================================================

print("=" * 80)
print("LISTAS DE DICCIONARIOS")
print("=" * 80)

"""
Una lista puede contener múltiples diccionarios.
Esto es muy común para representar colecciones de objetos similares.
"""

# Ejemplo: Lista de productos en una tienda
productos = [
    {
        "id": 1,
        "nombre": "Laptop",
        "precio": 1200,
        "stock": 15
    },
    {
        "id": 2,
        "nombre": "Mouse",
        "precio": 25,
        "stock": 50
    },
    {
        "id": 3,
        "nombre": "Teclado",
        "precio": 75,
        "stock": 30
    }
]

print("Productos en la tienda:")
for producto in productos:
    print(f"  • {producto['nombre']}: ${producto['precio']} (Stock: {producto['stock']})")

# Buscar un producto específico
producto_buscado = "Mouse"
for producto in productos:
    if producto["nombre"] == producto_buscado:
        print(f"\n✓ Encontrado: {producto['nombre']} cuesta ${producto['precio']}")
        break

# Calcular valor total del inventario
valor_total = sum(p["precio"] * p["stock"] for p in productos)
print(f"\nValor total del inventario: ${valor_total}")
print()

# ==============================================================================
# 12. DICCIONARIO CON LISTAS DE DICCIONARIOS (Combinación compleja)
# ==============================================================================

print("=" * 80)
print("DICCIONARIO CON LISTAS DE DICCIONARIOS")
print("=" * 80)

"""
Estructura: Diccionario principal → Lista → Diccionarios
Muy útil para organizar datos categorizados.
"""

# Ejemplo: Restaurante con menú organizado por categorías
restaurante = {
    "nombre": "La Buena Mesa",
    "direccion": "Calle Principal 123",
    "menu": {
        "entradas": [
            {"nombre": "Ensalada César", "precio": 8.50, "vegetariano": True},
            {"nombre": "Sopa de tomate", "precio": 6.00, "vegetariano": True},
            {"nombre": "Alitas de pollo", "precio": 10.00, "vegetariano": False}
        ],
        "platos_principales": [
            {"nombre": "Filete de res", "precio": 22.00, "vegetariano": False},
            {"nombre": "Pasta primavera", "precio": 15.00, "vegetariano": True},
            {"nombre": "Salmón a la parrilla", "precio": 25.00, "vegetariano": False}
        ],
        "postres": [
            {"nombre": "Tiramisú", "precio": 7.00, "vegetariano": True},
            {"nombre": "Helado", "precio": 5.00, "vegetariano": True}
        ]
    }
}

print(f"Restaurante: {restaurante['nombre']}")
print(f"Dirección: {restaurante['direccion']}\n")

# Mostrar el menú completo
print("MENÚ:")
for categoria, platos in restaurante["menu"].items():
    print(f"\n  {categoria.upper().replace('_', ' ')}:")
    for plato in platos:
        veggie = "🌱" if plato["vegetariano"] else "🍖"
        print(f"    {veggie} {plato['nombre']}: ${plato['precio']:.2f}")

# Buscar platos vegetarianos
print("\n\nPlatos vegetarianos disponibles:")
for categoria, platos in restaurante["menu"].items():
    for plato in platos:
        if plato["vegetariano"]:
            print(f"  • {plato['nombre']} (${plato['precio']:.2f})")

# Agregar un nuevo plato a una categoría
restaurante["menu"]["postres"].append({
    "nombre": "Flan casero",
    "precio": 6.50,
    "vegetariano": True
})
print(f"\nPostres actualizados: {len(restaurante['menu']['postres'])} opciones")
print()

# ==============================================================================
# 13. LISTA CON DICCIONARIOS ANIDADOS (Múltiples niveles)
# ==============================================================================

print("=" * 80)
print("LISTA CON DICCIONARIOS ANIDADOS")
print("=" * 80)

"""
Estructura: Lista → Diccionario → Diccionario
Ejemplo: Lista de clientes, cada uno con información personal y dirección.
"""

clientes = [
    {
        "id": 1,
        "nombre": "Juan Pérez",
        "contacto": {
            "email": "juan@email.com",
            "telefono": "555-1234"
        },
        "direccion": {
            "calle": "Av. Libertad 456",
            "ciudad": "Barcelona",
            "codigo_postal": "08001"
        }
    },
    {
        "id": 2,
        "nombre": "María González",
        "contacto": {
            "email": "maria@email.com",
            "telefono": "555-5678"
        },
        "direccion": {
            "calle": "Calle Mayor 789",
            "ciudad": "Madrid",
            "codigo_postal": "28001"
        }
    }
]

print("Información de clientes:")
for cliente in clientes:
    print(f"\n👤 Cliente #{cliente['id']}: {cliente['nombre']}")
    print(f"   📧 Email: {cliente['contacto']['email']}")
    print(f"   📞 Teléfono: {cliente['contacto']['telefono']}")
    print(f"   🏠 Dirección: {cliente['direccion']['calle']}, {cliente['direccion']['ciudad']}")

# Buscar cliente por ciudad
ciudad_buscar = "Madrid"
print(f"\n\nClientes en {ciudad_buscar}:")
for cliente in clientes:
    if cliente["direccion"]["ciudad"] == ciudad_buscar:
        print(f"  • {cliente['nombre']}")
print()

# ==============================================================================
# 14. ESTRUCTURA ULTRA COMPLEJA: Diccionario → Lista → Diccionario → Diccionario
# ==============================================================================

print("=" * 80)
print("ESTRUCTURA ULTRA COMPLEJA")
print("=" * 80)

"""
Ejemplo del mundo real: Sistema de gestión de una red de hospitales
Estructura: Hospital → Departamentos (lista) → Doctores (dict) → Pacientes (dict)
"""

red_hospitales = {
    "Hospital Central": {
        "direccion": "Av. Principal 100",
        "telefono": "555-0000",
        "departamentos": [
            {
                "nombre": "Cardiología",
                "piso": 3,
                "doctores": {
                    "doc_001": {
                        "nombre": "Dr. Ramírez",
                        "especialidad": "Cardiólogo",
                        "pacientes": {
                            "pac_001": {
                                "nombre": "Pedro López",
                                "edad": 55,
                                "diagnostico": "Hipertensión",
                                "medicamentos": ["Enalapril", "Aspirina"]
                            },
                            "pac_002": {
                                "nombre": "Carmen Ruiz",
                                "edad": 62,
                                "diagnostico": "Arritmia",
                                "medicamentos": ["Betabloqueador"]
                            }
                        }
                    }
                }
            },
            {
                "nombre": "Pediatría",
                "piso": 2,
                "doctores": {
                    "doc_002": {
                        "nombre": "Dra. Martínez",
                        "especialidad": "Pediatra",
                        "pacientes": {
                            "pac_003": {
                                "nombre": "Sofía Gómez",
                                "edad": 8,
                                "diagnostico": "Gripe",
                                "medicamentos": ["Paracetamol"]
                            }
                        }
                    }
                }
            }
        ]
    },
    "Hospital Norte": {
        "direccion": "Calle Norte 200",
        "telefono": "555-1111",
        "departamentos": [
            {
                "nombre": "Traumatología",
                "piso": 1,
                "doctores": {
                    "doc_003": {
                        "nombre": "Dr. Torres",
                        "especialidad": "Traumatólogo",
                        "pacientes": {
                            "pac_004": {
                                "nombre": "Miguel Ángel",
                                "edad": 30,
                                "diagnostico": "Fractura de brazo",
                                "medicamentos": ["Ibuprofeno", "Antibiótico"]
                            }
                        }
                    }
                }
            }
        ]
    }
}

# Navegar por esta estructura compleja
print("RED DE HOSPITALES:\n")
for nombre_hospital, info_hospital in red_hospitales.items():
    print(f"🏥 {nombre_hospital}")
    print(f"   📍 {info_hospital['direccion']}")
    print(f"   📞 {info_hospital['telefono']}")
    
    for departamento in info_hospital["departamentos"]:
        print(f"\n   🏢 Departamento: {departamento['nombre']} (Piso {departamento['piso']})")
        
        for id_doctor, info_doctor in departamento["doctores"].items():
            print(f"      👨‍⚕️ {info_doctor['nombre']} - {info_doctor['especialidad']}")
            
            for id_paciente, info_paciente in info_doctor["pacientes"].items():
                print(f"         🤒 Paciente: {info_paciente['nombre']} ({info_paciente['edad']} años)")
                print(f"            Diagnóstico: {info_paciente['diagnostico']}")
                print(f"            Medicamentos: {', '.join(info_paciente['medicamentos'])}")
    print()

# Acceder a un dato específico en esta estructura compleja
# Obtener los medicamentos del primer paciente del Dr. Ramírez
medicamentos = (red_hospitales["Hospital Central"]["departamentos"][0]
                ["doctores"]["doc_001"]["pacientes"]["pac_001"]["medicamentos"])
print(f"Medicamentos de Pedro López: {medicamentos}")
print()

# ==============================================================================
# 15. DICCIONARIO → DICCIONARIO → LISTA → DICCIONARIO
# ==============================================================================

print("=" * 80)
print("DICCIONARIO → DICCIONARIO → LISTA → DICCIONARIO")
print("=" * 80)

"""
Ejemplo: Red social con usuarios, cada usuario tiene publicaciones (lista),
y cada publicación tiene información detallada (diccionario).
"""

red_social = {
    "usuario_001": {
        "nombre": "Laura Martínez",
        "edad": 28,
        "seguidores": 1500,
        "publicaciones": [
            {
                "id": 1,
                "fecha": "2026-03-20",
                "contenido": "¡Hermoso día en la playa!",
                "likes": 45,
                "comentarios": [
                    {"usuario": "Ana", "texto": "¡Qué bonito!"},
                    {"usuario": "Carlos", "texto": "Me encanta"}
                ]
            },
            {
                "id": 2,
                "fecha": "2026-03-22",
                "contenido": "Aprendiendo Python 🐍",
                "likes": 89,
                "comentarios": [
                    {"usuario": "Pedro", "texto": "Excelente lenguaje"}
                ]
            }
        ]
    },
    "usuario_002": {
        "nombre": "Carlos Ruiz",
        "edad": 32,
        "seguidores": 2300,
        "publicaciones": [
            {
                "id": 3,
                "fecha": "2026-03-25",
                "contenido": "Nuevo proyecto en GitHub",
                "likes": 120,
                "comentarios": []
            }
        ]
    }
}

print("PUBLICACIONES EN LA RED SOCIAL:\n")
for id_usuario, datos_usuario in red_social.items():
    print(f"👤 {datos_usuario['nombre']} ({datos_usuario['seguidores']} seguidores)")
    print(f"   Publicaciones:")
    
    for publicacion in datos_usuario["publicaciones"]:
        print(f"\n   📝 Post #{publicacion['id']} - {publicacion['fecha']}")
        print(f"      {publicacion['contenido']}")
        print(f"      ❤️ {publicacion['likes']} likes")
        
        if publicacion["comentarios"]:
            print(f"      💬 Comentarios:")
            for comentario in publicacion["comentarios"]:
                print(f"         • {comentario['usuario']}: {comentario['texto']}")
    print()

# Agregar una nueva publicación a un usuario
red_social["usuario_001"]["publicaciones"].append({
    "id": 4,
    "fecha": "2026-03-27",
    "contenido": "Viernes de código",
    "likes": 0,
    "comentarios": []
})

# Agregar un comentario a una publicación existente
red_social["usuario_001"]["publicaciones"][0]["comentarios"].append({
    "usuario": "Roberto",
    "texto": "¡Increíble vista!"
})

print("Después de agregar contenido:")
print(f"Total de publicaciones de Laura: {len(red_social['usuario_001']['publicaciones'])}")
print(f"Comentarios en primera publicación: {len(red_social['usuario_001']['publicaciones'][0]['comentarios'])}")
print()

# ==============================================================================
# 16. LISTA → DICCIONARIO → DICCIONARIO → LISTA → DICCIONARIO (Máxima complejidad)
# ==============================================================================

print("=" * 80)
print("ESTRUCTURA DE MÁXIMA COMPLEJIDAD")
print("=" * 80)

"""
Ejemplo: Sistema de gestión de una cadena de tiendas con inventario detallado
Estructura: Lista de tiendas → Cada tienda (dict) → Inventario por categoría (dict) 
→ Lista de productos → Cada producto (dict) con detalles
"""

cadena_tiendas = [
    {
        "id_tienda": "T001",
        "nombre": "Tienda Centro",
        "ciudad": "Madrid",
        "gerente": "Ana López",
        "inventario": {
            "electronica": [
                {
                    "codigo": "E001",
                    "producto": "Smartphone",
                    "marca": "Samsung",
                    "precio": 699,
                    "stock": 25,
                    "caracteristicas": {
                        "pantalla": "6.5 pulgadas",
                        "memoria": "128GB",
                        "color": "Negro"
                    }
                },
                {
                    "codigo": "E002",
                    "producto": "Tablet",
                    "marca": "Apple",
                    "precio": 899,
                    "stock": 15,
                    "caracteristicas": {
                        "pantalla": "10.9 pulgadas",
                        "memoria": "256GB",
                        "color": "Plata"
                    }
                }
            ],
            "ropa": [
                {
                    "codigo": "R001",
                    "producto": "Camiseta",
                    "marca": "Zara",
                    "precio": 29,
                    "stock": 100,
                    "caracteristicas": {
                        "talla": "M",
                        "material": "Algodón",
                        "color": "Azul"
                    }
                }
            ]
        }
    },
    {
        "id_tienda": "T002",
        "nombre": "Tienda Norte",
        "ciudad": "Barcelona",
        "gerente": "Carlos Ruiz",
        "inventario": {
            "electronica": [
                {
                    "codigo": "E003",
                    "producto": "Laptop",
                    "marca": "Dell",
                    "precio": 1299,
                    "stock": 10,
                    "caracteristicas": {
                        "procesador": "Intel i7",
                        "ram": "16GB",
                        "almacenamiento": "512GB SSD"
                    }
                }
            ],
            "hogar": [
                {
                    "codigo": "H001",
                    "producto": "Cafetera",
                    "marca": "Nespresso",
                    "precio": 199,
                    "stock": 20,
                    "caracteristicas": {
                        "tipo": "Cápsulas",
                        "capacidad": "1.2L",
                        "color": "Rojo"
                    }
                }
            ]
        }
    }
]

# Navegar por esta estructura ultra compleja
print("CADENA DE TIENDAS - INVENTARIO COMPLETO:\n")
for tienda in cadena_tiendas:
    print(f"🏪 {tienda['nombre']} ({tienda['id_tienda']})")
    print(f"   📍 Ciudad: {tienda['ciudad']}")
    print(f"   👔 Gerente: {tienda['gerente']}")
    print(f"   📦 INVENTARIO:")
    
    for categoria, productos in tienda["inventario"].items():
        print(f"\n      📂 {categoria.upper()}:")
        
        for producto in productos:
            print(f"         • {producto['producto']} - {producto['marca']}")
            print(f"           Código: {producto['codigo']}")
            print(f"           Precio: ${producto['precio']}")
            print(f"           Stock: {producto['stock']} unidades")
            print(f"           Características:")
            
            for caract, valor in producto["caracteristicas"].items():
                print(f"              - {caract}: {valor}")
    print("\n" + "-" * 80 + "\n")

# Ejemplo de búsqueda en estructura compleja: Encontrar un producto por código
codigo_buscar = "E002"
print(f"🔍 Buscando producto con código: {codigo_buscar}\n")

encontrado = False
for tienda in cadena_tiendas:
    for categoria, productos in tienda["inventario"].items():
        for producto in productos:
            if producto["codigo"] == codigo_buscar:
                print(f"✓ ENCONTRADO en {tienda['nombre']}:")
                print(f"  Producto: {producto['producto']}")
                print(f"  Marca: {producto['marca']}")
                print(f"  Precio: ${producto['precio']}")
                print(f"  Stock: {producto['stock']}")
                print(f"  Características: {producto['caracteristicas']}")
                encontrado = True
                break
        if encontrado:
            break
    if encontrado:
        break

if not encontrado:
    print(f"✗ Producto {codigo_buscar} no encontrado")
print()

# ==============================================================================
# 17. OPERACIONES AVANZADAS CON DICCIONARIOS
# ==============================================================================

print("=" * 80)
print("OPERACIONES AVANZADAS")
print("=" * 80)

# Copiar diccionarios
original = {"a": 1, "b": 2}
copia_superficial = original.copy()  # Copia superficial
copia_referencia = original  # ¡CUIDADO! Esto NO es una copia, es una referencia

original["a"] = 100
print(f"Original modificado: {original}")
print(f"Copia superficial (no afectada): {copia_superficial}")
print(f"Referencia (SÍ afectada): {copia_referencia}")

# Para copias profundas de diccionarios anidados, usar copy.deepcopy()
import copy

dict_anidado = {"nivel1": {"nivel2": {"valor": 10}}}
copia_profunda = copy.deepcopy(dict_anidado)
dict_anidado["nivel1"]["nivel2"]["valor"] = 999

print(f"\nOriginal anidado modificado: {dict_anidado}")
print(f"Copia profunda (no afectada): {copia_profunda}")
print()

# Combinar diccionarios
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"b": 20, "e": 5}  # Nota: 'b' se sobrescribirá

# Forma 1: Usando .update()
combinado = dict1.copy()
combinado.update(dict2)
print(f"Combinado con .update(): {combinado}")

# Forma 2: Usando ** (desempaquetado) - Python 3.5+
combinado2 = {**dict1, **dict2, **dict3}
print(f"Combinado con **: {combinado2}")

# Forma 3: Usando | (operador de unión) - Python 3.9+
combinado3 = dict1 | dict2 | dict3
print(f"Combinado con |: {combinado3}")
print()

# ==============================================================================
# 18. COMPRENSIÓN DE DICCIONARIOS (Dictionary Comprehension)
# ==============================================================================

print("=" * 80)
print("COMPRENSIÓN DE DICCIONARIOS")
print("=" * 80)

"""
Similar a las listas por comprensión, podemos crear diccionarios
de forma concisa y elegante.
"""

# Crear un diccionario de cuadrados
cuadrados = {x: x**2 for x in range(1, 6)}
print(f"Cuadrados: {cuadrados}")

# Diccionario con condición
pares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Cuadrados de números pares: {pares}")

# Invertir un diccionario (intercambiar claves y valores)
original_dict = {"a": 1, "b": 2, "c": 3}
invertido = {valor: clave for clave, valor in original_dict.items()}
print(f"Original: {original_dict}")
print(f"Invertido: {invertido}")

# Filtrar un diccionario
estudiantes_notas = {
    "Juan": 8.5,
    "María": 9.2,
    "Pedro": 6.8,
    "Laura": 9.5,
    "Carlos": 7.0
}

aprobados = {nombre: nota for nombre, nota in estudiantes_notas.items() if nota >= 7.0}
print(f"\nEstudiantes aprobados: {aprobados}")

sobresalientes = {nombre: nota for nombre, nota in estudiantes_notas.items() if nota >= 9.0}
print(f"Estudiantes sobresalientes: {sobresalientes}")
print()

# ==============================================================================
# 19. DICCIONARIOS CON VALORES POR DEFECTO (defaultdict)
# ==============================================================================

print("=" * 80)
print("DEFAULTDICT - DICCIONARIOS CON VALORES POR DEFECTO")
print("=" * 80)

"""
defaultdict es una subclase de dict que proporciona un valor por defecto
para claves que no existen, evitando errores KeyError.
"""

from collections import defaultdict

# defaultdict con lista como valor por defecto
grupos = defaultdict(list)
grupos["matematicas"].append("Juan")
grupos["matematicas"].append("María")
grupos["fisica"].append("Pedro")

print(f"Grupos: {dict(grupos)}")

# defaultdict con int como valor por defecto (útil para contadores)
contador = defaultdict(int)
palabras = ["manzana", "pera", "manzana", "uva", "pera", "manzana"]

for palabra in palabras:
    contador[palabra] += 1

print(f"Contador de palabras: {dict(contador)}")

# defaultdict con dict como valor por defecto
usuarios = defaultdict(dict)
usuarios["user1"]["nombre"] = "Ana"
usuarios["user1"]["edad"] = 25

print(f"Usuarios: {dict(usuarios)}")
print()

# ==============================================================================
# 20. EJEMPLO PRÁCTICO COMPLETO: SISTEMA DE GESTIÓN ESCOLAR
# ==============================================================================

print("=" * 80)
print("EJEMPLO PRÁCTICO COMPLETO: SISTEMA ESCOLAR")
print("=" * 80)

"""
Este ejemplo integra todos los conceptos vistos:
- Diccionarios anidados múltiples niveles
- Listas dentro de diccionarios
- Diccionarios dentro de listas
- Operaciones CRUD (Crear, Leer, Actualizar, Eliminar)
"""

sistema_escolar = {
    "nombre_institucion": "Colegio San Martín",
    "año_academico": 2026,
    "grados": {
        "primero_secundaria": {
            "tutor": "Prof. García",
            "aula": "A-101",
            "estudiantes": [
                {
                    "id": "2026001",
                    "nombre": "Lucía Fernández",
                    "edad": 12,
                    "materias": {
                        "matematicas": {
                            "profesor": "Prof. Ramírez",
                            "calificaciones": [8.5, 9.0, 8.8],
                            "tareas_pendientes": ["Ejercicios pág. 45", "Proyecto final"]
                        },
                        "lengua": {
                            "profesor": "Prof. Martínez",
                            "calificaciones": [9.5, 9.2, 9.8],
                            "tareas_pendientes": ["Ensayo literario"]
                        }
                    },
                    "actividades_extracurriculares": ["Fútbol", "Teatro"]
                },
                {
                    "id": "2026002",
                    "nombre": "Miguel Ángel Torres",
                    "edad": 13,
                    "materias": {
                        "matematicas": {
                            "profesor": "Prof. Ramírez",
                            "calificaciones": [7.5, 8.0, 7.8],
                            "tareas_pendientes": ["Ejercicios pág. 45"]
                        },
                        "lengua": {
                            "profesor": "Prof. Martínez",
                            "calificaciones": [8.0, 8.5, 8.2],
                            "tareas_pendientes": []
                        }
                    },
                    "actividades_extracurriculares": ["Baloncesto"]
                }
            ]
        },
        "segundo_secundaria": {
            "tutor": "Prof. Sánchez",
            "aula": "A-201",
            "estudiantes": [
                {
                    "id": "2025001",
                    "nombre": "Isabella Moreno",
                    "edad": 13,
                    "materias": {
                        "ciencias": {
                            "profesor": "Prof. López",
                            "calificaciones": [9.8, 9.5, 10.0],
                            "tareas_pendientes": []
                        }
                    },
                    "actividades_extracurriculares": ["Robótica", "Ajedrez"]
                }
            ]
        }
    }
}

# OPERACIÓN 1: Mostrar información general
print(f"🏫 {sistema_escolar['nombre_institucion']}")
print(f"📅 Año académico: {sistema_escolar['año_academico']}\n")

# OPERACIÓN 2: Listar todos los estudiantes de un grado
print("ESTUDIANTES DE PRIMERO DE SECUNDARIA:")
for estudiante in sistema_escolar["grados"]["primero_secundaria"]["estudiantes"]:
    print(f"  • {estudiante['nombre']} (ID: {estudiante['id']}) - {estudiante['edad']} años")
print()

# OPERACIÓN 3: Calcular promedio de un estudiante en una materia
estudiante_lucia = sistema_escolar["grados"]["primero_secundaria"]["estudiantes"][0]
calificaciones_mate = estudiante_lucia["materias"]["matematicas"]["calificaciones"]
promedio_mate = sum(calificaciones_mate) / len(calificaciones_mate)

print(f"📊 Promedio de {estudiante_lucia['nombre']} en Matemáticas: {promedio_mate:.2f}")
print()

# OPERACIÓN 4: Agregar una nueva calificación
sistema_escolar["grados"]["primero_secundaria"]["estudiantes"][0]["materias"]["matematicas"]["calificaciones"].append(9.5)
print(f"Nueva calificación agregada a Lucía en Matemáticas")
print(f"Calificaciones actualizadas: {estudiante_lucia['materias']['matematicas']['calificaciones']}")
print()

# OPERACIÓN 5: Listar todas las tareas pendientes de todos los estudiantes
print("📝 TAREAS PENDIENTES POR ESTUDIANTE:")
for grado, info_grado in sistema_escolar["grados"].items():
    for estudiante in info_grado["estudiantes"]:
        tiene_tareas = False
        tareas_estudiante = []
        
        for materia, info_materia in estudiante["materias"].items():
            if info_materia["tareas_pendientes"]:
                tiene_tareas = True
                for tarea in info_materia["tareas_pendientes"]:
                    tareas_estudiante.append(f"{materia}: {tarea}")
        
        if tiene_tareas:
            print(f"\n  {estudiante['nombre']}:")
            for tarea in tareas_estudiante:
                print(f"    - {tarea}")

if not tiene_tareas:
    print("  ¡Todos los estudiantes están al día!")
print()

# OPERACIÓN 6: Generar reporte de promedios generales
print("📈 REPORTE DE PROMEDIOS GENERALES:")
for grado, info_grado in sistema_escolar["grados"].items():
    print(f"\n{grado.replace('_', ' ').title()}:")
    
    for estudiante in info_grado["estudiantes"]:
        print(f"  {estudiante['nombre']}:")
        
        for materia, info_materia in estudiante["materias"].items():
            if info_materia["calificaciones"]:
                promedio = sum(info_materia["calificaciones"]) / len(info_materia["calificaciones"])
                print(f"    • {materia.title()}: {promedio:.2f}")
print()

# ==============================================================================
# 21. FUNCIONES ÚTILES PARA TRABAJAR CON DICCIONARIOS ANIDADOS
# ==============================================================================

print("=" * 80)
print("FUNCIONES ÚTILES PERSONALIZADAS")
print("=" * 80)

def obtener_valor_anidado(diccionario, ruta, valor_defecto=None):
    """
    Obtiene un valor de un diccionario anidado usando una ruta de claves.
    
    Args:
        diccionario: El diccionario a consultar
        ruta: Lista de claves para navegar (ej: ["nivel1", "nivel2", "valor"])
        valor_defecto: Valor a retornar si no se encuentra la ruta
    
    Returns:
        El valor encontrado o valor_defecto
    """
    resultado = diccionario
    try:
        for clave in ruta:
            resultado = resultado[clave]
        return resultado
    except (KeyError, TypeError, IndexError):
        return valor_defecto

# Ejemplo de uso
ruta = ["grados", "primero_secundaria", "tutor"]
tutor = obtener_valor_anidado(sistema_escolar, ruta)
print(f"Tutor de primero: {tutor}")

# Ruta que no existe
ruta_invalida = ["grados", "tercero_secundaria", "tutor"]
tutor_inexistente = obtener_valor_anidado(sistema_escolar, ruta_invalida, "No encontrado")
print(f"Tutor inexistente: {tutor_inexistente}")
print()


def establecer_valor_anidado(diccionario, ruta, valor):
    """
    Establece un valor en un diccionario anidado, creando niveles si no existen.
    
    Args:
        diccionario: El diccionario a modificar
        ruta: Lista de claves para navegar
        valor: El valor a establecer
    """
    for clave in ruta[:-1]:
        if clave not in diccionario:
            diccionario[clave] = {}
        diccionario = diccionario[clave]
    diccionario[ruta[-1]] = valor


# Ejemplo de uso
config = {}
establecer_valor_anidado(config, ["servidor", "base_datos", "host"], "localhost")
establecer_valor_anidado(config, ["servidor", "base_datos", "puerto"], 5432)
establecer_valor_anidado(config, ["servidor", "api", "version"], "v2")

print(f"Configuración creada dinámicamente: {config}")
print()


def aplanar_diccionario(diccionario, padre="", separador="_"):
    """
    Convierte un diccionario anidado en uno plano.
    
    Args:
        diccionario: El diccionario anidado
        padre: Prefijo para las claves (uso interno)
        separador: Separador entre niveles
    
    Returns:
        Diccionario plano
    """
    items = []
    for clave, valor in diccionario.items():
        nueva_clave = f"{padre}{separador}{clave}" if padre else clave
        
        if isinstance(valor, dict):
            items.extend(aplanar_diccionario(valor, nueva_clave, separador).items())
        else:
            items.append((nueva_clave, valor))
    
    return dict(items)


# Ejemplo de uso
anidado = {
    "usuario": {
        "nombre": "Juan",
        "contacto": {
            "email": "juan@email.com",
            "telefono": "555-1234"
        }
    },
    "configuracion": {
        "tema": "oscuro"
    }
}

plano = aplanar_diccionario(anidado)
print("Diccionario anidado aplanado:")
for clave, valor in plano.items():
    print(f"  {clave}: {valor}")
print()

# ==============================================================================
# 22. EJEMPLO REAL: API REST - RESPUESTA JSON
# ==============================================================================

print("=" * 80)
print("EJEMPLO REAL: RESPUESTA DE API REST")
print("=" * 80)

"""
Las APIs REST suelen devolver datos en formato JSON, que en Python
se representan como diccionarios anidados complejos.
"""

respuesta_api = {
    "status": "success",
    "code": 200,
    "data": {
        "usuario": {
            "id": 12345,
            "username": "developer_pro",
            "perfil": {
                "nombre_completo": "Andrea Rodríguez",
                "email": "andrea@example.com",
                "avatar": "https://example.com/avatar.jpg",
                "verificado": True
            },
            "estadisticas": {
                "publicaciones": 156,
                "seguidores": 2340,
                "siguiendo": 890
            }
        },
        "publicaciones_recientes": [
            {
                "id": 9001,
                "titulo": "Aprendiendo Python",
                "fecha": "2026-03-25",
                "contenido": "Los diccionarios son increíbles",
                "etiquetas": ["python", "programacion", "tutorial"],
                "interacciones": {
                    "likes": 234,
                    "comentarios": 45,
                    "compartidos": 12
                }
            },
            {
                "id": 9002,
                "titulo": "Estructuras de datos",
                "fecha": "2026-03-26",
                "contenido": "Comparando listas y diccionarios",
                "etiquetas": ["python", "datos"],
                "interacciones": {
                    "likes": 189,
                    "comentarios": 32,
                    "compartidos": 8
                }
            }
        ]
    },
    "metadata": {
        "timestamp": "2026-03-27T10:30:00Z",
        "version": "2.1",
        "servidor": "api-server-03"
    }
}

# Procesar la respuesta de la API
if respuesta_api["status"] == "success":
    usuario = respuesta_api["data"]["usuario"]
    perfil = usuario["perfil"]
    
    print(f"✓ Solicitud exitosa (Código: {respuesta_api['code']})")
    print(f"\n👤 Usuario: {perfil['nombre_completo']} (@{usuario['username']})")
    print(f"   Email: {perfil['email']}")
    print(f"   Verificado: {'Sí' if perfil['verificado'] else 'No'}")
    
    stats = usuario["estadisticas"]
    print(f"\n📊 Estadísticas:")
    print(f"   Publicaciones: {stats['publicaciones']}")
    print(f"   Seguidores: {stats['seguidores']}")
    print(f"   Siguiendo: {stats['siguiendo']}")
    
    print(f"\n📝 Publicaciones recientes:")
    for pub in respuesta_api["data"]["publicaciones_recientes"]:
        print(f"\n   • {pub['titulo']} (ID: {pub['id']})")
        print(f"     Fecha: {pub['fecha']}")
        print(f"     Contenido: {pub['contenido']}")
        print(f"     Etiquetas: {', '.join(pub['etiquetas'])}")
        print(f"     ❤️ {pub['interacciones']['likes']} likes | "
              f"💬 {pub['interacciones']['comentarios']} comentarios | "
              f"🔄 {pub['interacciones']['compartidos']} compartidos")

print()

# ==============================================================================
# 23. EJEMPLO REAL: CONFIGURACIÓN DE APLICACIÓN
# ==============================================================================

print("=" * 80)
print("EJEMPLO REAL: ARCHIVO DE CONFIGURACIÓN")
print("=" * 80)

"""
Los archivos de configuración suelen usar diccionarios anidados
para organizar diferentes aspectos de una aplicación.
"""

configuracion_app = {
    "app": {
        "nombre": "MiAplicacion",
        "version": "1.5.2",
        "debug": False,
        "idioma": "es"
    },
    "base_datos": {
        "principal": {
            "tipo": "postgresql",
            "host": "localhost",
            "puerto": 5432,
            "nombre": "mi_base_datos",
            "credenciales": {
                "usuario": "admin",
                "password": "********"  # En producción, usar variables de entorno
            },
            "pool": {
                "min_conexiones": 5,
                "max_conexiones": 20,
                "timeout": 30
            }
        },
        "cache": {
            "tipo": "redis",
            "host": "localhost",
            "puerto": 6379,
            "ttl": 3600
        }
    },
    "servicios_externos": {
        "email": {
            "proveedor": "smtp.gmail.com",
            "puerto": 587,
            "ssl": True,
            "credenciales": {
                "usuario": "app@example.com",
                "api_key": "********"
            }
        },
        "almacenamiento": {
            "tipo": "s3",
            "region": "us-east-1",
            "bucket": "mi-bucket",
            "credenciales": {
                "access_key": "********",
                "secret_key": "********"
            }
        }
    },
    "logging": {
        "nivel": "INFO",
        "archivo": "/var/log/app.log",
        "formato": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        "rotacion": {
            "max_bytes": 10485760,  # 10MB
            "backup_count": 5
        }
    }
}

print("⚙️ CONFIGURACIÓN DE LA APLICACIÓN:\n")
print(f"Aplicación: {configuracion_app['app']['nombre']} v{configuracion_app['app']['version']}")
print(f"Modo debug: {configuracion_app['app']['debug']}")
print(f"\nBase de datos principal: {configuracion_app['base_datos']['principal']['tipo']}")
print(f"Host: {configuracion_app['base_datos']['principal']['host']}:{configuracion_app['base_datos']['principal']['puerto']}")
print(f"Pool de conexiones: {configuracion_app['base_datos']['principal']['pool']['min_conexiones']}-{configuracion_app['base_datos']['principal']['pool']['max_conexiones']}")
print(f"\nServicio de email: {configuracion_app['servicios_externos']['email']['proveedor']}")
print(f"Nivel de logging: {configuracion_app['logging']['nivel']}")
print()

# ==============================================================================
# 24. EJEMPLO REAL: CARRITO DE COMPRAS E-COMMERCE
# ==============================================================================

print("=" * 80)
print("EJEMPLO REAL: CARRITO DE COMPRAS")
print("=" * 80)

"""
Sistema de carrito de compras con productos, cantidades, descuentos y cálculos.
"""

carrito_compras = {
    "id_carrito": "CART-2026-001",
    "usuario": {
        "id": "USER-456",
        "nombre": "Patricia Gómez",
        "email": "patricia@email.com",
        "nivel_membresia": "premium"
    },
    "items": [
        {
            "producto_id": "PROD-001",
            "nombre": "Laptop Gaming",
            "categoria": "Electrónica",
            "precio_unitario": 1500,
            "cantidad": 1,
            "descuento": {
                "tipo": "porcentaje",
                "valor": 10,
                "codigo": "TECH10"
            },
            "especificaciones": {
                "marca": "ASUS",
                "modelo": "ROG Strix",
                "garantia": "2 años"
            }
        },
        {
            "producto_id": "PROD-002",
            "nombre": "Mouse Inalámbrico",
            "categoria": "Accesorios",
            "precio_unitario": 45,
            "cantidad": 2,
            "descuento": None,
            "especificaciones": {
                "marca": "Logitech",
                "modelo": "MX Master 3",
                "garantia": "1 año"
            }
        },
        {
            "producto_id": "PROD-003",
            "nombre": "Teclado Mecánico",
            "categoria": "Accesorios",
            "precio_unitario": 120,
            "cantidad": 1,
            "descuento": {
                "tipo": "fijo",
                "valor": 20,
                "codigo": "WELCOME20"
            },
            "especificaciones": {
                "marca": "Corsair",
                "modelo": "K95 RGB",
                "garantia": "2 años"
            }
        }
    ],
    "envio": {
        "metodo": "Express",
        "costo": 15,
        "direccion": {
            "calle": "Av. Reforma 456",
            "ciudad": "Ciudad de México",
            "codigo_postal": "06600",
            "pais": "México"
        },
        "tiempo_estimado": "2-3 días"
    }
}

# Función para calcular el total del carrito
def calcular_total_carrito(carrito):
    """
    Calcula el total del carrito incluyendo descuentos y envío.
    """
    subtotal = 0
    descuento_total = 0
    
    print(f"🛒 CARRITO DE COMPRAS - {carrito['id_carrito']}")
    print(f"Cliente: {carrito['usuario']['nombre']} (Membresía: {carrito['usuario']['nivel_membresia']})\n")
    print("PRODUCTOS:")
    
    for item in carrito["items"]:
        precio_base = item["precio_unitario"] * item["cantidad"]
        descuento_item = 0
        
        # Calcular descuento si existe
        if item["descuento"]:
            if item["descuento"]["tipo"] == "porcentaje":
                descuento_item = precio_base * (item["descuento"]["valor"] / 100)
            elif item["descuento"]["tipo"] == "fijo":
                descuento_item = item["descuento"]["valor"]
        
        precio_final_item = precio_base - descuento_item
        subtotal += precio_final_item
        descuento_total += descuento_item
        
        print(f"\n  • {item['nombre']} x{item['cantidad']}")
        print(f"    Marca: {item['especificaciones']['marca']} {item['especificaciones']['modelo']}")
        print(f"    Precio unitario: ${item['precio_unitario']}")
        print(f"    Subtotal: ${precio_base}")
        
        if descuento_item > 0:
            print(f"    Descuento ({item['descuento']['codigo']}): -${descuento_item:.2f}")
            print(f"    Total: ${precio_final_item:.2f}")
    
    # Descuento adicional por membresía premium
    descuento_membresia = 0
    if carrito["usuario"]["nivel_membresia"] == "premium":
        descuento_membresia = subtotal * 0.05  # 5% adicional
        print(f"\n  🌟 Descuento membresía premium (5%): -${descuento_membresia:.2f}")
    
    costo_envio = carrito["envio"]["costo"]
    total_final = subtotal - descuento_membresia + costo_envio
    
    print(f"\n{'─' * 50}")
    print(f"  Subtotal: ${subtotal:.2f}")
    print(f"  Descuentos: -${(descuento_total + descuento_membresia):.2f}")
    print(f"  Envío ({carrito['envio']['metodo']}): ${costo_envio:.2f}")
    print(f"  {'─' * 50}")
    print(f"  TOTAL A PAGAR: ${total_final:.2f}")
    print(f"\n📦 Envío a: {carrito['envio']['direccion']['calle']}, {carrito['envio']['direccion']['ciudad']}")
    print(f"⏱️ Tiempo estimado: {carrito['envio']['tiempo_estimado']}")
    
    return total_final

total = calcular_total_carrito(carrito_compras)
print()

# ==============================================================================
# 25. EJEMPLO REAL: ÁRBOL GENEALÓGICO
# ==============================================================================

print("=" * 80)
print("EJEMPLO REAL: ÁRBOL GENEALÓGICO")
print("=" * 80)

"""
Representación de un árbol genealógico usando diccionarios anidados recursivos.
"""

arbol_genealogico = {
    "nombre": "José Martínez",
    "nacimiento": 1950,
    "profesion": "Ingeniero",
    "hijos": [
        {
            "nombre": "Carlos Martínez",
            "nacimiento": 1975,
            "profesion": "Médico",
            "hijos": [
                {
                    "nombre": "Sofía Martínez",
                    "nacimiento": 2005,
                    "profesion": "Estudiante",
                    "hijos": []
                },
                {
                    "nombre": "Diego Martínez",
                    "nacimiento": 2008,
                    "profesion": "Estudiante",
                    "hijos": []
                }
            ]
        },
        {
            "nombre": "Laura Martínez",
            "nacimiento": 1978,
            "profesion": "Arquitecta",
            "hijos": [
                {
                    "nombre": "Emma García",
                    "nacimiento": 2010,
                    "profesion": "Estudiante",
                    "hijos": []
                }
            ]
        }
    ]
}


def mostrar_arbol_genealogico(persona, nivel=0):
    """
    Muestra el árbol genealógico de forma recursiva.
    """
    indentacion = "  " * nivel
    edad = 2026 - persona["nacimiento"]
    print(f"{indentacion}👤 {persona['nombre']} ({edad} años) - {persona['profesion']}")
    
    if persona["hijos"]:
        for hijo in persona["hijos"]:
            mostrar_arbol_genealogico(hijo, nivel + 1)


print("🌳 ÁRBOL GENEALÓGICO DE LA FAMILIA MARTÍNEZ:\n")
mostrar_arbol_genealogico(arbol_genealogico)
print()


def contar_descendientes(persona):
    """
    Cuenta el número total de descendientes de una persona.
    """
    if not persona["hijos"]:
        return 0
    
    total = len(persona["hijos"])
    for hijo in persona["hijos"]:
        total += contar_descendientes(hijo)
    
    return total


total_descendientes = contar_descendientes(arbol_genealogico)
print(f"José Martínez tiene {total_descendientes} descendientes en total")
print()

# ==============================================================================
# 26. TIPS Y MEJORES PRÁCTICAS
# ==============================================================================

print("=" * 80)
print("TIPS Y MEJORES PRÁCTICAS")
print("=" * 80)

"""
1. USAR .get() EN LUGAR DE []
   - Evita errores KeyError cuando la clave puede no existir
   - Permite especificar valores por defecto
"""

datos = {"nombre": "Juan"}
# ❌ Malo: puede causar error
# apellido = datos["apellido"]  # KeyError!

# ✓ Bueno: maneja claves inexistentes
apellido = datos.get("apellido", "Desconocido")
print(f"1. Uso de .get(): {apellido}")

"""
2. VERIFICAR EXISTENCIA DE CLAVES CON 'in'
   - Más legible y pythónico
"""

if "nombre" in datos:
    print(f"2. La clave existe: {datos['nombre']}")

"""
3. USAR .items() PARA ITERAR
   - Más eficiente y legible que iterar sobre claves
"""

persona_simple = {"nombre": "Ana", "edad": 25}
print("\n3. Iteración con .items():")
for clave, valor in persona_simple.items():
    print(f"   {clave}: {valor}")

"""
4. COMPRENSIÓN DE DICCIONARIOS PARA TRANSFORMACIONES
   - Más conciso y rápido que bucles tradicionales
"""

numeros = {"a": 1, "b": 2, "c": 3}
duplicados = {k: v * 2 for k, v in numeros.items()}
print(f"\n4. Comprensión de diccionarios: {duplicados}")

"""
5. USAR setdefault() PARA INICIALIZAR VALORES
   - Útil cuando necesitas asegurar que una clave existe
"""

contador_letras = {}
texto = "hola mundo"
for letra in texto:
    if letra != " ":
        contador_letras.setdefault(letra, 0)
        contador_letras[letra] += 1

print(f"\n5. setdefault() para contadores: {contador_letras}")

"""
6. EVITAR MODIFICAR DICCIONARIOS MIENTRAS SE ITERAN
   - Puede causar errores RuntimeError
"""

# ❌ Malo: modificar mientras se itera
# for clave in diccionario:
#     del diccionario[clave]  # Error!

# ✓ Bueno: crear una lista de claves primero
diccionario_prueba = {"a": 1, "b": 2, "c": 3}
claves_a_eliminar = [k for k in diccionario_prueba if diccionario_prueba[k] < 3]
for clave in claves_a_eliminar:
    del diccionario_prueba[clave]

print(f"\n6. Eliminación segura: {diccionario_prueba}")

"""
7. USAR isinstance() PARA VERIFICAR TIPOS EN ESTRUCTURAS ANIDADAS
   - Importante cuando trabajas con datos de fuentes externas
"""

def procesar_valor(valor):
    if isinstance(valor, dict):
        return "Es un diccionario"
    elif isinstance(valor, list):
        return "Es una lista"
    elif isinstance(valor, str):
        return "Es un string"
    else:
        return f"Es de tipo {type(valor).__name__}"

print(f"\n7. Verificación de tipos:")
print(f"   {procesar_valor({'a': 1})}")
print(f"   {procesar_valor([1, 2, 3])}")
print(f"   {procesar_valor('texto')}")
print()

# ==============================================================================
# 27. ERRORES COMUNES Y CÓMO EVITARLOS
# ==============================================================================

print("=" * 80)
print("ERRORES COMUNES Y SOLUCIONES")
print("=" * 80)

"""
ERROR 1: KeyError - Intentar acceder a una clave que no existe
"""
print("\n❌ ERROR 1: KeyError")
try:
    persona_test = {"nombre": "Juan"}
    apellido = persona_test["apellido"]  # Esto causa KeyError
except KeyError as e:
    print(f"   Error capturado: {e}")
    print(f"   ✓ Solución: Usar .get() → {persona_test.get('apellido', 'N/A')}")

"""
ERROR 2: TypeError - Usar un tipo mutable como clave
"""
print("\n❌ ERROR 2: TypeError con claves mutables")
try:
    dict_invalido = {[1, 2]: "valor"}  # Las listas no pueden ser claves
except TypeError as e:
    print(f"   Error: No se pueden usar listas como claves")
    dict_con_tupla = {(1, 2): "valor"}
    print(f"   ✓ Solución: Usar tuplas → {dict_con_tupla}")

"""
ERROR 3: Modificar copia superficial de diccionario anidado
"""
print("\n❌ ERROR 3: Copia superficial de diccionarios anidados")
original_anidado = {"nivel1": {"nivel2": "valor"}}
copia_superficial = original_anidado.copy()
copia_superficial["nivel1"]["nivel2"] = "modificado"

print(f"   Original (afectado): {original_anidado}")
print(f"   ✓ Solución: Usar copy.deepcopy() para diccionarios anidados")

"""
ERROR 4: Asumir orden en versiones antiguas de Python
"""
print("\n❌ ERROR 4: Orden de diccionarios")
print(f"   En Python 3.7+: Los diccionarios mantienen el orden de inserción")
print(f"   En Python 3.6-: El orden no está garantizado")
print(f"   ✓ Solución: Si el orden es crítico, usar OrderedDict o Python 3.7+")
print()

# ==============================================================================
# 28. CASOS DE USO PRÁCTICOS
# ==============================================================================

print("=" * 80)
print("CASOS DE USO PRÁCTICOS")
print("=" * 80)

"""
CASO 1: Contador de frecuencias
"""
print("\n📊 CASO 1: Contador de frecuencias de palabras")

texto_ejemplo = "python es genial python es poderoso python es versátil"
palabras_lista = texto_ejemplo.split()

frecuencias = {}
for palabra in palabras_lista:
    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

print(f"Texto: '{texto_ejemplo}'")
print("Frecuencias:")
for palabra, cantidad in frecuencias.items():
    print(f"  '{palabra}': {cantidad} veces")

"""
CASO 2: Agrupar datos por categoría
"""
print("\n📁 CASO 2: Agrupar estudiantes por edad")

estudiantes_lista = [
    {"nombre": "Ana", "edad": 12},
    {"nombre": "Luis", "edad": 13},
    {"nombre": "María", "edad": 12},
    {"nombre": "Pedro", "edad": 13},
    {"nombre": "Carmen", "edad": 12}
]

por_edad = {}
for estudiante in estudiantes_lista:
    edad = estudiante["edad"]
    if edad not in por_edad:
        por_edad[edad] = []
    por_edad[edad].append(estudiante["nombre"])

print("Estudiantes agrupados por edad:")
for edad, nombres in por_edad.items():
    print(f"  {edad} años: {', '.join(nombres)}")

"""
CASO 3: Caché de resultados (memoización)
"""
print("\n💾 CASO 3: Caché de resultados")

cache_fibonacci = {}

def fibonacci_con_cache(n):
    """
    Calcula el número de Fibonacci usando un diccionario como caché.
    """
    if n in cache_fibonacci:
        return cache_fibonacci[n]
    
    if n <= 1:
        return n
    
    resultado = fibonacci_con_cache(n - 1) + fibonacci_con_cache(n - 2)
    cache_fibonacci[n] = resultado
    return resultado

# Calcular algunos números de Fibonacci
for i in range(10):
    fib = fibonacci_con_cache(i)
    print(f"  F({i}) = {fib}")

print(f"\nCaché generado: {cache_fibonacci}")

"""
CASO 4: Índice invertido (búsqueda rápida)
"""
print("\n🔍 CASO 4: Índice invertido para búsqueda")

documentos = [
    {"id": 1, "titulo": "Python básico", "palabras": ["python", "programacion", "basico"]},
    {"id": 2, "titulo": "Python avanzado", "palabras": ["python", "programacion", "avanzado"]},
    {"id": 3, "titulo": "JavaScript intro", "palabras": ["javascript", "web", "programacion"]}
]

# Crear índice invertido: palabra → lista de documentos que la contienen
indice_invertido = {}
for doc in documentos:
    for palabra in doc["palabras"]:
        if palabra not in indice_invertido:
            indice_invertido[palabra] = []
        indice_invertido[palabra].append(doc["id"])

print("Índice invertido creado:")
for palabra, docs in indice_invertido.items():
    print(f"  '{palabra}' aparece en documentos: {docs}")

# Buscar documentos que contengan una palabra
palabra_buscar = "python"
docs_encontrados = indice_invertido.get(palabra_buscar, [])
print(f"\nDocumentos que contienen '{palabra_buscar}': {docs_encontrados}")
print()

# ==============================================================================
# 29. SERIALIZACIÓN: GUARDAR Y CARGAR DICCIONARIOS
# ==============================================================================

print("=" * 80)
print("SERIALIZACIÓN: GUARDAR Y CARGAR DICCIONARIOS")
print("=" * 80)

"""
Los diccionarios se pueden guardar en archivos y cargar después
usando JSON (formato más común) o pickle (específico de Python).
"""

import json

# Diccionario a guardar
datos_usuario = {
    "nombre": "Roberto",
    "edad": 30,
    "hobbies": ["lectura", "ciclismo"],
    "configuracion": {
        "tema": "oscuro",
        "notificaciones": True
    }
}

# Convertir a JSON string
json_string = json.dumps(datos_usuario, indent=2, ensure_ascii=False)
print("Diccionario convertido a JSON:")
print(json_string)

# Convertir de JSON string a diccionario
datos_recuperados = json.loads(json_string)
print(f"\nDatos recuperados: {datos_recuperados}")
print(f"Tipo: {type(datos_recuperados)}")
print()

# Nota: Para guardar en archivo, usar:
# with open("datos.json", "w", encoding="utf-8") as archivo:
#     json.dump(datos_usuario, archivo, indent=2, ensure_ascii=False)
#
# Para cargar desde archivo:
# with open("datos.json", "r", encoding="utf-8") as archivo:
#     datos = json.load(archivo)

# ==============================================================================
# 30. EJERCICIOS PRÁCTICOS RESUELTOS
# ==============================================================================

print("=" * 80)
print("EJERCICIOS PRÁCTICOS RESUELTOS")
print("=" * 80)

"""
EJERCICIO 1: Crear un sistema de inventario de biblioteca
"""
print("\n📚 EJERCICIO 1: Sistema de biblioteca")

biblioteca = {
    "libros": [
        {
            "isbn": "978-0-123456-78-9",
            "titulo": "Python para todos",
            "autor": {
                "nombre": "Juan Pérez",
                "nacionalidad": "España"
            },
            "detalles": {
                "año": 2024,
                "paginas": 450,
                "editorial": "Tech Books"
            },
            "disponible": True,
            "prestamos": [
                {"usuario": "María", "fecha_prestamo": "2026-03-01", "fecha_devolucion": "2026-03-15"},
                {"usuario": "Carlos", "fecha_prestamo": "2026-02-10", "fecha_devolucion": "2026-02-24"}
            ]
        },
        {
            "isbn": "978-0-987654-32-1",
            "titulo": "Estructuras de datos",
            "autor": {
                "nombre": "Laura Gómez",
                "nacionalidad": "México"
            },
            "detalles": {
                "año": 2025,
                "paginas": 380,
                "editorial": "Code Press"
            },
            "disponible": False,
            "prestamos": [
                {"usuario": "Pedro", "fecha_prestamo": "2026-03-20", "fecha_devolucion": None}
            ]
        }
    ]
}

# Función para buscar libros disponibles
def libros_disponibles(biblioteca):
    disponibles = [libro for libro in biblioteca["libros"] if libro["disponible"]]
    return disponibles

# Función para buscar libros por autor
def buscar_por_autor(biblioteca, nombre_autor):
    encontrados = [libro for libro in biblioteca["libros"] 
                   if nombre_autor.lower() in libro["autor"]["nombre"].lower()]
    return encontrados

# Usar las funciones
print("Libros disponibles:")
for libro in libros_disponibles(biblioteca):
    print(f"  • {libro['titulo']} - {libro['autor']['nombre']}")

print("\nLibros de 'Pérez':")
for libro in buscar_por_autor(biblioteca, "Pérez"):
    print(f"  • {libro['titulo']} ({libro['detalles']['año']})")

# Calcular estadísticas
total_libros = len(biblioteca["libros"])
libros_prestados = sum(1 for libro in biblioteca["libros"] if not libro["disponible"])
print(f"\nEstadísticas: {libros_prestados}/{total_libros} libros prestados")
print()

"""
EJERCICIO 2: Sistema de reservas de hotel
"""
print("🏨 EJERCICIO 2: Sistema de reservas de hotel")

hotel = {
    "nombre": "Hotel Paradise",
    "estrellas": 5,
    "pisos": {
        "piso_1": {
            "habitaciones": [
                {
                    "numero": 101,
                    "tipo": "simple",
                    "precio_noche": 80,
                    "ocupada": False,
                    "servicios": ["wifi", "tv", "aire_acondicionado"]
                },
                {
                    "numero": 102,
                    "tipo": "doble",
                    "precio_noche": 120,
                    "ocupada": True,
                    "servicios": ["wifi", "tv", "aire_acondicionado", "minibar"],
                    "huesped": {
                        "nombre": "Andrea Silva",
                        "check_in": "2026-03-25",
                        "check_out": "2026-03-30",
                        "noches": 5
                    }
                }
            ]
        },
        "piso_2": {
            "habitaciones": [
                {
                    "numero": 201,
                    "tipo": "suite",
                    "precio_noche": 250,
                    "ocupada": False,
                    "servicios": ["wifi", "tv", "aire_acondicionado", "minibar", "jacuzzi", "vista_mar"]
                }
            ]
        }
    }
}

# Función para buscar habitaciones disponibles
def habitaciones_disponibles(hotel, tipo=None):
    disponibles = []
    for piso, info_piso in hotel["pisos"].items():
        for habitacion in info_piso["habitaciones"]:
            if not habitacion["ocupada"]:
                if tipo is None or habitacion["tipo"] == tipo:
                    disponibles.append({
                        "numero": habitacion["numero"],
                        "tipo": habitacion["tipo"],
                        "precio": habitacion["precio_noche"],
                        "piso": piso
                    })
    return disponibles

# Función para calcular ingresos actuales
def calcular_ingresos(hotel):
    ingresos = 0
    for piso, info_piso in hotel["pisos"].items():
        for habitacion in info_piso["habitaciones"]:
            if habitacion["ocupada"] and "huesped" in habitacion:
                ingresos += habitacion["precio_noche"] * habitacion["huesped"]["noches"]
    return ingresos

print(f"Hotel: {hotel['nombre']} ⭐ {hotel['estrellas']}")
print("\nHabitaciones disponibles:")
for hab in habitaciones_disponibles(hotel):
    print(f"  • Habitación {hab['numero']} ({hab['tipo']}) - ${hab['precio']}/noche")

print(f"\nIngresos por reservas actuales: ${calcular_ingresos(hotel)}")
print()

# ==============================================================================
# 31. RESUMEN Y REFERENCIA RÁPIDA
# ==============================================================================

print("=" * 80)
print("RESUMEN Y REFERENCIA RÁPIDA")
print("=" * 80)

resumen = """
📖 OPERACIONES BÁSICAS:
   • Crear: dict = {"clave": "valor"}
   • Acceder: dict["clave"] o dict.get("clave", default)
   • Agregar/Modificar: dict["nueva_clave"] = valor
   • Eliminar: del dict["clave"] o dict.pop("clave")
   • Verificar: "clave" in dict

📖 MÉTODOS IMPORTANTES:
   • .keys() - Obtiene todas las claves
   • .values() - Obtiene todos los valores
   • .items() - Obtiene pares (clave, valor)
   • .get(clave, default) - Acceso seguro
   • .update(otro_dict) - Combina diccionarios
   • .pop(clave) - Elimina y retorna valor
   • .clear() - Vacía el diccionario
   • .copy() - Copia superficial
   • .setdefault(clave, default) - Obtiene o inicializa

📖 ESTRUCTURAS ANIDADAS:
   • Dict → Dict: {"nivel1": {"nivel2": valor}}
   • Dict → List: {"clave": [1, 2, 3]}
   • List → Dict: [{"id": 1}, {"id": 2}]
   • Dict → List → Dict: {"categoria": [{"item": "valor"}]}
   • Acceso: dict["nivel1"]["nivel2"] o dict.get("nivel1", {}).get("nivel2")

📖 MEJORES PRÁCTICAS:
   • Usar .get() para evitar KeyError
   • Usar .items() para iterar eficientemente
   • Usar copy.deepcopy() para copias profundas
   • Verificar tipos con isinstance() en datos externos
   • Usar comprensión de diccionarios para transformaciones
   • No modificar diccionarios mientras se iteran

📖 MÓDULOS ÚTILES:
   • json - Serialización y deserialización
   • copy - Copias profundas (deepcopy)
   • collections - defaultdict, OrderedDict, Counter

📖 COMPLEJIDAD TEMPORAL:
   • Acceso: O(1) - Muy rápido
   • Inserción: O(1) - Muy rápido
   • Eliminación: O(1) - Muy rápido
   • Búsqueda de clave: O(1) - Muy rápido
   • Búsqueda de valor: O(n) - Requiere iterar
"""

print(resumen)
print()

# ==============================================================================
# 32. EJEMPLO FINAL: MINI PROYECTO - GESTOR DE TAREAS
# ==============================================================================

print("=" * 80)
print("PROYECTO FINAL: GESTOR DE TAREAS COMPLETO")
print("=" * 80)

"""
Sistema completo de gestión de tareas con proyectos, tareas, subtareas,
etiquetas, prioridades y asignaciones.
"""

gestor_tareas = {
    "proyectos": {
        "PROJ-001": {
            "nombre": "Desarrollo Web",
            "descripcion": "Crear sitio web corporativo",
            "estado": "en_progreso",
            "fecha_inicio": "2026-03-01",
            "fecha_limite": "2026-04-30",
            "equipo": [
                {
                    "id": "DEV-001",
                    "nombre": "Ana Martínez",
                    "rol": "Frontend Developer",
                    "email": "ana@company.com"
                },
                {
                    "id": "DEV-002",
                    "nombre": "Carlos López",
                    "rol": "Backend Developer",
                    "email": "carlos@company.com"
                }
            ],
            "tareas": [
                {
                    "id": "TASK-001",
                    "titulo": "Diseñar interfaz de usuario",
                    "descripcion": "Crear mockups y prototipos",
                    "prioridad": "alta",
                    "estado": "completada",
                    "asignado_a": "DEV-001",
                    "etiquetas": ["diseño", "ui", "frontend"],
                    "fecha_creacion": "2026-03-01",
                    "fecha_completado": "2026-03-10",
                    "subtareas": [
                        {"id": "SUB-001", "titulo": "Crear wireframes", "completada": True},
                        {"id": "SUB-002", "titulo": "Diseñar componentes", "completada": True},
                        {"id": "SUB-003", "titulo": "Prototipo interactivo", "completada": True}
                    ],
                    "comentarios": [
                        {
                            "autor": "DEV-002",
                            "fecha": "2026-03-05",
                            "texto": "Los mockups se ven geniales"
                        }
                    ]
                },
                {
                    "id": "TASK-002",
                    "titulo": "Implementar API REST",
                    "descripcion": "Crear endpoints para el backend",
                    "prioridad": "alta",
                    "estado": "en_progreso",
                    "asignado_a": "DEV-002",
                    "etiquetas": ["backend", "api", "desarrollo"],
                    "fecha_creacion": "2026-03-05",
                    "fecha_completado": None,
                    "subtareas": [
                        {"id": "SUB-004", "titulo": "Configurar servidor", "completada": True},
                        {"id": "SUB-005", "titulo": "Crear modelos de datos", "completada": True},
                        {"id": "SUB-006", "titulo": "Implementar endpoints", "completada": False},
                        {"id": "SUB-007", "titulo": "Escribir tests", "completada": False}
                    ],
                    "comentarios": [
                        {
                            "autor": "DEV-001",
                            "fecha": "2026-03-20",
                            "texto": "¿Cuándo estará lista la API de usuarios?"
                        },
                        {
                            "autor": "DEV-002",
                            "fecha": "2026-03-21",
                            "texto": "Estará lista esta semana"
                        }
                    ]
                },
                {
                    "id": "TASK-003",
                    "titulo": "Integrar frontend con backend",
                    "descripcion": "Conectar la UI con la API",
                    "prioridad": "media",
                    "estado": "pendiente",
                    "asignado_a": "DEV-001",
                    "etiquetas": ["integracion", "frontend", "backend"],
                    "fecha_creacion": "2026-03-15",
                    "fecha_completado": None,
                    "subtareas": [],
                    "comentarios": []
                }
            ]
        },
        "PROJ-002": {
            "nombre": "Aplicación Móvil",
            "descripcion": "App para iOS y Android",
            "estado": "planificacion",
            "fecha_inicio": "2026-04-01",
            "fecha_limite": "2026-06-30",
            "equipo": [
                {
                    "id": "DEV-003",
                    "nombre": "Laura Sánchez",
                    "rol": "Mobile Developer",
                    "email": "laura@company.com"
                }
            ],
            "tareas": []
        }
    }
}


# FUNCIÓN 1: Mostrar resumen de proyectos
def mostrar_resumen_proyectos(gestor):
    print("📊 RESUMEN DE PROYECTOS:\n")
    for id_proyecto, proyecto in gestor["proyectos"].items():
        print(f"🎯 {proyecto['nombre']} ({id_proyecto})")
        print(f"   Estado: {proyecto['estado']}")
        print(f"   Equipo: {len(proyecto['equipo'])} miembros")
        print(f"   Tareas: {len(proyecto['tareas'])}")
        
        if proyecto["tareas"]:
            completadas = sum(1 for t in proyecto["tareas"] if t["estado"] == "completada")
            print(f"   Progreso: {completadas}/{len(proyecto['tareas'])} tareas completadas")
        print()

mostrar_resumen_proyectos(gestor_tareas)

# FUNCIÓN 2: Obtener tareas por prioridad
def tareas_por_prioridad(gestor, prioridad):
    tareas_filtradas = []
    for proyecto in gestor["proyectos"].values():
        for tarea in proyecto["tareas"]:
            if tarea["prioridad"] == prioridad:
                tareas_filtradas.append({
                    "proyecto": proyecto["nombre"],
                    "tarea": tarea["titulo"],
                    "asignado": tarea["asignado_a"],
                    "estado": tarea["estado"]
                })
    return tareas_filtradas

print("🔴 TAREAS DE ALTA PRIORIDAD:")
for tarea in tareas_por_prioridad(gestor_tareas, "alta"):
    print(f"  • [{tarea['estado']}] {tarea['tarea']}")
    print(f"    Proyecto: {tarea['proyecto']}, Asignado a: {tarea['asignado']}")
print()


# FUNCIÓN 3: Calcular progreso de subtareas
def progreso_subtareas(tarea):
    if not tarea["subtareas"]:
        return 0
    
    completadas = sum(1 for sub in tarea["subtareas"] if sub["completada"])
    total = len(tarea["subtareas"])
    porcentaje = (completadas / total) * 100
    
    return porcentaje

print("📈 PROGRESO DE TAREAS CON SUBTAREAS:")
for proyecto in gestor_tareas["proyectos"].values():
    for tarea in proyecto["tareas"]:
        if tarea["subtareas"]:
            progreso = progreso_subtareas(tarea)
            print(f"  • {tarea['titulo']}: {progreso:.0f}% completado")
            print(f"    Subtareas: {sum(1 for s in tarea['subtareas'] if s['completada'])}/{len(tarea['subtareas'])}")
print()


# FUNCIÓN 4: Agregar comentario a una tarea
def agregar_comentario(gestor, id_proyecto, id_tarea, autor, texto):
    proyecto = gestor["proyectos"].get(id_proyecto)
    if not proyecto:
        return False
    
    for tarea in proyecto["tareas"]:
        if tarea["id"] == id_tarea:
            from datetime import datetime
            tarea["comentarios"].append({
                "autor": autor,
                "fecha": datetime.now().strftime("%Y-%m-%d"),
                "texto": texto
            })
            return True
    
    return False

# Agregar un comentario
agregar_comentario(gestor_tareas, "PROJ-001", "TASK-002", "DEV-001", "Necesito acceso a la base de datos")
print("✓ Comentario agregado a TASK-002")
print()


# FUNCIÓN 5: Generar reporte completo
def generar_reporte_completo(gestor):
    print("=" * 80)
    print("REPORTE COMPLETO DEL GESTOR DE TAREAS")
    print("=" * 80)
    
    for id_proyecto, proyecto in gestor["proyectos"].items():
        print(f"\n🎯 PROYECTO: {proyecto['nombre']} ({id_proyecto})")
        print(f"   📝 {proyecto['descripcion']}")
        print(f"   📅 {proyecto['fecha_inicio']} → {proyecto['fecha_limite']}")
        print(f"   📊 Estado: {proyecto['estado'].upper()}")
        
        print(f"\n   👥 EQUIPO ({len(proyecto['equipo'])} miembros):")
        for miembro in proyecto["equipo"]:
            print(f"      • {miembro['nombre']} - {miembro['rol']}")
        
        if proyecto["tareas"]:
            print(f"\n   ✅ TAREAS ({len(proyecto['tareas'])}):")
            for tarea in proyecto["tareas"]:
                icono_estado = "✓" if tarea["estado"] == "completada" else "⏳" if tarea["estado"] == "en_progreso" else "○"
                icono_prioridad = "🔴" if tarea["prioridad"] == "alta" else "🟡" if tarea["prioridad"] == "media" else "🟢"
                
                print(f"\n      {icono_estado} {icono_prioridad} {tarea['titulo']} ({tarea['id']})")
                print(f"         Estado: {tarea['estado']} | Prioridad: {tarea['prioridad']}")
                print(f"         Asignado a: {tarea['asignado_a']}")
                print(f"         Etiquetas: {', '.join(tarea['etiquetas'])}")
                
                if tarea["subtareas"]:
                    progreso = progreso_subtareas(tarea)
                    print(f"         Subtareas: {progreso:.0f}% completado")
                    for subtarea in tarea["subtareas"]:
                        check = "☑" if subtarea["completada"] else "☐"
                        print(f"            {check} {subtarea['titulo']}")
                
                if tarea["comentarios"]:
                    print(f"         💬 {len(tarea['comentarios'])} comentarios")
        else:
            print(f"\n   ℹ️ No hay tareas creadas aún")
        
        print("\n" + "─" * 80)

generar_reporte_completo(gestor_tareas)

# ==============================================================================
# 33. CONCLUSIÓN
# ==============================================================================

print("\n" + "=" * 80)
print("CONCLUSIÓN")
print("=" * 80)

conclusion = """
🎓 ¡FELICIDADES! Has completado la guía completa de diccionarios en Python.

Ahora sabes:
✓ Qué son los diccionarios y cómo crearlos
✓ Todas las operaciones básicas (crear, leer, actualizar, eliminar)
✓ Cómo trabajar con diccionarios anidados de múltiples niveles
✓ Cómo combinar diccionarios con listas
✓ Cómo navegar estructuras complejas
✓ Funciones útiles para trabajar con datos anidados
✓ Mejores prácticas y errores comunes
✓ Casos de uso reales y prácticos

💡 PRÓXIMOS PASOS:
   • Practica creando tus propias estructuras de datos
   • Experimenta con APIs reales que devuelven JSON
   • Crea proyectos pequeños usando diccionarios
   • Explora módulos como collections para estructuras avanzadas

🚀 Los diccionarios son una de las estructuras más poderosas y versátiles
   de Python. ¡Dominarlos te hará un mejor programador!

📚 Para más información:
   • Documentación oficial: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
   • PEP 584: https://www.python.org/dev/peps/pep-0584/ (Operadores | y |=)
"""

print(conclusion)
print("=" * 80)
print("FIN DE LA GUÍA")
print("=" * 80)
