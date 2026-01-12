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
