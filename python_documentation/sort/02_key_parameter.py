"""
================================================================================
PASO 2: EL PARÁMETRO 'key' - EL SECRETO DEL SORTING PERSONALIZADO
================================================================================

El parámetro 'key' es una FUNCIÓN que transforma cada elemento ANTES de comparar.
Python NO ordena los elementos directamente, ordena los VALORES que retorna key.

IMPORTANTE: La función key recibe UN elemento y debe retornar UN valor comparable.

"""

# =============================================================================
# 2.1 - ¿Qué es 'key'?
# =============================================================================

"""
Imagina que tienes: ["banana", "Apple", "cherry"]

Sin key:
    Python compara: "banana" vs "Apple" vs "cherry"
    Resultado: ['Apple', 'banana', 'cherry']  (mayúsculas primero por ASCII)

Con key=str.lower:
    Python TRANSFORMA primero: "banana" -> "banana", "Apple" -> "apple", "cherry" -> "cherry"
    Luego compara: "banana" vs "apple" vs "cherry"
    Resultado: ['Apple', 'banana', 'cherry'] ordenado como si fueran minúsculas

¡IMPORTANTE! Los elementos originales NO cambian, solo se usa key para COMPARAR.
"""

frutas = ["banana", "Apple", "cherry", "apricot"]

# Sin key - orden ASCII (mayúsculas primero)
print("Sin key:", sorted(frutas))
# ['Apple', 'apricot', 'banana', 'cherry']

# Con key=str.lower - ignora mayúsculas/minúsculas
print("Con key=str.lower:", sorted(frutas, key=str.lower))
# ['Apple', 'apricot', 'banana', 'cherry'] - pero ordenado alfabéticamente real

# =============================================================================
# 2.2 - Visualizando cómo funciona 'key'
# =============================================================================

"""
Vamos a ver EXACTAMENTE qué pasa internamente.
"""


def mi_key_con_debug(elemento):
    """Esta función nos muestra qué está pasando"""
    valor_transformado = len(elemento)  # Usamos la longitud como ejemplo
    print(f"  key('{elemento}') -> {valor_transformado}")
    return valor_transformado


palabras = ["hi", "hello", "hey", "howdy"]

print("=== Proceso de sorting con key=len ===")
print("Python llama a key() para cada elemento:")
resultado = sorted(palabras, key=mi_key_con_debug)
print(f"Resultado: {resultado}")
print()

"""
Output:
  key('hi') -> 2
  key('hello') -> 5
  key('hey') -> 3
  key('howdy') -> 5
Resultado: ['hi', 'hey', 'hello', 'howdy']

Python ordenó por LONGITUD (2, 3, 5, 5), no alfabéticamente.
"""

# =============================================================================
# 2.3 - Funciones built-in comunes como key
# =============================================================================

# len - ordenar por longitud
palabras = ["python", "es", "genial", "yo"]
print("Por longitud:", sorted(palabras, key=len))
# ['es', 'yo', 'python', 'genial']  -> ordenado por len: 2, 2, 6, 6

# str.lower - ordenar ignorando mayúsculas
nombres = ["Ana", "bob", "Carlos", "diana"]
print("Ignorando mayúsculas:", sorted(nombres, key=str.lower))
# ['Ana', 'bob', 'Carlos', 'diana']

# abs - ordenar por valor absoluto
numeros = [-5, 2, -1, 4, -3]
print("Por valor absoluto:", sorted(numeros, key=abs))
# [-1, 2, -3, 4, -5]  -> ordenado por abs: 1, 2, 3, 4, 5

# =============================================================================
# 2.4 - Definiendo tu propia función key
# =============================================================================

# Ejemplo: Ordenar personas por edad
personas = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Bob", "edad": 30},
    {"nombre": "Carlos", "edad": 20}
]

# Definimos una función que extrae la edad


def obtener_edad(persona):
    return persona["edad"]


# Usamos esa función como key
por_edad = sorted(personas, key=obtener_edad)
print("Personas por edad:")
for p in por_edad:
    print(f"  {p['nombre']}: {p['edad']}")
# Carlos: 20, Ana: 25, Bob: 30

# =============================================================================
# 2.5 - ¿Qué DEBE retornar la función key?
# =============================================================================

"""
La función key DEBE retornar algo COMPARABLE con < y >

VÁLIDO - Retorna tipos comparables:
- Números (int, float)
- Strings
- Tuplas de valores comparables
- Listas de valores comparables

INVÁLIDO - Esto causará error:
- None (no se puede comparar con <)
- Diccionarios (no son comparables directamente)
- Objetos personalizados sin __lt__ definido
"""

# CORRECTO: Retornando un número


def key_correcta(x):
    return x * 2  # Retorna número

# CORRECTO: Retornando un string


def key_correcta_str(x):
    return str(x).lower()  # Retorna string

# CORRECTO: Retornando una tupla (MUY ÚTIL - lo veremos en detalle)


def key_correcta_tupla(x):
    return (x["prioridad"], x["nombre"])  # Retorna tupla

# INCORRECTO: Retornando None


def key_incorrecta(x):
    return None  # ERROR: NoneType no es comparable

# =============================================================================
# 2.6 - La función key se llama UNA VEZ por elemento
# =============================================================================


"""
OPTIMIZACIÓN IMPORTANTE:

Python llama a key() una sola vez por cada elemento, NO en cada comparación.
Esto se llama "decorate-sort-undecorate" o "Schwartzian transform".

Si tienes 1000 elementos y key() es costosa, solo se llama 1000 veces,
no miles de veces en cada comparación.
"""

contador = 0


def key_costosa(elemento):
    global contador
    contador += 1
    # Simulamos una operación costosa
    return len(elemento)


lista = ["uno", "dos", "tres", "cuatro", "cinco"]
sorted(lista, key=key_costosa)
print(f"key() se llamó {contador} veces para {len(lista)} elementos")
# key() se llamó 5 veces para 5 elementos (no 5*4=20 comparaciones)
print()

# =============================================================================
# RESUMEN PASO 2
# =============================================================================

"""
PUNTOS CLAVE:

1. key es una FUNCIÓN que recibe UN elemento
2. key DEBE retornar un valor COMPARABLE (<, >)
3. Python ordena por los valores que RETORNA key, no por los elementos
4. Los elementos originales NO se modifican
5. key se llama UNA vez por elemento (eficiente)
6. Funciones built-in útiles: len, str.lower, abs, int, float

ESTRUCTURA DE UNA FUNCIÓN KEY:

    def mi_key(elemento):
        # Transformar elemento
        valor = alguna_transformacion(elemento)
        # Retornar valor comparable
        return valor

PRÓXIMO PASO: Entender exactamente cómo Python compara los valores
"""
