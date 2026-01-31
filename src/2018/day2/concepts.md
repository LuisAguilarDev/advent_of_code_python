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

## 6. Checksum (Suma de Verificacion)

Un checksum es un valor calculado a partir de un bloque de datos con el proposito de detectar errores o verificar integridad. Es una forma de "huella digital" que resume los datos en un valor compacto. Si los datos cambian, el checksum resultante sera diferente, permitiendo detectar modificaciones o corrupciones.

El concepto fundamental detras de un checksum es la redundancia controlada: agregamos informacion extra (el checksum) que depende matematicamente de los datos originales. Esta dependencia permite verificar posteriormente si los datos se mantienen intactos comparando el checksum recalculado con el original almacenado.

En el contexto de este problema (Day 2, 2018), el checksum se calcula multiplicando la cantidad de box IDs que contienen exactamente 2 letras repetidas por la cantidad que contienen exactamente 3 letras repetidas. Este checksum "personalizado" actua como una firma del conjunto de datos que permite verificar que se proceso correctamente todo el input.

Los checksums varian en complejidad desde simples sumas aritmeticas hasta funciones hash criptograficas. La eleccion depende del balance entre velocidad de calculo, probabilidad de colision (dos inputs diferentes produciendo el mismo checksum), y resistencia a manipulacion intencional.

---

## Ejercicios de practica

- **LeetCode 242** - Valid Anagram (Frequency Counting)
- **LeetCode 383** - Ransom Note (Frequency Counting con Hash Tables)
- **LeetCode 349** - Intersection of Two Arrays (Set Operations)
- **LeetCode 350** - Intersection of Two Arrays II (Frequency Counting)
- **LeetCode 461** - Hamming Distance (String Similarity)
- **LeetCode 1941** - Check if All Characters Have Equal Number of Occurrences (Frequency Analysis)
- **LeetCode 1217** - Minimum Cost to Move Chips to The Same Position (Checksum/Parity)
- **LeetCode 268** - Missing Number (Checksum con XOR)
- **LeetCode 136** - Single Number (Checksum con XOR)
- **LeetCode 389** - Find the Difference (Checksum con suma o XOR)

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

## Checksum → Conceptos Avanzados

**Materias relacionadas:** Redes de Computadoras, Sistemas Operativos, Seguridad Informatica, Teoria de la Informacion, Bases de Datos

| Concepto Avanzado | Descripcion | Area de CS |
|-------------------|-------------|------------|
| **CRC (Cyclic Redundancy Check)** | Checksum basado en division polinomial, usado en Ethernet, USB, y almacenamiento | Redes / Sistemas |
| **MD5 / SHA Family** | Funciones hash criptograficas que producen checksums de longitud fija resistentes a colisiones | Criptografia / Seguridad |
| **Luhn Algorithm** | Checksum modular usado para validar numeros de tarjetas de credito e identificadores | Sistemas Financieros |
| **Parity Bits** | Bit adicional para detectar errores de un solo bit en transmision de datos | Arquitectura de Computadoras |
| **RAID Parity** | Checksum distribuido para recuperacion de datos en arreglos de discos | Sistemas Operativos |
| **Merkle Trees** | Estructura de arbol donde cada nodo es un hash de sus hijos, usado en blockchain y Git | Sistemas Distribuidos |
| **ECC (Error Correcting Codes)** | Codigos como Hamming y Reed-Solomon que no solo detectan sino corrigen errores | Teoria de la Informacion |
| **Internet Checksum (RFC 1071)** | Checksum de 16 bits usado en protocolos IP, TCP, y UDP | Redes de Computadoras |

### Utilidades Practicas de Checksums

| Aplicacion | Tipo de Checksum | Uso Real |
|------------|------------------|----------|
| **Verificacion de descargas** | SHA-256, MD5 | Confirmar que un archivo descargado no esta corrupto |
| **Control de versiones (Git)** | SHA-1 | Identificar commits y detectar cambios en archivos |
| **Bases de datos** | CRC-32 | Verificar integridad de registros en disco |
| **Comunicaciones de red** | CRC, Internet Checksum | Detectar errores en paquetes transmitidos |
| **Almacenamiento** | RAID parity, ECC | Recuperar datos de discos fallidos o memoria corrupta |
| **Blockchain** | SHA-256, Merkle Trees | Asegurar inmutabilidad de transacciones |
| **Sistemas de archivos (ZFS, Btrfs)** | Checksums por bloque | Detectar y reparar bit rot silencioso |

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
          │                            │                                │
          ▼                            ▼                                ▼
+──────────────────────+   +────────────────────────────+   +─────────────────────────────+
| - Checksums simples  |   | - CRC / Luhn Algorithm     |   | - SHA / MD5 (Criptografia)  |
| - Parity bits        |──►| - Internet Checksum        |──►| - Merkle Trees (Blockchain) |
| - XOR para deteccion |   | - Codigos de Hamming       |   | - Reed-Solomon / ECC        |
+──────────────────────+   +────────────────────────────+   +─────────────────────────────+
```

Los conceptos del Day 2 son **building blocks** que aparecen repetidamente en niveles superiores de la carrera. El conteo de frecuencias evoluciona hacia algoritmos de streaming para Big Data. Las operaciones de conjuntos se extienden a estructuras probabilisticas como Bloom Filters. La comparacion de strings escala a sistemas de busqueda de similitud usados en motores de busqueda y bioinformatica.

Los checksums comienzan como operaciones aritmeticas simples (sumas, XOR) y evolucionan hacia funciones hash criptograficas usadas en seguridad y blockchain. El concepto de detectar errores mediante redundancia es fundamental en redes, almacenamiento, y cualquier sistema donde la integridad de datos sea critica.
