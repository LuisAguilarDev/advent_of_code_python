# Conceptos de CS - Day 2 (2018)

---

## 1. Frequency Counting (Conteo de Frecuencias)

El conteo de frecuencias es una tecnica fundamental que consiste en contar cuantas veces aparece cada elemento en una coleccion. Se implementa tipicamente usando una tabla hash (diccionario) donde las claves son los elementos y los valores son sus conteos.

Esta tecnica es extremadamente util porque transforma problemas de busqueda O(n) en consultas O(1). En lugar de recorrer toda la coleccion cada vez que necesitas saber cuantas veces aparece un elemento, construyes el mapa de frecuencias una sola vez y luego consultas en tiempo constante.

En el contexto de este problema, el conteo de frecuencias permite determinar rapidamente si un box ID contiene exactamente 2 o 3 caracteres repetidos. Sin esta tecnica, tendrias que comparar cada caracter con todos los demas, resultando en O(n^2) por cada string.

---

## 2. Hash Tables (Tablas Hash)

Las tablas hash son estructuras de datos que implementan un arreglo asociativo, permitiendo mapear claves a valores con operaciones de insercion, busqueda y eliminacion en tiempo promedio O(1). Funcionan aplicando una funcion hash a la clave para determinar el indice donde almacenar el valor.

La eficiencia de las tablas hash proviene de su acceso directo: en lugar de buscar secuencialmente, calculas donde deberia estar el elemento. Las colisiones (cuando dos claves producen el mismo hash) se manejan con tecnicas como encadenamiento o direccionamiento abierto.

En Python, los diccionarios (`dict`) son implementaciones de tablas hash optimizadas. El metodo `dict.get(key, default)` usado en la solucion es un patron comun para inicializar contadores, evitando verificar explicitamente si la clave existe.

---

## 3. Set Operations (Operaciones de Conjuntos)

Los conjuntos (sets) son colecciones de elementos unicos que soportan operaciones matematicas eficientes como union, interseccion y diferencia. Internamente se implementan con tablas hash, permitiendo verificar pertenencia en O(1) promedio.

La interseccion de conjuntos es particularmente poderosa para encontrar elementos comunes. Si dos strings de longitud n difieren en exactamente un caracter, la interseccion de sus conjuntos de caracteres con posicion tendra exactamente n-1 elementos. Esta observacion transforma un problema de comparacion caracter por caracter en una operacion de conjuntos.

En la solucion de Part 2, cada caracter se codifica con su posicion (ej: "a0", "b1") para crear un conjunto unico por string. La interseccion revela inmediatamente cuantos caracteres coinciden en las mismas posiciones.

---

## 4. Brute Force con Optimizacion

La fuerza bruta consiste en probar todas las combinaciones posibles para encontrar la solucion. Aunque a menudo se considera ineficiente, es una estrategia valida cuando el espacio de busqueda es manejable y la implementacion es simple.

La clave esta en reconocer cuando la fuerza bruta es aceptable. Con n box IDs de longitud m, comparar todos los pares es O(n^2 * m). Para inputs tipicos de Advent of Code (cientos de elementos), esto se ejecuta en milisegundos. La optimizacion prematura seria contraproducente.

El patron de doble loop anidado (`for box1 in boxes: for box2 in boxes`) es clasico de fuerza bruta. En problemas mas grandes, se reemplazaria con estructuras como tries o hashing para reducir comparaciones.

---

## 5. String Similarity (Distancia de Hamming)

La distancia de Hamming mide cuantas posiciones difieren entre dos strings de igual longitud. Es una metrica fundamental en teoria de la informacion, usada en deteccion y correccion de errores, bioinformatica, y busqueda de similitud.

Dos strings con distancia de Hamming igual a 1 son "casi identicos" - difieren en exactamente una posicion. Este concepto es central en Part 2, donde buscamos el par de box IDs con esta propiedad.

La solucion implementa una variante usando conjuntos: si la interseccion de caracteres posicionados tiene tamano n-1, la distancia de Hamming es 1. Esta es una forma elegante pero indirecta; una implementacion directa compararia caracter por caracter contando diferencias.

---

## Ejercicios de practica

- **LeetCode 242** - Valid Anagram (Frequency Counting)
- **LeetCode 383** - Ransom Note (Frequency Counting con Hash Tables)
- **LeetCode 349** - Intersection of Two Arrays (Set Operations)
- **LeetCode 350** - Intersection of Two Arrays II (Frequency Counting)
- **LeetCode 461** - Hamming Distance (String Similarity)
- **LeetCode 1941** - Check if All Characters Have Equal Number of Occurrences (Frequency Analysis)

---

# Conceptos Avanzados Relacionados

## Frequency Counting → Conceptos Avanzados

**Materias relacionadas:** Estructuras de Datos, Algoritmos, Bases de Datos, Procesamiento de Streams

