"""
================================================================================
PASO 3: CÓMO PYTHON COMPARA VALORES INTERNAMENTE
================================================================================

Entender la comparación es CLAVE para dominar el sorting.
Python usa los operadores < y > para decidir el orden.

"""

# =============================================================================
# 3.1 - Comparación de números
# =============================================================================

"""
Los números se comparan por su valor matemático.
Esto es intuitivo.
"""

print("=== Comparación de Números ===")
print(f"1 < 5: {1 < 5}")       # True
print(f"10 < 5: {10 < 5}")     # False
print(f"-3 < 0: {-3 < 0}")     # True
print(f"3.14 < 4: {3.14 < 4}")  # True
print()

# =============================================================================
# 3.2 - Comparación de Strings (MUY IMPORTANTE)
# =============================================================================

"""
Los strings se comparan CARÁCTER POR CARÁCTER usando su valor ASCII/Unicode.

Tabla ASCII relevante:
    '0'-'9': 48-57
    'A'-'Z': 65-90
    'a'-'z': 97-122

¡Por eso 'Apple' < 'banana'! Porque 'A' (65) < 'b' (98)
"""

print("=== Comparación de Strings ===")

# Comparación carácter por carácter
print(f"'apple' < 'banana': {'apple' < 'banana'}")  # True ('a' < 'b')
print(f"'apple' < 'apricot': {'apple' < 'apricot'}")  # True ('l' < 'r')
print(f"'apple' < 'Apple': {'apple' < 'Apple'}")  # False ('a'=97 > 'A'=65)

# Ver valores ASCII
print(f"\nValores ASCII:")
print(f"ord('A') = {ord('A')}")  # 65
print(f"ord('Z') = {ord('Z')}")  # 90
print(f"ord('a') = {ord('a')}")  # 97
print(f"ord('z') = {ord('z')}")  # 122
print(f"ord('0') = {ord('0')}")  # 48
print(f"ord('9') = {ord('9')}")  # 57
print()

# Cómo Python compara "apple" vs "apricot"
"""
Paso 1: 'a' vs 'a' -> iguales, siguiente
Paso 2: 'p' vs 'p' -> iguales, siguiente
Paso 3: 'p' vs 'r' -> 'p' (112) < 'r' (114) -> "apple" < "apricot"
"""

# =============================================================================
# 3.3 - Comparación de Listas y Tuplas (LEXICOGRÁFICA)
# =============================================================================

"""
Las listas y tuplas se comparan ELEMENTO POR ELEMENTO (orden lexicográfico).
Esto es CRUCIAL para el sorting multi-criterio.

Reglas:
1. Compara el primer elemento
2. Si son iguales, compara el segundo
3. Si son iguales, compara el tercero
4. ... y así sucesivamente
5. Si una lista es prefijo de otra, la más corta es "menor"
"""

print("=== Comparación de Listas/Tuplas ===")

# Ejemplo 1: Primer elemento decide
# True (1 < 2, no mira el resto)
print(f"[1, 100] < [2, 0]: {[1, 100] < [2, 0]}")

# Ejemplo 2: Primer elemento igual, segundo decide
print(f"[1, 2] < [1, 3]: {[1, 2] < [1, 3]}")  # True (1==1, luego 2 < 3)

# Ejemplo 3: Dos primeros iguales, tercero decide
print(f"[1, 2, 3] < [1, 2, 4]: {[1, 2, 3] < [1, 2, 4]}")  # True

# Ejemplo 4: Lista más corta es "menor" si es prefijo
print(f"[1, 2] < [1, 2, 3]: {[1, 2] < [1, 2, 3]}")  # True

# Lo mismo aplica para tuplas
print(f"(1, 2) < (1, 3): {(1, 2) < (1, 3)}")  # True
print()

# =============================================================================
# 3.4 - VISUALIZACIÓN: Cómo se comparan tuplas paso a paso
# =============================================================================

"""
Comparemos (2, 'apple') vs (2, 'banana') vs (1, 'zebra')

Paso 1: Comparar primer elemento
    - (2, ...) vs (2, ...) -> iguales, ir al segundo
    - (2, ...) vs (1, ...) -> 2 > 1, entonces (1, 'zebra') es MENOR

Paso 2: Para los que tienen primer elemento igual, comparar segundo
    - (2, 'apple') vs (2, 'banana') -> 'apple' < 'banana'

Orden final: (1, 'zebra'), (2, 'apple'), (2, 'banana')
"""

