from test_utils import load_module
from global_utils.utils import read_file
import pytest

part1 = load_module("src/2018/day1/part1.py")
part2 = load_module("src/2018/day1/part2.py")

sample = read_file("test/2018/day1/sample.txt")

def test_sum_values_examples():
    assert part1.sum_values([]) == 0
    assert part1.sum_values(["+1"]) == 1
    assert part1.sum_values(["-1"]) == -1
    assert part1.sum_values(["-1", "+1"]) == 0
    assert part1.sum_values(sample) == -1


def test_get_first_repeated_total_examples():
    with pytest.raises(TypeError, match="missing 1 required positional argument"):
        part2.get_first_repeated_total()
    assert part2.get_first_repeated_total([]) == 0
    assert part2.get_first_repeated_total(["+1","+2","-3"]) == 0
    assert part2.get_first_repeated_total(["+1", "+2", "-1"]) == 3