| Concepto Avanzado | Descripcion | Area de CS |
|-------------------|-------------|------------|
| **Count-Min Sketch** | Estructura probabilistica para estimar frecuencias en streams con memoria limitada | Algoritmos Probabilisticos |
| **Heavy Hitters Problem** | Encontrar los k elementos mas frecuentes en tiempo sublineal | Big Data / Streaming |
| **Misra-Gries Algorithm** | Algoritmo determinista para encontrar elementos frecuentes en una pasada | Algoritmos de Streaming |
| **Lossy Counting** | Conteo aproximado de frecuencias con garantias de error | Mineria de Datos |
| **Space-Saving Algorithm** | Mantener top-k elementos frecuentes con memoria fija | Sistemas Distribuidos |

---

## Hash Tables → Conceptos Avanzados

**Materias relacionadas:** Estructuras de Datos, Bases de Datos, Sistemas Distribuidos, Criptografia

| Concepto Avanzado | Descripcion | Area de CS |
|-------------------|-------------|------------|
| **Consistent Hashing** | Distribucion de datos que minimiza reasignaciones al cambiar el numero de nodos | Sistemas Distribuidos |
| **Cuckoo Hashing** | Esquema con O(1) worst-case para busquedas usando multiples funciones hash | Estructuras de Datos |
| **Bloom Filters** | Estructura probabilistica para membership queries con falsos positivos pero sin falsos negativos | Bases de Datos |
| **Hash Joins** | Algoritmo de join en bases de datos usando tablas hash en memoria | Bases de Datos |
| **Perfect Hashing** | Funciones hash sin colisiones para conjuntos estaticos conocidos | Compiladores |

---

## Set Operations → Conceptos Avanzados

**Materias relacionadas:** Matematicas Discretas, Bases de Datos, Teoria de la Computacion

| Concepto Avanzado | Descripcion | Area de CS |
|-------------------|-------------|------------|
| **Union-Find (Disjoint Sets)** | Estructura para particionar elementos en conjuntos disjuntos con union y find eficientes | Algoritmos de Grafos |
| **Bitmap Indexes** | Representacion de conjuntos como vectores de bits para operaciones rapidas | Bases de Datos |
| **Set Cover Problem** | Problema NP-completo de cubrir un universo con minimo numero de subconjuntos | Teoria de la Complejidad |
| **MinHash** | Tecnica de locality-sensitive hashing para estimar similitud de conjuntos | Machine Learning |
| **HyperLogLog** | Algoritmo para estimar cardinalidad de conjuntos con memoria logaritmica | Big Data |

---

## String Similarity → Conceptos Avanzados

**Materias relacionadas:** Algoritmos, Bioinformatica, Procesamiento de Lenguaje Natural, Teoria de la Informacion

| Concepto Avanzado | Descripcion | Area de CS |
|-------------------|-------------|------------|
| **Edit Distance (Levenshtein)** | Minimo numero de operaciones (insertar, eliminar, sustituir) para transformar un string en otro | Algoritmos / NLP |
| **Longest Common Subsequence** | Encontrar la subsecuencia comun mas larga entre dos strings | Programacion Dinamica |
| **Suffix Trees/Arrays** | Estructuras para busqueda eficiente de patrones y analisis de strings | Bioinformatica |
| **Error Correcting Codes** | Codigos que detectan y corrigen errores basados en distancia de Hamming | Teoria de la Informacion |
| **Locality Sensitive Hashing** | Tecnica para encontrar strings similares en grandes datasets | Information Retrieval |

---

## Mapa Curricular

```
Semestre 1-2:              Semestre 3-4:                    Semestre 5+:
+──────────────────────+   +────────────────────────────+   +─────────────────────────────+
| - Arreglos           |   | - Tablas Hash avanzadas    |   | - Consistent Hashing        |
| - Diccionarios       |──►| - Analisis de complejidad  |──►| - Sistemas Distribuidos     |
| - Conjuntos basicos  |   | - Union-Find               |   | - Bloom Filters             |
| - Loops anidados     |   | - Programacion Dinamica    |   | - Algoritmos Probabilisticos|
+──────────────────────+   +────────────────────────────+   +─────────────────────────────+
          │                            │                                │
          ▼                            ▼                                ▼
+──────────────────────+   +────────────────────────────+   +─────────────────────────────+
| - Conteo simple      |   | - Edit Distance            |   | - MinHash / LSH             |
| - Comparacion strings|──►| - Suffix Arrays            |──►| - Bioinformatica            |
| - Distancia Hamming  |   | - Pattern Matching (KMP)   |   | - Error Correcting Codes    |
+──────────────────────+   +────────────────────────────+   +─────────────────────────────+
```

Los conceptos del Day 2 son **building blocks** que aparecen repetidamente en niveles superiores de la carrera. El conteo de frecuencias evoluciona hacia algoritmos de streaming para Big Data. Las operaciones de conjuntos se extienden a estructuras probabilisticas como Bloom Filters. La comparacion de strings escala a sistemas de busqueda de similitud usados en motores de busqueda y bioinformatica.
