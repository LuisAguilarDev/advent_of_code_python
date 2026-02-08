# Conceptos de CS - Day 4 (2018)

---

## 1. Hash Tables (Diccionarios y defaultdict)

Una hash table es una estructura de datos que almacena pares clave-valor, permitiendo acceso, insercion y busqueda en tiempo promedio O(1). Funciona aplicando una funcion hash a la clave para calcular un indice en un arreglo interno donde se almacena el valor asociado.

En este ejercicio, se utiliza `defaultdict(list)` para agrupar los periodos de sueno por guardia. Cada guardia (clave) tiene asociada una lista de tuplas `(duracion, minuto_inicio)`. Esta estructura permite agregar datos sin verificar previamente si la clave existe, ya que `defaultdict` inicializa automaticamente el valor con una lista vacia cuando se accede a una clave nueva.

La eleccion de un diccionario es fundamental aqui porque necesitamos asociar multiples registros de sueno a cada guardia de forma eficiente, y luego acceder rapidamente a los datos de cualquier guardia especifica para calcular totales o frecuencias.

---

## 2. Sorting con Funciones de Comparacion Custom

El sorting (ordenamiento) es el proceso de reorganizar elementos segun un criterio definido. Python utiliza Timsort, un algoritmo hibrido entre merge sort e insertion sort con complejidad O(n log n) en el peor caso. Cuando los datos no tienen un orden natural obvio para el problema, se necesita definir una funcion `key` que extraiga el valor de comparacion.

En este problema, los registros del log de guardias llegan desordenados cronologicamente. El ordenamiento es un **paso de preprocesamiento critico**: sin el, seria imposible determinar que guardia esta activa cuando ocurre un evento de "falls asleep" o "wakes up". La funcion `key` convierte cada string de fecha a un objeto `datetime` para que la comparacion sea temporal y no lexicografica.

Este patron de ordenar datos como paso previo al procesamiento es extremadamente comun en problemas de intervalos, eventos temporales y procesamiento de logs.

---

## 3. Frequency Counting (Counter)

El conteo de frecuencias es una tecnica que registra cuantas veces aparece cada elemento en una coleccion. La clase `Counter` de Python es una especializacion de diccionario optimizada para este proposito, donde las claves son elementos y los valores son sus conteos.

En este ejercicio, `Counter` se utiliza para determinar en que minuto especifico un guardia estuvo dormido con mayor frecuencia. Por cada periodo de sueno, se expande el rango de minutos y se actualiza el contador. El metodo `most_common(1)` retorna eficientemente el minuto con mayor frecuencia sin necesidad de iterar manualmente sobre todos los conteos.

Esta tecnica es la base de problemas de "moda estadistica" y aparece frecuentemente cuando se necesita encontrar el elemento mas repetido, detectar patrones de uso, o analizar distribucion de datos.

---

## 4. Event-Driven Processing (Procesamiento basado en Eventos)

El procesamiento basado en eventos consiste en interpretar una secuencia ordenada de acciones donde el significado de cada evento depende del estado actual del sistema. Se mantiene un estado mutable (que guardia esta activa, cuando se durmio) que se actualiza conforme se procesan los eventos.

En este problema, el log contiene tres tipos de eventos: "begins shift", "falls asleep" y "wakes up". El procesamiento requiere mantener dos variables de estado: el guardia actual y el minuto en que se durmio. Un evento de "wakes up" solo tiene sentido en el contexto del "falls asleep" previo y del guardia activo. Este patron de maquina de estados simple es comun en parseo de logs, procesamiento de transacciones y simulaciones.

La complejidad de este enfoque es O(n) sobre los eventos, ya que cada evento se procesa exactamente una vez en una sola pasada.

---

## 5. Aggregation Strategies (Estrategias de Agregacion)

La agregacion es el proceso de combinar multiples valores en un resultado resumido. Diferentes estrategias de agregacion sobre los mismos datos pueden responder preguntas distintas. La eleccion de la estrategia correcta depende de lo que se busca optimizar.

Este ejercicio ilustra dos estrategias de agregacion contrastantes. La Parte 1 busca el guardia con **mayor tiempo total dormido** (agregacion por suma) y luego su minuto mas frecuente. La Parte 2 busca el guardia que es **mas frecuentemente dormido en un mismo minuto** (agregacion por maximo de frecuencia). Ambas partes usan los mismos datos preprocesados pero llegan a respuestas distintas porque optimizan metricas diferentes.

Este concepto es central en bases de datos (GROUP BY con diferentes funciones de agregacion), analisis de datos y optimizacion, donde una misma coleccion puede ser resumida de multiples formas segun la pregunta que se quiere responder.

---

## Ejercicios de practica

- **LeetCode 49** - Group Anagrams (Hash table con agrupamiento por clave derivada)
- **LeetCode 347** - Top K Frequent Elements (Frequency counting con Counter)
- **LeetCode 56** - Merge Intervals (Sorting como preprocesamiento + procesamiento de intervalos)
- **LeetCode 253** - Meeting Rooms II (Event-driven processing con intervalos temporales)
- **LeetCode 1094** - Car Pooling (Procesamiento de eventos ordenados cronologicamente)
- **LeetCode 169** - Majority Element (Conteo de frecuencias y agregacion)

---

# Conceptos Avanzados Relacionados

## Hash Tables → Conceptos Avanzados

**Materias relacionadas:** Estructuras de Datos, Bases de Datos, Sistemas Distribuidos, Criptografia

