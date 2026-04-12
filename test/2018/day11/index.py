from test_utils import load_module
from global_utils.utils import read_file

part1 = load_module("src/2018/day11/part1.py")

# Part 1

def test_different_units_no_reaction():
    result = part1.get_power_level(3,5,8)
    assert result == 4
    result = part1.get_power_level(122,79,57)
    assert result == -5
    result = part1.get_power_level(217,196,39)
    assert result == 0
    result = part1.get_power_level(101,153,71)
    assert result == 4