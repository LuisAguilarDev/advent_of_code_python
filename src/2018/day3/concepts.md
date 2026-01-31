# Conceptos de CS - Day 3 (2018)

---

## 1. Grid-Based Coordinate Systems (Sistemas de Coordenadas en Grilla)

Un sistema de coordenadas en grilla representa el espacio como una matriz bidimensional de celdas discretas. Cada celda se identifica por un par (fila, columna) o (x, y). Este modelo es fundamental en graficos por computadora, videojuegos, simulaciones fisicas, y problemas geometricos.

La discretizacion del espacio continuo en celdas permite usar estructuras de datos eficientes como arreglos 2D o hash maps. En lugar de calcular intersecciones geometricas complejas, simplemente verificamos si dos objetos ocupan la misma celda. Esta simplificacion transforma problemas de geometria computacional en problemas de conjuntos.

En este problema, cada "claim" define un rectangulo en la grilla. Las coordenadas (columna, fila) indican la esquina superior izquierda, y las dimensiones (ancho, alto) definen cuantas celdas ocupa. Iterar sobre todas las celdas de un rectangulo es O(ancho * alto), lo cual es eficiente para rectangulos pequenos.

---

## 2. Rectangle Overlap Detection (Deteccion de Colisiones entre Rectangulos)

La deteccion de colisiones entre rectangulos es un problema clasico en graficos, videojuegos, y sistemas CAD. Dos rectangulos se solapan si comparten al menos una celda (o punto, en el caso continuo). Este problema tiene multiples soluciones dependiendo del contexto.

El enfoque "brute force" usado en este problema enumera cada celda de cada rectangulo y verifica si ya fue visitada. Aunque tiene complejidad O(n * area_promedio), es simple y suficiente para inputs moderados. Para grandes cantidades de rectangulos, se usarian estructuras como R-trees o sweep line algorithms.

La solucion utiliza un set `visited` para rastrear celdas ocupadas. Cuando una celda ya esta en `visited`, se agrega a `overlaped`. Esta tecnica de "marcar y verificar" es un patron comun en deteccion de colisiones discretas.

---

## 3. Spatial Hashing (Hashing Espacial)

El hashing espacial es una tecnica que mapea posiciones en el espacio a buckets en una tabla hash. Permite consultas de proximidad y colision en tiempo O(1) promedio, evitando comparar cada par de objetos (que seria O(n^2)).

En la solucion, cada celda (r, c) se usa directamente como clave en un set o diccionario. Python hashea tuplas de enteros eficientemente, permitiendo O(1) para insercion y busqueda. Este es un caso especial de spatial hashing donde cada celda es su propio bucket.

Para grillas muy grandes o espacios continuos, se usarian funciones hash que agrupan multiples posiciones cercanas en el mismo bucket. Esto reduce memoria a costa de verificaciones adicionales dentro de cada bucket.

---

## 4. Set Difference for Filtering (Diferencia de Conjuntos para Filtrado)

La diferencia de conjuntos (A - B) retorna elementos que estan en A pero no en B. Es una operacion fundamental para filtrar elementos que cumplen o no cumplen ciertas condiciones.

En Part 2, se mantienen dos sets: `visited` con todos los IDs de claims, y `overlapped` con IDs que tienen al menos un solapamiento. La diferencia `visited - overlapped` produce exactamente los IDs sin solapamiento. Esta operacion es O(|A|) y elegantemente resuelve el problema de filtrado.

Este patron aparece frecuentemente: construir un "universo" de candidatos, construir un conjunto de "descalificados", y la diferencia produce los candidatos validos. Es mas eficiente que iterar y verificar cada candidato individualmente.

---

## 5. String Parsing and Tokenization (Parsing y Tokenizacion de Strings)

El parsing transforma texto en estructuras de datos utilizables. La tokenizacion divide el texto en componentes significativos (tokens) basandose en delimitadores o patrones.

