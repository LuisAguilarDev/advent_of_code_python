from test_utils import load_module

part1 = load_module("src/2018/day3/part1.py")
part2 = load_module("src/2018/day3/part2.py")

# Part 1

## Caso 1: No se sobreponen
def test_no_overlap():
    registers = part1.parse_data([
        "#1 @ 1,1: 1x1",
        "#2 @ 2,2: 1x1",
    ])
    assert part1.get_total_overlaped(registers) == 0


## Caso 2: Se sobreponen
def test_overlap():
    registers = part1.parse_data([
        "#1 @ 1,1: 2x2",
        "#2 @ 2,2: 2x2",
    ])
    assert part1.get_total_overlaped(registers) == 1


## Caso 3: Esta contenido
def test_contained():
    registers = part1.parse_data([
        "#1 @ 1,1: 3x3",
        "#2 @ 2,2: 1x1",
    ])
    assert part1.get_total_overlaped(registers) == 1


## Caso 4: Se sobrepone con mas de un registro
def test_overlap_multiple():
    registers = part1.parse_data([
        "#1 @ 1,1: 3x3",
        "#2 @ 3,0: 2x2",
        "#3 @ 3,3: 2x2",
    ])
    assert part1.get_total_overlaped(registers) == 2


## Caso 5: Son iguales
def test_equal():
    registers = part1.parse_data([
        "#1 @ 1,1: 3x3",
        "#2 @ 1,1: 3x3",
    ])
    assert part1.get_total_overlaped(registers) == 9


## Caso 6: Un solo registro
def test_single_claim():
    registers = part1.parse_data([
        "#1 @ 1,1: 3x3",
    ])
    assert part1.get_total_overlaped(registers) == 0


## Caso 7: Tres iguales
def test_three_equal():
    registers = part1.parse_data([
        "#1 @ 1,1: 3x3",
        "#2 @ 1,1: 3x3",
        "#3 @ 1,1: 3x3",
    ])
    assert part1.get_total_overlaped(registers) == 9


## Caso 8: Se tocan
def test_touching():
    registers = part1.parse_data([
        "#1 @ 1,1: 2x2",
        "#2 @ 3,1: 2x2",
    ])
    assert part1.get_total_overlaped(registers) == 0

# Part 2

## Caso 1: El ultimo no se sobrepone
def test_last_not_overlapped():
    registers = part2.parse_data([
        "#1 @ 1,1: 2x2",
        "#2 @ 2,2: 2x2",
        "#3 @ 4,4: 1x1",
    ])
    assert part2.get_not_overlaped_id(registers) == 3


## Caso 2: El primero no se sobrepone
def test_first_not_overlapped():
    registers = part2.parse_data([
        "#1 @ 4,4: 1x1",
        "#2 @ 1,1: 2x2",
        "#3 @ 2,2: 2x2",
    ])
    assert part2.get_not_overlaped_id(registers) == 1


## Caso 3: El del medio no se sobrepone
def test_middle_not_overlapped():
    registers = part2.parse_data([
        "#1 @ 1,1: 2x2",
        "#2 @ 4,4: 1x1",
        "#3 @ 2,2: 2x2",
    ])
    assert part2.get_not_overlaped_id(registers) == 2


## Caso 4: Uno contenido, otro aparte
def test_contained_with_separate():
    registers = part2.parse_data([
        "#1 @ 1,1: 3x3",
        "#2 @ 2,2: 1x1",
        "#3 @ 4,4: 1x1",
    ])
    assert part2.get_not_overlaped_id(registers) == 3


## Caso 5: Cadena de solapamientos
def test_chain_overlap():
    registers = part2.parse_data([
        "#1 @ 0,0: 2x2",
        "#2 @ 1,1: 2x2",
        "#3 @ 2,2: 2x2",
        "#4 @ 4,4: 1x1",
    ])
    assert part2.get_not_overlaped_id(registers) == 4


## Caso 6: Multiples se solapan con uno, otro aparte
def test_multiple_overlap_one_separate():
    registers = part2.parse_data([
        "#1 @ 2,4: 1x1",
        "#2 @ 1,1: 3x3",
        "#3 @ 3,0: 2x2",
        "#4 @ 3,3: 2x2",
    ])
    assert part2.get_not_overlaped_id(registers) == 1
