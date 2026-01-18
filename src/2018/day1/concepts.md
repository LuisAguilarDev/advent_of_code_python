# Conceptos de CS - Day 1 (2018)

---

## 1. Hash Tables (Tablas Hash)

Una **Hash Table** es una estructura de datos que almacena pares clave-valor y permite busquedas, inserciones y eliminaciones en tiempo **O(1)** promedio.

Funciona aplicando una **funcion hash** a la clave, lo cual determina directamente la posicion en memoria donde se guarda el valor. Para buscar, se aplica la misma funcion y se accede sin recorrer toda la estructura.

**Por que importa:** Sin hash tables, buscar si un elemento existe requiere recorrer toda la coleccion (O(n)). Con hash tables es instantaneo (O(1)).

| Operacion | Lista | Hash Table |
|-----------|-------|------------|
| Buscar    | O(n)  | O(1)       |
| Insertar  | O(1)  | O(1)       |
| Eliminar  | O(n)  | O(1)       |

**Cuando usarlas:** Busquedas frecuentes, detectar duplicados, contar ocurrencias, cache de resultados.

---

## 2. Deteccion de Ciclos (Cycle Detection)

Es el problema de determinar si una secuencia de estados eventualmente se repite. Un **ciclo** ocurre cuando el sistema vuelve a un estado previamente visitado.

El patron basico consiste en mantener un registro de todos los estados visitados (usando una hash table) y verificar en cada paso si el estado actual ya fue visto.

**Algoritmo de Floyd (Tortuga y Liebre):** Metodo alternativo que usa O(1) espacio. Utiliza dos punteros que avanzan a diferentes velocidades; si hay ciclo, eventualmente se encontraran.

**Aplicaciones:** Deteccion de loops infinitos, listas enlazadas circulares, deteccion de deadlocks, criptografia (colisiones de hash).

---

## 3. Prefix Sum (Suma de Prefijos)

Un arreglo donde cada posicion contiene la suma acumulada de todos los elementos anteriores. Permite calcular la suma de cualquier rango en **O(1)** una vez construido.

En este ejercicio, la frecuencia acumulada es esencialmente un prefix sum: cada valor representa la suma de todos los cambios de frecuencia hasta ese punto.

---

## 4. Trade-off Espacio vs Tiempo

Concepto fundamental: frecuentemente podemos hacer un algoritmo mas rapido usando mas memoria, o usar menos memoria a costa de velocidad.

En este ejercicio se usa **O(n) espacio extra** (el diccionario de frecuencias vistas) para lograr **O(n) tiempo** en lugar de O(n^2).

---

## Ejercicios de practica

- **LeetCode 217** - Contains Duplicate (Hash Tables)
- **LeetCode 141** - Linked List Cycle (Floyd's Algorithm)
- **LeetCode 303** - Range Sum Query (Prefix Sum)
- **LeetCode 287** - Find the Duplicate Number (Cycle Detection)

---

# Conceptos Avanzados Relacionados

## Hash Tables → Conceptos Avanzados

**Materias relacionadas:** Estructuras de Datos, Algoritmos, Bases de Datos, Sistemas Distribuidos

| Concepto Avanzado | Descripcion | Area de CS |
|-------------------|-------------|------------|
| **Consistent Hashing** | Distribucion de datos en sistemas distribuidos (DHT, CDNs, sharding de bases de datos) | Sistemas Distribuidos |
| **Bloom Filters** | Estructura probabilistica para membership queries con falsos positivos pero sin falsos negativos | Algoritmos Probabilisticos |
| **Cuckoo Hashing** | Tecnica de resolucion de colisiones con O(1) worst-case para busquedas | Estructuras de Datos Avanzadas |
| **LSM Trees** | Usa hash tables en memoria + merging en disco (LevelDB, RocksDB, Cassandra) | Bases de Datos |
| **Hash Joins** | Algoritmo de join en DBMS que usa hash tables para eficiencia | Bases de Datos |

---

## Deteccion de Ciclos → Conceptos Avanzados

**Materias relacionadas:** Teoria de Grafos, Sistemas Operativos, Compiladores, Criptografia

| Concepto Avanzado | Descripcion | Area de CS |
|-------------------|-------------|------------|
| **Strongly Connected Components (SCC)** | Tarjan/Kosaraju para detectar ciclos en grafos dirigidos | Teoria de Grafos |
| **Deadlock Detection** | Grafos de espera (wait-for graphs) en SO y DBMS | Sistemas Operativos |
| **Garbage Collection** | Reference counting con cycle detection (mark-and-sweep) | Lenguajes de Programacion |
| **Pollard's Rho** | Factorizacion de enteros usando cycle detection | Criptografia |
| **Model Checking** | Verificacion formal de sistemas con estados finitos | Verificacion Formal |

---

## Prefix Sum → Conceptos Avanzados

**Materias relacionadas:** Algoritmos, Programacion Competitiva, Procesamiento de Senales, Bases de Datos

| Concepto Avanzado | Descripcion | Area de CS |
|-------------------|-------------|------------|
| **Fenwick Tree (BIT)** | Estructura para prefix sums con actualizaciones en O(log n) | Estructuras de Datos |
| **Segment Trees** | Generalizacion para queries de rango arbitrarias | Algoritmos |
| **Summed Area Tables** | Extension 2D para procesamiento de imagenes | Computer Vision |
| **OLAP/Data Cubes** | Pre-computacion de agregaciones multidimensionales | Data Warehousing |
| **Scan (Parallel Prefix)** | Primitiva fundamental en programacion paralela (GPU computing) | Computacion Paralela |

---

## Trade-off Espacio vs Tiempo → Conceptos Avanzados

**Materias relacionadas:** Analisis de Algoritmos, Complejidad Computacional, Arquitectura de Computadoras

| Concepto Avanzado | Descripcion | Area de CS |
|-------------------|-------------|------------|
| **Memoization / Dynamic Programming** | Almacenar subproblemas para evitar recalculo | Algoritmos |
| **Cache Hierarchies** | L1/L2/L3 cache, locality, cache-oblivious algorithms | Arquitectura |
| **Streaming Algorithms** | O(1) o O(log n) espacio para datos masivos | Big Data |
| **Succinct Data Structures** | Representaciones que usan espacio teoricamente optimo | Estructuras Avanzadas |
| **Time-Space Tradeoffs en Criptografia** | Rainbow tables, memory-hard functions (Argon2) | Criptografia |

---

## Mapa Curricular

```
Semestre 1-2:           Semestre 3-4:              Semestre 5+:
+─────────────────+     +──────────────────────+   +─────────────────────────+
| Estructuras de  | ──► | Algoritmos Avanzados |──►| Sistemas Distribuidos   |
| Datos (basico)  |     | Teoria de Grafos     |   | Bases de Datos Avanzadas|
|                 |     | Analisis de Algos    |   | Criptografia            |
| - Hash Tables   |     | - Floyd-Warshall     |   | - Consistent Hashing    |
| - Prefix Sum    |     | - SCC (Tarjan)       |   | - Bloom Filters         |
| - Cycle Det.    |     | - DP avanzado        |   | - Parallel Prefix       |
+─────────────────+     +──────────────────────+   +─────────────────────────+
```

Los conceptos del Day 1 son **building blocks** que aparecen repetidamente en niveles superiores de la carrera.
