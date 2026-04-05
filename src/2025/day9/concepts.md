# Conceptos de CS - Day 9 (2025)

---

## 1. Sparse Table (Tabla Dispersa)

Una Sparse Table es una estructura de datos que permite responder consultas de rango (range queries) en tiempo constante O(1) despues de un preprocesamiento de O(n log n). Funciona exclusivamente para operaciones **idempotentes**, es decir, operaciones donde aplicarla dos veces al mismo elemento no cambia el resultado, como `min` y `max`. Por ejemplo, `max(5, 5) = 5` -- no importa si "cuentas" un elemento dos veces.

### Como identificar cuando necesitas una Sparse Table

La senal mas clara es: **tienes un arreglo que no cambia y necesitas responder muchas veces la pregunta "cual es el minimo (o maximo) entre la posicion i y la posicion j?"**. Si haces esta pregunta una sola vez, un simple `for` basta. Pero si la haces miles o millones de veces sobre el mismo arreglo, un `for` por cada consulta es demasiado lento.

En este ejercicio, la version lenta (`part2.py`) validaba cada rectangulo recorriendo fila por fila: "esta fila cubre el rango de columnas que necesito?". Con coordenadas de hasta 100,000, cada validacion podia iterar decenas de miles de filas. Multiplicado por 122,760 pares de posiciones, el total era de cientos de millones de operaciones.

### Como funciona paso a paso

**Paso 1 - Preprocesamiento (se hace UNA sola vez):**

La idea central es precalcular respuestas para todos los sub-rangos cuyo tamano es una potencia de 2: rangos de tamano 1, 2, 4, 8, 16, etc.

Imagina que tienes el arreglo `[3, 1, 4, 1, 5, 9, 2, 6]` y quieres hacer consultas de minimo:

- Nivel 0 (tamano 1): cada elemento solo: `[3, 1, 4, 1, 5, 9, 2, 6]`
- Nivel 1 (tamano 2): minimo de cada par consecutivo: `[1, 1, 1, 1, 5, 2, 2, -]`
  - `min(3,1)=1, min(1,4)=1, min(4,1)=1, min(1,5)=1, min(5,9)=5, min(9,2)=2, min(2,6)=2`
- Nivel 2 (tamano 4): minimo de cada grupo de 4: `[1, 1, 1, 1, 2, 2, -, -]`
  - Se construye combinando el nivel anterior: `min(nivel1[0], nivel1[2])=min(1,1)=1`, etc.
- Nivel 3 (tamano 8): minimo de todo el arreglo: `[1, -, -, -, -, -, -, -]`

Cada nivel se construye a partir del anterior, por eso es O(n log n) en total.

**Paso 2 - Consulta (se hace CADA VEZ que preguntas):**

Para consultar el minimo entre posiciones `l` y `r`, encuentras la mayor potencia de 2 que cabe en ese rango. Llamala `k`. Luego combinas dos bloques que se pueden solapar:

- Bloque 1: desde `l`, de tamano `2^k`
- Bloque 2: terminando en `r`, de tamano `2^k`

Como `min` es idempotente, no importa que los bloques se solapen. El resultado es correcto. Esto toma O(1) porque solo es una operacion: `min(tabla[k][l], tabla[k][r - 2^k + 1])`.

### Aplicacion en este ejercicio

En la version mejorada (`part2_improved.py`), en lugar de recorrer cada fila una por una para validar, se precalculan 4 Sparse Tables:

1. **row_max_lo**: el maximo de todos los "limites izquierdos" de las filas en un rango. Si este valor es mayor que la columna izquierda del rectangulo, alguna fila no lo cubre.
2. **row_min_hi**: el minimo de todos los "limites derechos" de las filas. Si este valor es menor que la columna derecha, alguna fila no alcanza.
3. **col_max_lo** y **col_min_hi**: lo mismo pero para columnas.

Resultado: cada validacion pasa de O(rango) a O(1). Con ~97,000 filas/columnas posibles, esto elimina millones de operaciones.

---

## 2. Compresion de Coordenadas

