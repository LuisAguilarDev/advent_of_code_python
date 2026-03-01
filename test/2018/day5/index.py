from test_utils import load_module
from global_utils.utils import read_file

part1 = load_module("src/2018/day5/part1.py")

sample = read_file("test/2018/day5/sample.txt")

# Part 1

## Caso 1: Distintas unidades - no reaccionan
def test_different_units_no_reaction():
    result = part1.get_reacted_polymer("AB")
    assert len(result) == 2
    assert result == "AB"


## Caso 2: Misma unidad distintas polaridades - se destruyen
def test_same_unit_different_polarity():
    result = part1.get_reacted_polymer("Aa")
    assert len(result) == 0
    assert result == ""


## Caso 3a: Reaccion en cadena destruye el polimero completo
def test_chain_reaction_destroys_polymer():
    result = part1.get_reacted_polymer("BAab")
    assert len(result) == 0
    assert result == ""


## Caso 3b: Reaccion en cadena no destruye el polimero
def test_chain_reaction_partial():
    result = part1.get_reacted_polymer("CAab")
    assert len(result) == 2
    assert result == "Cb"


## Caso 4: Ejemplo conocido del problema
def test_sample():
    result = part1.get_reacted_polymer(sample)
    assert len(result) == 10
    assert result == "dabCBAcaDA"


## Caso 5: Cadena vacia
def test_empty_string():
    result = part1.get_reacted_polymer("")
    assert len(result) == 0
    assert result == ""


## Caso 6: Un solo caracter - no puede reaccionar
def test_single_character():
    result = part1.get_reacted_polymer("z")
    assert len(result) == 1
    assert result == "z"


## Caso 7: Mismo tipo misma polaridad - no reaccionan
def test_same_type_same_polarity():
    assert part1.get_reacted_polymer("aa") == "aa"
