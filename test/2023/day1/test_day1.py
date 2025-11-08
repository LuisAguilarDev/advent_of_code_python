from test_utils import load_module
from global_utils.utils import read_file

module = load_module("src/2023/day1")

input = read_file("src/2023/day1/input.txt")
sample1 = read_file("test/2023/day1/sample1.txt")
sample2 = read_file("test/2023/day1/sample2.txt")


def test_find_number_examples():
    assert module.find_number("1abc2") == 12
    assert module.find_number("pqr3stu8vwx") == 38
    assert module.find_number("a1b2c3d4e5f") == 15
    assert module.find_number("treb7uchet") == 77
    assert module.find_number("trebuchet") == 0


def test_sum_calibration_examples():

    assert module.sum_calibration(sample1) == 142


def test_part1_input_answer():

    assert module.sum_calibration(input) == 54573


def sum_calibration_should_continue_if_not_coincidence_was_found():
    assert 0 == module.sum_calibration_letters(
        ["nonumbershere", "alsononumbershere"])


def test_part2_input_answer():

    assert module.sum_calibration_letters(input) == 54591