tuplas = [(2, 'apple'), (2, 'banana'), (1, 'zebra')]
print("=== Ordenando tuplas ===")
print(f"Original: {tuplas}")
print(f"Ordenado: {sorted(tuplas)}")
# [(1, 'zebra'), (2, 'apple'), (2, 'banana')]
print()

# =============================================================================
# 3.5 - ¿Por qué es TAN importante entender la comparación de tuplas?
# =============================================================================

"""
¡PORQUE ES LA CLAVE PARA ORDENAR POR MÚLTIPLES CRITERIOS!

Si tu función key retorna una TUPLA, Python ordenará por:
1. Primer elemento de la tupla
2. Si hay empate, segundo elemento
3. Si hay empate, tercero
4. ... etc
"""

# Ejemplo: Ordenar jugadores por puntaje (desc) y nombre (asc)
jugadores = [
    {"nombre": "Ana", "puntaje": 100},
    {"nombre": "Bob", "puntaje": 100},
    {"nombre": "Carlos", "puntaje": 90},
    {"nombre": "Diana", "puntaje": 100},
]


def key_jugador(j):
    # Negativo para orden descendente de puntaje
    # El nombre queda ascendente
    return (-j["puntaje"], j["nombre"])


ordenados = sorted(jugadores, key=key_jugador)
print("=== Jugadores ordenados (puntaje desc, nombre asc) ===")
for j in ordenados:
    print(f"  {j['nombre']}: {j['puntaje']}")
# Ana: 100, Bob: 100, Diana: 100, Carlos: 90
print()

# =============================================================================
# 3.6 - El truco del NEGATIVO para orden descendente
# =============================================================================

"""
Problema: sorted() ordena ascendente por defecto.
¿Cómo ordenas UN criterio descendente y otro ascendente?

reverse=True afecta a TODO, no puedes usarlo selectivamente.

SOLUCIÓN: Negar los valores numéricos que quieres descendentes.

    sorted(lista, key=lambda x: (-x["puntaje"], x["nombre"]))

    -100 < -90  (porque -100 es "más negativo")

    Entonces los puntajes altos (100 -> -100) quedan primero.
"""

# Demostración
print("=== Truco del negativo ===")
puntajes = [100, 90, 100, 80]
print(f"Ascendente: {sorted(puntajes)}")           # [80, 90, 100, 100]
print(f"Descendente: {sorted(puntajes, reverse=True)}")  # [100, 100, 90, 80]

# Usando negativo en key
# [100, 100, 90, 80]
print(f"Con key negativo: {sorted(puntajes, key=lambda x: -x)}")
print()

# =============================================================================
# 3.7 - EJERCICIO MENTAL: Predice el orden
# =============================================================================

"""
¿Cuál será el resultado de ordenar estas tuplas?

datos = [
    (2, 'b', 10),
    (1, 'a', 20),
    (2, 'a', 30),
    (1, 'b', 40),
]

Piensa antes de ver la respuesta...
"""

datos = [
    (2, 'b', 10),
    (1, 'a', 20),
    (2, 'a', 30),
    (1, 'b', 40),
]

print("=== Ejercicio: Ordenar tuplas ===")
print(f"Resultado: {sorted(datos)}")
# [(1, 'a', 20), (1, 'b', 40), (2, 'a', 30), (2, 'b', 10)]

"""
Explicación:
1. Primero por elemento 0: los que tienen 1 van antes que los que tienen 2
2. Entre los que tienen 1: (1, 'a', ...) < (1, 'b', ...) porque 'a' < 'b'
3. Entre los que tienen 2: (2, 'a', ...) < (2, 'b', ...) porque 'a' < 'b'
"""
print()

# =============================================================================
# RESUMEN PASO 3
# =============================================================================

"""
PUNTOS CLAVE:

1. Números: Comparación matemática normal
2. Strings: Carácter por carácter usando ASCII ('A' < 'a')
3. Listas/Tuplas: Elemento por elemento (lexicográfico)
4. La comparación de tuplas es la BASE del sorting multi-criterio
5. Truco del NEGATIVO: -valor para ordenar números descendente
6. La función key puede retornar una TUPLA para múltiples criterios

ESTE ES EL CONCEPTO MÁS IMPORTANTE:
    key=lambda x: (criterio1, criterio2, criterio3)

    Python ordenará por criterio1, luego por criterio2 en empates, etc.

PRÓXIMO PASO: Lambda functions - escribir keys de forma concisa
"""
