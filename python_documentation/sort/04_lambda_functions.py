"""
================================================================================
PASO 4: LAMBDA FUNCTIONS - FUNCIONES ANÓNIMAS PARA SORTING
================================================================================

Las lambdas son funciones pequeñas de una línea, perfectas para 'key'.
Son la forma más común y concisa de definir funciones de ordenamiento.

"""

# =============================================================================
# 4.1 - ¿Qué es una Lambda?
# =============================================================================

"""
Una lambda es una función ANÓNIMA (sin nombre) de UNA sola expresión.

Sintaxis:
    lambda parametros: expresion_que_retorna

Equivale a:
    def funcion(parametros):
        return expresion_que_retorna
"""

# Función normal
def duplicar(x):
    return x * 2

# Lambda equivalente
duplicar_lambda = lambda x: x * 2

print("=== Lambda básica ===")
print(f"Función normal: duplicar(5) = {duplicar(5)}")
print(f"Lambda: duplicar_lambda(5) = {duplicar_lambda(5)}")
print()

# =============================================================================
# 4.2 - Lambdas con múltiples parámetros
# =============================================================================

# Un parámetro
cuadrado = lambda x: x ** 2

# Dos parámetros
suma = lambda x, y: x + y

# Tres parámetros
promedio = lambda a, b, c: (a + b + c) / 3

print("=== Lambdas con múltiples parámetros ===")
print(f"cuadrado(4) = {cuadrado(4)}")        # 16
print(f"suma(3, 5) = {suma(3, 5)}")          # 8
print(f"promedio(10, 20, 30) = {promedio(10, 20, 30)}")  # 20.0
print()

# =============================================================================
# 4.3 - Lambdas en Sorting - Casos comunes
# =============================================================================

# CASO 1: Ordenar por un atributo de diccionario
personas = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Bob", "edad": 30},
    {"nombre": "Carlos", "edad": 20}
]

# Forma larga
def obtener_edad(p):
    return p["edad"]
por_edad_v1 = sorted(personas, key=obtener_edad)

# Forma corta con lambda
por_edad_v2 = sorted(personas, key=lambda p: p["edad"])

print("=== Ordenar diccionarios ===")
print("Por edad:", [p["nombre"] for p in por_edad_v2])
# ['Carlos', 'Ana', 'Bob']

# CASO 2: Ordenar por segundo elemento de tupla
tuplas = [("a", 3), ("b", 1), ("c", 2)]
por_segundo = sorted(tuplas, key=lambda t: t[1])
print("Por segundo elemento:", por_segundo)
# [('b', 1), ('c', 2), ('a', 3)]

# CASO 3: Ordenar strings por longitud
palabras = ["python", "es", "genial"]
por_longitud = sorted(palabras, key=lambda s: len(s))
print("Por longitud:", por_longitud)
# ['es', 'genial', 'python'] - Oops, 'genial' y 'python' tienen 6 letras
# Arreglemos: ordenar por longitud, y si empatan, alfabéticamente
por_longitud_alfa = sorted(palabras, key=lambda s: (len(s), s))
print("Por longitud y alfabético:", por_longitud_alfa)
# ['es', 'genial', 'python']

# =============================================================================
# 4.4 - Lambdas que retornan Tuplas (MULTI-CRITERIO)
# =============================================================================

"""
ESTE ES EL PATRÓN MÁS PODEROSO:

    key=lambda x: (criterio1, criterio2, criterio3)

Python ordenará por criterio1, luego criterio2 en empates, etc.
"""

estudiantes = [
    {"nombre": "Ana", "nota": 90, "edad": 20},
    {"nombre": "Bob", "nota": 85, "edad": 22},
    {"nombre": "Carlos", "nota": 90, "edad": 19},
    {"nombre": "Diana", "nota": 85, "edad": 22},
]

# Ordenar por nota (desc), luego edad (asc), luego nombre (asc)
ordenados = sorted(estudiantes, key=lambda e: (-e["nota"], e["edad"], e["nombre"]))

print("=== Multi-criterio con lambda ===")
print("Ordenados por nota(desc), edad(asc), nombre(asc):")
for e in ordenados:
    print(f"  {e['nombre']}: nota={e['nota']}, edad={e['edad']}")
# Carlos: nota=90, edad=19  (nota alta, más joven)
# Ana: nota=90, edad=20     (nota alta, segundo más joven)
# Bob: nota=85, edad=22     (nota=85, mismo edad que Diana, 'Bob' < 'Diana')
# Diana: nota=85, edad=22