Compresion de coordenadas es una tecnica que transforma valores grandes y dispersos en indices pequenos y consecutivos. Si tus coordenadas originales son `[1544, 3200, 98366]`, despues de comprimir se convierten en `[0, 1, 2]`. Los valores originales se guardan en un arreglo ordenado para poder traducir de vuelta.

### Como identificar cuando la necesitas

La senal es: **tus datos usan coordenadas enormes (miles, millones) pero la cantidad de valores unicos es mucho menor**. En este ejercicio, las coordenadas van de 1,544 a 98,366, pero solo hay ~97,000 filas unicas. Sin compresion, necesitarias un arreglo de 100,000 posiciones (la mayoria vacias). Con compresion, solo necesitas un arreglo de 97,000 posiciones, todas utiles.

### Como funciona paso a paso

1. **Recolectar** todos los valores unicos que aparecen (en este caso, todas las filas que tienen posiciones validas).
2. **Ordenarlos**: `sorted_rows = sorted(row_ranges.keys())` -- esto convierte el conjunto desordenado en una lista ordenada.
3. **Crear un mapa de traduccion**: `row_idx = {r: i for i, r in enumerate(sorted_rows)}` -- ahora la fila 1544 es el indice 0, la fila 1545 es el indice 1, etc.
4. **Usar indices en lugar de coordenadas reales** para todas las operaciones internas (Sparse Tables, verificaciones de contiguidad).

### Por que es critica en este ejercicio

La compresion permite dos cosas fundamentales:

Primero, hace posible la **verificacion de contiguidad en O(1)**. Para saber si todas las filas entre `min_r` y `max_r` existen, basta comparar: `sorted_rows[idx_end] - sorted_rows[idx_start] == idx_end - idx_start`. Si las filas 5, 6, 7, 8 estan en posiciones 3, 4, 5, 6 del arreglo comprimido, entonces `8 - 5 == 6 - 3` (ambos son 3). Pero si faltara la fila 7, los indices serian 3, 4, 5 para las filas 5, 6, 8, y `8 - 5 = 3` pero `5 - 3 = 2` -- no coinciden, asi que hay un hueco.

Segundo, permite construir las Sparse Tables sobre arreglos **densos** (sin huecos), lo cual es requisito para que funcionen correctamente.

---

## 3. Busqueda Exhaustiva con Poda (Brute Force con Pruning)

Busqueda exhaustiva significa probar todas las combinaciones posibles. En este problema, se prueban todos los pares de posiciones (n*(n-1)/2 = 122,760 pares para 496 posiciones). La **poda** (pruning) consiste en descartar combinaciones tempranamente sin evaluarlas completamente, usando condiciones que detectan rapido que no pueden dar un resultado mejor.

### Como identificar cuando aplicarla

Cuando el espacio de busqueda es manejable (miles o cientos de miles, no millones) pero cada evaluacion individual es costosa. La estrategia es: **mantener la busqueda exhaustiva pero hacer cada evaluacion lo mas rapida posible**. No siempre puedes evitar revisar todos los pares, pero si puedes hacer que cada revision tome microsegundos en vez de milisegundos.

### Poda aplicada en este ejercicio

El codigo usa dos formas de poda:

1. **`area > big_area`**: se verifica ANTES de llamar a `is_valid_rectangle`. Si el area del rectangulo candidato ni siquiera supera el mejor encontrado hasta ahora, no tiene sentido validarlo. Esto es poda por **cota inferior** (lower bound pruning).

2. **Evaluacion corto-circuito en `is_valid_rectangle`**: la funcion retorna `False` al primer chequeo que falla. En la version optimizada, los chequeos mas baratos (existencia de endpoints, contiguidad) se hacen primero, antes de las consultas a la Sparse Table.

La combinacion de poda + validacion O(1) convierte un algoritmo que tardaba minutos en uno que termina en menos de 1 segundo.

---

## 4. Range Queries (Consultas de Rango)

Una consulta de rango es cualquier pregunta de la forma: "dado un arreglo, cual es el resultado de aplicar una operacion sobre todos los elementos entre la posicion i y la posicion j?". Ejemplos comunes: suma de un rango, minimo de un rango, maximo de un rango, GCD de un rango.

