"""
================================================================================
PASO 5: SORTING MULTI-CRITERIO - DOMINIO TOTAL
================================================================================

Este es el paso donde todo se une.
Aprenderás a ordenar por múltiples criterios en UN solo sort().

"""

# =============================================================================
# 5.1 - El Problema del Doble Sort
# =============================================================================

"""
PROBLEMA COMÚN: Ordenar por múltiples criterios usando múltiples sorts.

Ejemplo: Ordenar empleados por departamento y luego por salario.

FORMA INCORRECTA (lo que muchos hacen):
    empleados.sort(key=lambda x: x["departamento"])
    empleados.sort(key=lambda x: x["salario"])  # ¡ESTO ROMPE EL ORDEN ANTERIOR!

El segundo sort() DESTRUYE el orden del primero.
"""

empleados = [
    {"nombre": "Ana", "depto": "Ventas", "salario": 50000},
    {"nombre": "Bob", "depto": "IT", "salario": 60000},
    {"nombre": "Carlos", "depto": "Ventas", "salario": 45000},
    {"nombre": "Diana", "depto": "IT", "salario": 55000},
]

# FORMA INCORRECTA
copia1 = empleados.copy()
copia1.sort(key=lambda x: x["depto"])
copia1.sort(key=lambda x: x["salario"])  # ¡Rompe el orden por depto!

print("=== Doble sort INCORRECTO ===")
for e in copia1:
    print(f"  {e['nombre']}: {e['depto']}, ${e['salario']}")
# Carlos: Ventas, $45000
# Ana: Ventas, $50000
# Diana: IT, $55000
# Bob: IT, $60000
# ¡Los departamentos quedaron mezclados!
print()

# =============================================================================
# 5.2 - La Solución: Tuplas en key
# =============================================================================

"""
FORMA CORRECTA: Una sola key que retorna una tupla.

    key=lambda x: (criterio1, criterio2, criterio3)

Python compara tuplas elemento por elemento, así que:
1. Primero ordena por criterio1
2. Si hay empate en criterio1, ordena por criterio2
3. Si hay empate en criterio2, ordena por criterio3
4. ...etc
"""

# FORMA CORRECTA - Un solo sort con tupla
copia2 = empleados.copy()
copia2.sort(key=lambda x: (x["depto"], x["salario"]))

print("=== Un solo sort CORRECTO ===")
for e in copia2:
    print(f"  {e['nombre']}: {e['depto']}, ${e['salario']}")
# Diana: IT, $55000
# Bob: IT, $60000
# Carlos: Ventas, $45000
# Ana: Ventas, $50000
# ¡Primero por departamento, luego por salario dentro de cada depto!
print()

# =============================================================================
# 5.3 - Mezclando Ascendente y Descendente
# =============================================================================

"""
PROBLEMA: ¿Qué pasa si quieres:
    - Departamento: Ascendente (A-Z)
    - Salario: Descendente (mayor primero)

reverse=True afecta a TODO, no puedes usarlo selectivamente.

SOLUCIÓN: Negar los valores numéricos que quieres descendentes.

    key=lambda x: (x["depto"], -x["salario"])
                               ^
                               Negativo = descendente
"""

copia3 = empleados.copy()
copia3.sort(key=lambda x: (x["depto"], -x["salario"]))

print("=== Depto ASC, Salario DESC ===")
for e in copia3:
    print(f"  {e['nombre']}: {e['depto']}, ${e['salario']}")
# Bob: IT, $60000       (IT primero, salario alto primero)
# Diana: IT, $55000
# Ana: Ventas, $50000   (Ventas después, salario alto primero)
# Carlos: Ventas, $45000
print()

# =============================================================================
# 5.4 - ¿Qué pasa con strings descendentes?
# =============================================================================

"""
No puedes negar un string: -"texto" da error.

SOLUCIONES:

1. Si solo strings: usar reverse=True
2. Si mezcla: hacer dos sorts (pero en orden inverso!)
3. Usar una función auxiliar para "invertir" strings
"""

# Solución 2: Doble sort en ORDEN INVERSO (el truco del stable sort)
# Si quieres: Primario DESC, Secundario ASC
# Hazlo al revés: Primero ordenas por secundario, luego por primario con reverse

datos = [
    {"categoria": "B", "nombre": "Zebra"},
    {"categoria": "A", "nombre": "Apple"},
    {"categoria": "B", "nombre": "Mango"},
    {"categoria": "A", "nombre": "Banana"},
]

# Queremos: categoria DESC (Z antes que A), nombre ASC
# Paso 1: Ordenar por nombre ASC
datos.sort(key=lambda x: x["nombre"])
# Paso 2: Ordenar por categoria DESC (reverse=True)
# Python tiene "stable sort" - mantiene orden relativo de elementos iguales
datos.sort(key=lambda x: x["categoria"], reverse=True)

print("=== Categoria DESC, Nombre ASC (doble sort inverso) ===")
for d in datos:
    print(f"  {d['categoria']}: {d['nombre']}")
# B: Mango
# B: Zebra
# A: Apple
# A: Banana

# =============================================================================
# 5.5 - Patrón General para Multi-Criterio
# =============================================================================

"""
PATRÓN UNIVERSAL:

    sorted(lista, key=lambda x: (
        criterio1(x),      # Primer criterio
        criterio2(x),      # Segundo criterio (desempate)
        criterio3(x),      # Tercer criterio (desempate)
        ...
    ))

PARA DESCENDENTE:
    - Números: usar negativo (-valor)
    - Strings: usar doble sort con stable sort, o reverse=True si es el único criterio

EJEMPLO COMPLETO:

    sorted(productos, key=lambda p: (
        -p["ventas"],           # Más ventas primero (DESC)
        p["categoria"],         # Alfabético por categoría (ASC)
        -p["rating"],           # Mejor rating primero (DESC)
        p["nombre"].lower()     # Alfabético ignorando mayúsculas (ASC)
    ))
"""

# Ejemplo completo
productos = [
    {"nombre": "iPhone", "categoria": "Tech", "ventas": 1000, "rating": 4.5},
    {"nombre": "Galaxy", "categoria": "Tech", "ventas": 1000, "rating": 4.3},
    {"nombre": "Laptop", "categoria": "Tech", "ventas": 500, "rating": 4.8},
    {"nombre": "Mesa", "categoria": "Hogar", "ventas": 200, "rating": 4.0},
    {"nombre": "Silla", "categoria": "Hogar", "ventas": 200, "rating": 4.5},
]

ordenados = sorted(productos, key=lambda p: (
    p["categoria"],         # Categoría ASC
    -p["ventas"],           # Ventas DESC
    -p["rating"],           # Rating DESC
    p["nombre"].lower()     # Nombre ASC
))

print("=== Productos ordenados (4 criterios) ===")
for p in ordenados:
    print(f"  {p['categoria']:6} | {p['nombre']:8} | ventas={p['ventas']:4} | rating={p['rating']}")
print()

# =============================================================================
# RESUMEN PASO 5
# =============================================================================

"""
PUNTOS CLAVE:

1. NUNCA uses múltiples sort() para multi-criterio (el segundo rompe el primero)

2. USA TUPLAS en key:
    key=lambda x: (criterio1, criterio2, criterio3)

3. Para DESCENDENTE numérico: usa negativo
    key=lambda x: (-x["valor"], x["nombre"])

4. Python compara tuplas elemento por elemento

5. El resultado es UN SOLO SORT que ordena correctamente por todos los criterios

PRÓXIMO PASO: Aplicar todo esto para refactorizar tu código del juego de cartas
"""