El input tiene formato "#1 @ 3,2: 5x4" que codifica: ID=1, columna=3, fila=2, ancho=5, alto=4. La solucion usa `split()` para separar por espacios, luego procesa cada parte individualmente. Este enfoque manual es fragil pero rapido para formatos simples y bien definidos.

Para formatos mas complejos, se usarian expresiones regulares (regex) o parsers formales. El metodo `split()` de Python es O(n) donde n es la longitud del string, y es suficiente cuando el formato es predecible y consistente.

---

## 6. Dictionary as Spatial Index (Diccionario como Indice Espacial)

Un diccionario puede funcionar como indice espacial mapeando posiciones a datos asociados. A diferencia de un set que solo responde "ocupado/vacio", un diccionario responde "quien ocupa esta posicion".

En Part 2, `visited_dict[square] = id` almacena cual claim ocupa cada celda. Cuando se detecta colision, podemos recuperar el ID del claim previo y marcar ambos como solapados. Esta informacion adicional es crucial para identificar el claim sin solapamientos.

Este patron de "indice inverso" es comun en bases de datos y sistemas de busqueda: en lugar de buscar "que celdas ocupa el claim X", preguntamos "que claim ocupa la celda Y". Ambas direcciones de busqueda son O(1) con la estructura correcta.

---

## Ejercicios de practica

- **LeetCode 836** - Rectangle Overlap (Deteccion de solapamiento)
- **LeetCode 223** - Rectangle Area (Area de union de rectangulos)
- **LeetCode 391** - Perfect Rectangle (Verificar si rectangulos forman un rectangulo perfecto)
- **LeetCode 218** - The Skyline Problem (Sweep line con rectangulos)
- **LeetCode 1828** - Queries on Number of Points Inside a Circle (Consultas espaciales)
- **LeetCode 939** - Minimum Area Rectangle (Encontrar rectangulo minimo)
- **LeetCode 850** - Rectangle Area II (Area de union de multiples rectangulos)

---

# Conceptos Avanzados Relacionados

## Grid-Based Systems -> Conceptos Avanzados

**Materias relacionadas:** Graficos por Computadora, Desarrollo de Videojuegos, Sistemas de Informacion Geografica (GIS), Robotica

| Concepto Avanzado | Descripcion | Area de CS |
|-------------------|-------------|------------|
| **Tile Maps** | Representacion de mundos 2D como mosaicos, usado en videojuegos y GIS | Desarrollo de Juegos |
| **Voxel Grids** | Extension 3D de grillas, usado en graficos volumetricos y simulaciones | Graficos 3D |
| **Occupancy Grids** | Grillas probabilisticas para mapeo robotico y navegacion autonoma | Robotica / SLAM |
| **Cellular Automata** | Sistemas donde el estado de cada celda depende de sus vecinos | Simulacion / Teoria de la Computacion |
| **Quadtrees / Octrees** | Subdivision recursiva del espacio para busquedas eficientes | Graficos / Bases de Datos Espaciales |

---

## Collision Detection -> Conceptos Avanzados

**Materias relacionadas:** Graficos por Computadora, Fisica de Videojuegos, CAD/CAM, Simulacion

| Concepto Avanzado | Descripcion | Area de CS |
|-------------------|-------------|------------|
| **Bounding Volume Hierarchies (BVH)** | Jerarquia de volumenes envolventes para colisiones eficientes | Graficos / Fisica |
| **Sweep and Prune** | Algoritmo que ordena objetos por ejes para detectar colisiones | Fisica de Videojuegos |
| **GJK Algorithm** | Algoritmo para detectar colision entre formas convexas | Geometria Computacional |
| **Separating Axis Theorem (SAT)** | Teorema para verificar no-colision entre poligonos convexos | Geometria Computacional |
| **Continuous Collision Detection** | Detectar colisiones considerando movimiento entre frames | Simulacion Fisica |

---

## Spatial Indexing -> Conceptos Avanzados

**Materias relacionadas:** Bases de Datos, GIS, Graficos, Machine Learning