### Diferentes estructuras segun el problema

No todas las consultas de rango se resuelven igual. La eleccion depende de dos factores: si el arreglo cambia (actualizaciones) y que operacion necesitas.

**Arreglo estatico (no cambia):**
- Prefix Sum: para consultas de suma en O(1). Precalculas sumas acumuladas.
- Sparse Table: para consultas de min/max en O(1). Es lo que usamos aqui.

**Arreglo dinamico (se modifica):**
- Segment Tree (arbol de segmentos): soporta actualizaciones y consultas en O(log n). Es mas flexible pero mas lenta para consultas que la Sparse Table.
- Binary Indexed Tree (Fenwick Tree): similar al Segment Tree pero mas simple para sumas.

En este ejercicio, el arreglo de rangos se construye una vez y nunca cambia, asi que la Sparse Table es la eleccion perfecta: O(1) por consulta sin la complejidad de un Segment Tree.

---

## Ejercicios de practica

- **LeetCode 239** - Sliding Window Maximum (Sparse Table / Deque para range max)
- **LeetCode 307** - Range Sum Query - Mutable (Segment Tree / Fenwick Tree)
- **LeetCode 304** - Range Sum Query 2D - Immutable (Prefix Sum 2D)
- **LeetCode 85** - Maximal Rectangle (Rectangulo maximo en matriz, stack-based)
- **LeetCode 221** - Maximal Square (DP para cuadrado maximo)
- **LeetCode 1157** - Online Majority Element In Subarray (Sparse Table avanzada)
- **LeetCode 2055** - Plates Between Candles (Prefix Sum + Binary Search)

---

# Conceptos Avanzados Relacionados

## Sparse Table -> Conceptos Avanzados

**Materias relacionadas:** Estructuras de Datos, Algoritmos, Bases de Datos, Computacion Paralela

| Concepto Avanzado | Descripcion | Area de CS |
|-------------------|-------------|------------|
| **Segment Tree** | Arbol que soporta consultas de rango Y actualizaciones en O(log n). Generaliza la Sparse Table para arreglos dinamicos | Estructuras de Datos |
| **Fenwick Tree (BIT)** | Estructura compacta para prefix sums con actualizaciones. Usa aritmetica de bits para navegar el arbol implicitamente | Estructuras de Datos |
| **Sparse Table 2D** | Extension a matrices: consultas de min/max sobre sub-matrices en O(1) con preprocesamiento O(nm log n log m) | Algoritmos |
| **Range Tree** | Arbol multi-dimensional para consultas de rango en espacios de k dimensiones. Usado en bases de datos espaciales | Bases de Datos |
| **Parallel Prefix (Scan)** | Version paralela de prefix sum que se ejecuta en GPUs. Fundamental en computacion de alto rendimiento (CUDA, OpenCL) | Computacion Paralela |

---

## Compresion de Coordenadas -> Conceptos Avanzados

**Materias relacionadas:** Algoritmos, Geometria Computacional, Bases de Datos, Sistemas de Informacion Geografica

| Concepto Avanzado | Descripcion | Area de CS |
|-------------------|-------------|------------|
| **Line Sweep** | Algoritmo que barre un plano con una linea vertical/horizontal. Usa compresion de coordenadas para discretizar eventos | Geometria Computacional |
| **R-Tree** | Estructura de indexacion espacial para bases de datos geograficas. Agrupa objetos cercanos en rectangulos jerarquicos | Bases de Datos |
| **Discretizacion para DP** | Comprimir estados de DP cuando el espacio es enorme pero los valores utiles son pocos. Comun en problemas de intervalos | Algoritmos |
| **Hash Joins con Compresion** | En bases de datos, comprimir claves de join para que quepan en cache L1/L2 y acelerar la operacion | Bases de Datos |
| **Quadtree / KD-Tree** | Arboles de particion espacial que subdividen el espacio recursivamente. Usados en graficos, GIS y busqueda de vecinos cercanos | Geometria Computacional |

---

## Busqueda Exhaustiva con Poda -> Conceptos Avanzados

