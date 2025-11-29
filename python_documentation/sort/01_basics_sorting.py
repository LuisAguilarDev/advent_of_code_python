"""
================================================================================
PASO 1: FUNDAMENTOS DEL SORTING EN PYTHON
================================================================================

Python tiene dos formas principales de ordenar:
1. sorted() - Función que RETORNA una nueva lista ordenada (no modifica la original)
2. list.sort() - Método que MODIFICA la lista in-place (no retorna nada útil)

"""

# =============================================================================
# 1.1 - sorted() vs .sort()
# =============================================================================

# sorted() - Crea una NUEVA lista, la original no cambia
numeros_original = [3, 1, 4, 1, 5, 9, 2, 6]
numeros_ordenados = sorted(numeros_original)

print("=== sorted() ===")
print(f"Original:  {numeros_original}")    # [3, 1, 4, 1, 5, 9, 2, 6] - NO CAMBIÓ
print(f"Ordenada:  {numeros_ordenados}")   # [1, 1, 2, 3, 4, 5, 6, 9]
print()

# .sort() - Modifica la lista DIRECTAMENTE, retorna None
numeros = [3, 1, 4, 1, 5, 9, 2, 6]
resultado = numeros.sort()  # Retorna None!

print("=== .sort() ===")
print(f"Lista después de .sort(): {numeros}")  # [1, 1, 2, 3, 4, 5, 6, 9]
print(f"Valor retornado: {resultado}")          # None
print()

# =============================================================================
# 1.2 - Orden ascendente vs descendente
# =============================================================================

numeros = [3, 1, 4, 1, 5, 9, 2, 6]

# Ascendente (por defecto)
ascendente = sorted(numeros)
print(f"Ascendente:  {ascendente}")   # [1, 1, 2, 3, 4, 5, 6, 9]

# Descendente - usar reverse=True
descendente = sorted(numeros, reverse=True)
print(f"Descendente: {descendente}")  # [9, 6, 5, 4, 3, 2, 1, 1]
print()

# =============================================================================
# 1.3 - ¿Qué tipos de datos se pueden ordenar?
# =============================================================================

# Números - Se ordenan por valor numérico
print("Números:", sorted([3.14, 1, 2.5, 0, -1]))  # [-1, 0, 1, 2.5, 3.14]

# Strings - Se ordenan ALFABÉTICAMENTE (por código ASCII/Unicode)
print("Strings:", sorted(["banana", "Apple", "cherry"]))  # ['Apple', 'banana', 'cherry']
# ¡OJO! Las mayúsculas van ANTES que las minúsculas (A=65, a=97 en ASCII)

# Listas - Se comparan elemento por elemento
print("Listas:", sorted([[1, 2], [1, 1], [2, 0]]))  # [[1, 1], [1, 2], [2, 0]]

# Tuplas - Igual que las listas
print("Tuplas:", sorted([(1, 2), (1, 1), (2, 0)]))  # [(1, 1), (1, 2), (2, 0)]
print()

# =============================================================================
# 1.4 - ERROR COMÚN: No puedes mezclar tipos incompatibles
# =============================================================================

# Esto da ERROR en Python 3:
# sorted([1, "dos", 3])  # TypeError: '<' not supported between 'str' and 'int'

# Python no sabe cómo comparar un número con un string
print()

# =============================================================================
# 1.5 - ¿Cómo decide Python el orden?
# =============================================================================

"""
Python usa los operadores de comparación: <, >, ==

Internamente, cuando ordenas [3, 1, 2], Python hace comparaciones como:
- ¿1 < 3? Sí -> 1 va antes que 3
- ¿2 < 3? Sí -> 2 va antes que 3
- ¿2 < 1? No -> 2 va después de 1

Resultado: [1, 2, 3]

Para strings:
- "apple" < "banana" -> True (porque 'a' < 'b' en ASCII)
- "Apple" < "apple" -> True (porque 'A'=65 < 'a'=97 en ASCII)
"""

# Puedes probar las comparaciones manualmente:
print("=== Comparaciones ===")
print(f"1 < 3: {1 < 3}")              # True
print(f"'apple' < 'banana': {'apple' < 'banana'}")  # True
print(f"'Apple' < 'apple': {'Apple' < 'apple'}")    # True (mayúscula < minúscula)
print(f"[1, 2] < [1, 3]: {[1, 2] < [1, 3]}")        # True (compara elemento por elemento)
print(f"[1, 2] < [2, 0]: {[1, 2] < [2, 0]}")        # True (1 < 2, no mira el segundo)
print()

# =============================================================================
# RESUMEN PASO 1
# =============================================================================

"""
PUNTOS CLAVE:

1. sorted(lista) -> Retorna nueva lista ordenada, original intacta
2. lista.sort()  -> Modifica la lista, retorna None
3. reverse=True  -> Orden descendente
4. Python compara usando <, >, ==
5. Los tipos deben ser comparables entre sí
6. Strings se ordenan por ASCII (mayúsculas antes que minúsculas)
7. Listas/Tuplas se comparan elemento por elemento

PRÓXIMO PASO: El parámetro 'key' - el secreto para ordenar como quieras
"""