# =============================================================================
# 4.5 - Lambdas con operaciones más complejas
# =============================================================================

# Puedes hacer cualquier operación en una lambda, siempre que sea UNA expresión

# Ordenar por última letra
palabras = ["hola", "mundo", "python"]
por_ultima = sorted(palabras, key=lambda s: s[-1])
print("Por última letra:", por_ultima)
# ['hola', 'mundo', 'python'] -> 'a', 'o', 'n' -> ['hola', 'python', 'mundo']
# Oops, 'n' < 'o' < 'a' en ASCII... veamos
print("Última letra de cada palabra:", [s[-1] for s in palabras])
# ['a', 'o', 'n'] -> ordenado: 'a', 'n', 'o' -> ['hola', 'python', 'mundo']

# Ordenar números por su representación como string (orden "alfabético")
numeros = [1, 10, 2, 20, 100]
como_string = sorted(numeros, key=lambda n: str(n))
print("Números ordenados como strings:", como_string)
# [1, 10, 100, 2, 20] - porque "1" < "10" < "100" < "2" < "20"

# Ordenar por la suma de dígitos
numeros = [123, 45, 6, 789]
por_suma_digitos = sorted(numeros, key=lambda n: sum(int(d) for d in str(n)))
print("Por suma de dígitos:", por_suma_digitos)
# 6->6, 45->9, 123->6, 789->24 ... ordenado: [6, 123, 45, 789]

# =============================================================================
# 4.6 - Lambda vs Función: ¿Cuándo usar cuál?
# =============================================================================

"""
USA LAMBDA CUANDO:
- La lógica es simple (una línea)
- Solo la usas una vez
- Es más legible en línea

USA FUNCIÓN NORMAL CUANDO:
- La lógica es compleja
- Necesitas múltiples líneas
- La reutilizarás en varios lugares
- Necesitas un nombre descriptivo para claridad
"""

# Ejemplo donde lambda es mejor
sorted(personas, key=lambda p: p["edad"])  # Claro y conciso

# Ejemplo donde función normal es mejor
def calcular_prioridad_compleja(tarea):
    """Calcula prioridad basada en múltiples factores"""
    base = tarea["urgencia"] * 10
    if tarea["tipo"] == "bug":
        base += 50
    if tarea["cliente_vip"]:
        base += 30
    return base

# Es más legible que una lambda gigante
# sorted(tareas, key=calcular_prioridad_compleja)

# =============================================================================
# 4.7 - Errores comunes con Lambdas
# =============================================================================

# ERROR 1: Olvidar que lambda retorna automáticamente
# MAL:  lambda x: return x * 2  # SyntaxError
# BIEN: lambda x: x * 2

# ERROR 2: Intentar múltiples statements
# MAL:  lambda x: y = x * 2; y + 1  # SyntaxError
# BIEN: lambda x: (x * 2) + 1

# ERROR 3: Olvidar paréntesis en tuplas
# MAL:  sorted(lista, key=lambda x: x[0], x[1])  # SyntaxError
# BIEN: sorted(lista, key=lambda x: (x[0], x[1]))

print("=== Errores comunes evitados ===")
# Tupla correcta
datos = [(1, 'b'), (2, 'a'), (1, 'a')]
print("Correcto:", sorted(datos, key=lambda x: (x[0], x[1])))
# [(1, 'a'), (1, 'b'), (2, 'a')]
print()

# =============================================================================
# RESUMEN PASO 4
# =============================================================================

"""
PUNTOS CLAVE:

1. Lambda: función anónima de una línea
2. Sintaxis: lambda parametros: expresion
3. NO uses 'return' en lambda (retorna automáticamente)
4. Usa paréntesis para retornar tuplas: lambda x: (a, b, c)
5. Lambda es perfecta para keys simples
6. Función normal para lógica compleja

PATRONES MÁS ÚTILES:

    # Por atributo de diccionario
    key=lambda x: x["campo"]

    # Por índice de tupla/lista
    key=lambda x: x[indice]

    # Multi-criterio
    key=lambda x: (criterio1, criterio2)

    # Descendente numérico
    key=lambda x: -x["valor"]

    # Combinado
    key=lambda x: (-x["prioridad"], x["nombre"])

PRÓXIMO PASO: Dominar el sorting multi-criterio con ejemplos avanzados
"""
