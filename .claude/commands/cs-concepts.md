---
description: Genera documentacion de conceptos de Computer Science para un dia de Advent of Code
allowed-tools: Read, Glob, Grep, Write
---

# Generador de Conceptos de CS para Advent of Code

## Instrucciones

Cuando el usuario invoque este comando, debes:

1. **Identificar el directorio del dia** que el usuario quiere documentar (ej: `src/2018/day1/`)

2. **Leer los archivos de solucion** (`part1.py`, `part2.py`, `index.py`) para entender que hace el codigo

3. **Identificar los conceptos de CS** que ilustra el ejercicio. Busca patrones como:
   - Estructuras de datos (hash tables, trees, graphs, heaps, stacks, queues)
   - Algoritmos (BFS, DFS, dynamic programming, greedy, backtracking, binary search)
   - Tecnicas (memoization, two pointers, sliding window, prefix sum, cycle detection)
   - Complejidad (trade-offs espacio/tiempo)

4. **Crear el archivo `concepts.md`** dentro de la carpeta del dia con este formato exacto:

```markdown
# Conceptos de CS - Day X (YEAR)

---

## 1. [Nombre del Concepto]

[Explicacion concisa del concepto - que es, como funciona, por que importa. Solo texto, SIN ejemplos de codigo. 2-4 parrafos maximo.]

---

## 2. [Siguiente Concepto]

[Misma estructura]

---

## Ejercicios de practica

- **LeetCode XXX** - Nombre (Concepto relacionado)
- **LeetCode XXX** - Nombre (Concepto relacionado)

---

# Conceptos Avanzados Relacionados

## [Nombre del Concepto] → Conceptos Avanzados

**Materias relacionadas:** [Lista de materias de CS donde se estudia este tema]

| Concepto Avanzado | Descripcion | Area de CS |
|-------------------|-------------|------------|
| **[Concepto 1]** | [Descripcion breve] | [Materia/Area] |
| **[Concepto 2]** | [Descripcion breve] | [Materia/Area] |
| **[Concepto 3]** | [Descripcion breve] | [Materia/Area] |

---

[Repetir para cada concepto identificado]

---

## Mapa Curricular

[Diagrama ASCII mostrando la progresion de los conceptos a traves de la carrera de CS]

```
Semestre 1-2:           Semestre 3-4:              Semestre 5+:
+─────────────────+     +──────────────────────+   +─────────────────────────+
| [Conceptos      | ──► | [Conceptos           |──►| [Conceptos              |
|  basicos]       |     |  intermedios]        |   |  avanzados]             |
+─────────────────+     +──────────────────────+   +─────────────────────────+
```

Los conceptos del Day X son **building blocks** que aparecen repetidamente en niveles superiores de la carrera.
```

## Reglas importantes

- **SIN ejemplos de codigo** - Solo texto explicativo
- **Conciso** - Cada concepto en 2-4 parrafos maximo
- **SI incluir ejercicios de LeetCode** relacionados al final
- El archivo se crea en la misma carpeta del dia: `src/YEAR/dayX/concepts.md`
- Usa acentos en espanol pero evita caracteres especiales en el markdown

## Reglas para Conceptos Avanzados

- **Por cada concepto basico**, crear una seccion de conceptos avanzados
- **Incluir 3-5 conceptos avanzados** por cada concepto basico en formato tabla
- **Materias relacionadas** deben ser materias reales de carreras de CS:
  - Estructuras de Datos, Algoritmos, Bases de Datos, Sistemas Operativos
  - Sistemas Distribuidos, Criptografia, Compiladores, Teoria de Grafos
  - Arquitectura de Computadoras, Computacion Paralela, etc.
- **El mapa curricular** debe mostrar progresion logica desde conceptos basicos hasta avanzados
- **Conectar con aplicaciones reales**: bases de datos (LSM Trees, Hash Joins), sistemas distribuidos (Consistent Hashing), criptografia (Pollard's Rho), etc.

## Argumento

El usuario debe proporcionar la ruta del dia, ejemplo:
- `src/2018/day1`
- `src/2025/day5`

Ruta proporcionada: $ARGUMENTS
