from test_utils import load_module
from global_utils.utils import read_file

module = load_module("src/2023/day1")


def test_find_number_examples():
    assert module.find_number("1abc2") == 12
    assert module.find_number("pqr3stu8vwx") == 38
    assert module.find_number("a1b2c3d4e5f") == 15
    assert module.find_number("treb7uchet") == 77
    assert module.find_number("trebuchet") == 0


def test_sum_calibration_examples():
    lines = read_file("test/2023/day1/sample1.txt")
    assert module.sum_calibration(lines) == 142


def test_part1_input_answer():
    lines = read_file("src/2023/day1/input.txt")
    assert module.sum_calibration(lines) == 54573