| Concepto Avanzado | Descripcion | Area de CS |
|-------------------|-------------|------------|
| **R-Trees** | Estructura de arbol para indexar objetos espaciales multidimensionales | Bases de Datos Espaciales |
| **K-D Trees** | Arbol binario que particiona espacio k-dimensional | Machine Learning / Graficos |
| **Geohashing** | Codificar coordenadas geograficas en strings para indexacion | GIS / Bases de Datos |
| **Locality Sensitive Hashing (LSH)** | Hashing que preserva proximidad para busqueda de vecinos cercanos | Machine Learning |
| **Grid Files** | Estructura de archivo que divide espacio en celdas para acceso a disco | Bases de Datos |

---

## Parsing -> Conceptos Avanzados

**Materias relacionadas:** Compiladores, Procesamiento de Lenguaje Natural, Bases de Datos

| Concepto Avanzado | Descripcion | Area de CS |
|-------------------|-------------|------------|
| **Regular Expressions** | Patrones para matching y extraccion de texto estructurado | Teoria de la Computacion |
| **Context-Free Grammars** | Gramaticas formales para describir lenguajes estructurados | Compiladores |
| **Recursive Descent Parsing** | Tecnica de parsing top-down para gramaticas LL | Compiladores |
| **Parser Combinators** | Funciones componibles para construir parsers complejos | Programacion Funcional |
| **Lexical Analysis (Tokenization)** | Primera fase de compilacion que convierte texto en tokens | Compiladores |

---

## Mapa Curricular

```
Semestre 1-2:              Semestre 3-4:                    Semestre 5+:
+──────────────────────+   +────────────────────────────+   +─────────────────────────────+
| - Arreglos 2D        |   | - Quadtrees / K-D Trees    |   | - R-Trees / Spatial DBs     |
| - Coordenadas (x,y)  |──►| - Geometria Computacional  |──►| - GIS / Mapping Systems     |
| - Iteracion de grids |   | - Algoritmos de graficos   |   | - Voxel Engines             |
+──────────────────────+   +────────────────────────────+   +─────────────────────────────+
          │                            │                                │
          ▼                            ▼                                ▼
+──────────────────────+   +────────────────────────────+   +─────────────────────────────+
| - Colision basica    |   | - Bounding Volumes         |   | - BVH / Broad Phase         |
| - AABB simple        |──►| - Sweep and Prune          |──►| - Continuous Collision      |
| - Grid-based check   |   | - SAT para poligonos       |   | - Physics Engines           |
+──────────────────────+   +────────────────────────────+   +─────────────────────────────+
          │                            │                                │
          ▼                            ▼                                ▼
+──────────────────────+   +────────────────────────────+   +─────────────────────────────+
| - split() / tokens   |   | - Regex avanzado           |   | - Gramaticas formales       |
| - Parsing manual     |──►| - State machines           |──►| - Compiladores              |
| - Formatos simples   |   | - JSON/XML parsing         |   | - Parser generators         |
+──────────────────────+   +────────────────────────────+   +─────────────────────────────+
```

Los conceptos del Day 3 son fundamentales para graficos, videojuegos y sistemas espaciales. El trabajo con grillas 2D evoluciona hacia estructuras espaciales avanzadas usadas en GIS y bases de datos. La deteccion de colisiones basica escala a motores de fisica sofisticados. El parsing manual de strings es el primer paso hacia la construccion de compiladores y procesadores de lenguaje.

---

## Aplicaciones en la Industria

| Concepto | Aplicacion Real | Ejemplo |
|----------|-----------------|---------|
| **Grid Systems** | Videojuegos 2D | Tiles en Super Mario, Civilization |
| **Collision Detection** | Motores de fisica | Unity, Unreal Engine, Box2D |
| **Spatial Hashing** | Bases de datos geograficas | PostGIS, MongoDB geospatial |
| **Rectangle Overlap** | UI Layout | Detectar elementos superpuestos en CSS |
| **Parsing** | Procesamiento de logs | Analisis de logs de servidores |
| **Spatial Indexing** | Mapas y navegacion | Google Maps, Uber routing |