| Concepto Avanzado | Descripcion | Area de CS |
|-------------------|-------------|------------|
| **Consistent Hashing** | Distribucion de claves entre nodos que minimiza redistribucion cuando se agregan o eliminan servidores | Sistemas Distribuidos |
| **Hash Joins** | Algoritmo de join en bases de datos que construye una hash table de la tabla menor para buscar coincidencias en O(n+m) | Bases de Datos |
| **Bloom Filters** | Estructura probabilistica que verifica pertenencia a un conjunto con falsos positivos posibles pero sin falsos negativos | Estructuras de Datos |
| **Cuckoo Hashing** | Esquema de hashing con O(1) en el peor caso para busquedas usando dos funciones hash y relocalizacion | Algoritmos |
| **Cryptographic Hash Functions** | Funciones hash unidireccionales resistentes a colisiones, usadas en firmas digitales y verificacion de integridad | Criptografia |

---

## Sorting con Funciones Custom → Conceptos Avanzados

**Materias relacionadas:** Algoritmos, Bases de Datos, Sistemas Operativos, Computacion Paralela

| Concepto Avanzado | Descripcion | Area de CS |
|-------------------|-------------|------------|
| **External Sorting** | Ordenamiento de datos que exceden la memoria RAM usando disco, dividiendo en chunks ordenados y fusionandolos | Sistemas Operativos |
| **Parallel Merge Sort** | Variante que distribuye el trabajo de ordenamiento entre multiples procesadores para acelerar el proceso | Computacion Paralela |
| **B-Tree Sort (Index Sorting)** | Ordenamiento implicitamente mantenido por indices de arboles B en bases de datos para consultas ORDER BY | Bases de Datos |
| **Topological Sort** | Ordenamiento de nodos en un grafo dirigido aciclico respetando dependencias, usado en compiladores y scheduling | Teoria de Grafos |

---

## Frequency Counting → Conceptos Avanzados

**Materias relacionadas:** Algoritmos, Bases de Datos, Estadistica Computacional, Sistemas Distribuidos

| Concepto Avanzado | Descripcion | Area de CS |
|-------------------|-------------|------------|
| **Count-Min Sketch** | Estructura probabilistica para estimar frecuencias en flujos de datos masivos con espacio sublineal | Algoritmos de Streaming |
| **Heavy Hitters Problem** | Identificar los elementos que superan un umbral de frecuencia en un stream, generaliza el "most common" | Sistemas Distribuidos |
| **MapReduce Word Count** | Paradigma de computacion distribuida donde el conteo de frecuencias es el ejemplo canonico | Computacion Paralela |
| **TF-IDF** | Metrica de frecuencia ponderada que mide importancia de terminos en documentos, base del information retrieval | Recuperacion de Informacion |

---

## Event-Driven Processing → Conceptos Avanzados

**Materias relacionadas:** Sistemas Operativos, Sistemas Distribuidos, Compiladores, Ingenieria de Software

| Concepto Avanzado | Descripcion | Area de CS |
|-------------------|-------------|------------|
| **Event Sourcing** | Patron arquitectonico que almacena el estado como secuencia de eventos inmutables en lugar de estado actual | Arquitectura de Software |
| **Finite State Machines** | Modelo formal de computacion con estados finitos y transiciones, base de parsers y protocolos de red | Teoria de la Computacion |
| **Complex Event Processing (CEP)** | Deteccion de patrones en flujos de eventos en tiempo real para identificar situaciones significativas | Sistemas Distribuidos |
| **Write-Ahead Logging** | Tecnica de bases de datos que registra eventos (transacciones) antes de aplicarlos para garantizar durabilidad | Bases de Datos |

---

## Aggregation Strategies → Conceptos Avanzados

**Materias relacionadas:** Bases de Datos, Estadistica Computacional, Machine Learning, Sistemas Distribuidos

| Concepto Avanzado | Descripcion | Area de CS |
|-------------------|-------------|------------|
| **OLAP Cubes** | Estructuras multidimensionales que pre-computan agregaciones para consultas analiticas rapidas | Bases de Datos |
| **Distributed Aggregation** | Combinar resultados parciales de multiples nodos, con desafios como funciones no descomponibles (mediana) | Sistemas Distribuidos |
| **Reduce en MapReduce** | Fase que combina valores asociados a la misma clave usando una funcion de agregacion definida por el usuario | Computacion Paralela |
| **Multi-Objective Optimization** | Optimizacion simultanea de multiples metricas que pueden estar en conflicto entre si | Algoritmos de Optimizacion |

---

## Mapa Curricular

```
Semestre 1-2:               Semestre 3-4:                    Semestre 5+:
+─────────────────────+     +──────────────────────────+     +────────────────────────────+
| Hash Tables         | ──► | Hash Joins               | ──► | Consistent Hashing         |
| Sorting basico      |     | External Sorting         |     | Distributed Aggregation    |
| Conteo de           |     | Topological Sort         |     | Event Sourcing             |
|  frecuencias        |     | Finite State Machines    |     | Complex Event Processing   |
| Procesamiento       |     | B-Tree Indexing          |     | Count-Min Sketch           |
|  secuencial         |     | OLAP y GROUP BY          |     | MapReduce                  |
| Agregaciones        |     | Write-Ahead Logging      |     | Multi-Objective            |
|  simples (sum, max) |     |                          |     |  Optimization              |
+─────────────────────+     +──────────────────────────+     +────────────────────────────+
```

Los conceptos del Day 4 son **building blocks** que aparecen repetidamente en niveles superiores de la carrera. El patron de agrupar datos con hash tables, ordenar eventos cronologicamente, contar frecuencias y aplicar diferentes estrategias de agregacion es la base de sistemas de monitoreo, analisis de logs, bases de datos analiticas y procesamiento de eventos en tiempo real.