**Materias relacionadas:** Algoritmos, Inteligencia Artificial, Investigacion de Operaciones, Teoria de Complejidad

| Concepto Avanzado | Descripcion | Area de CS |
|-------------------|-------------|------------|
| **Branch and Bound** | Formalizacion de la poda: explorar un arbol de soluciones descartando ramas que no pueden mejorar la mejor solucion conocida | Investigacion de Operaciones |
| **Alpha-Beta Pruning** | Poda para arboles de juegos (ajedrez, Go). Elimina ramas que un jugador racional nunca elegiria | Inteligencia Artificial |
| **Backtracking** | Busqueda exhaustiva que construye soluciones incrementalmente y retrocede al encontrar un camino sin salida (Sudoku, N-Queens) | Algoritmos |
| **Constraint Propagation** | Reducir el espacio de busqueda propagando restricciones antes de buscar. Usado en SAT solvers y CSP | Inteligencia Artificial |
| **Randomized Pruning** | Usar muestreo aleatorio para estimar si una rama es prometedora antes de explorarla completamente | Algoritmos Aleatorizados |

---

## Range Queries -> Conceptos Avanzados

**Materias relacionadas:** Estructuras de Datos, Bases de Datos, Sistemas Distribuidos, Arquitectura de Computadoras

| Concepto Avanzado | Descripcion | Area de CS |
|-------------------|-------------|------------|
| **Fractional Cascading** | Tecnica para acelerar busquedas binarias multiples en listas relacionadas. Reduce O(k log n) a O(k + log n) | Estructuras de Datos |
| **Persistent Data Structures** | Estructuras que preservan versiones anteriores al modificarse. Permiten consultas de rango "en el tiempo" | Estructuras de Datos |
| **LSM Trees** | Estructura de bases de datos (LevelDB, RocksDB) que optimiza escrituras usando merge sort entre niveles. Range scans eficientes | Bases de Datos |
| **Cache-Oblivious B-Trees** | Arboles que funcionan eficientemente sin importar el tamano de cache. Optimizan acceso a memoria en range queries | Arquitectura de Computadoras |
| **CRDT Range Queries** | Consultas de rango sobre datos replicados en sistemas distribuidos sin coordinacion central | Sistemas Distribuidos |

---

## Mapa Curricular

```
Semestre 1-2:                   Semestre 3-4:                       Semestre 5+:
+─────────────────────+         +──────────────────────────+        +─────────────────────────────+
| Arreglos, Hash Maps | ──────► | Segment Trees            | ─────► | Persistent Segment Trees    |
| Prefix Sum          |         | Fenwick Trees            |        | Fractional Cascading        |
| Busqueda Lineal     |         | Sparse Tables            |        | Cache-Oblivious Structures  |
+─────────────────────+         +──────────────────────────+        +─────────────────────────────+
         │                                │                                    │
         ▼                                ▼                                    ▼
+─────────────────────+         +──────────────────────────+        +─────────────────────────────+
| Fuerza Bruta        | ──────► | Backtracking             | ─────► | Branch and Bound            |
| Ordenamiento        |         | Branch and Bound basico  |        | Alpha-Beta Pruning          |
| Complejidad O(n^2)  |         | Poda por cotas           |        | Constraint Propagation      |
+─────────────────────+         +──────────────────────────+        +─────────────────────────────+
         │                                │                                    │
         ▼                                ▼                                    ▼
+─────────────────────+         +──────────────────────────+        +─────────────────────────────+
| Coordenadas basicas | ──────► | Compresion de Coordenadas| ─────► | R-Trees, KD-Trees           |
| Geometria simple    |         | Line Sweep               |        | Quadtrees, BSP Trees        |
|                     |         | Discretizacion           |        | Indexacion Espacial en DBs   |
+─────────────────────+         +──────────────────────────+        +─────────────────────────────+
```

Los conceptos del Day 9 son **building blocks** que aparecen repetidamente en niveles superiores de la carrera. La Sparse Table es la puerta de entrada al mundo de las range queries, la compresion de coordenadas es fundamental en geometria computacional y bases de datos, y la poda inteligente es la base de toda la optimizacion combinatoria.
