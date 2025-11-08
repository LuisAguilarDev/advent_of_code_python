import re
from global_utils.utils import read_file
from global_utils.logger import logger

logger.info("---- Day 1: Trebuchet?! ----")

logger.info("Part 1")
contents = read_file("input.txt")


def find_number(s: str):
    numbers = re.findall(r'\d+', s)
    number = "".join(numbers)
    if not number:
        return 0
    if len(number) == 1:
        return int(number + number)
    return int(number[0] + number[-1])


def sum_calibration(contents: list[str]) -> int:
    total = 0
    for item in contents:
        total += find_number(item)
    return total


result = sum_calibration(contents)
logger.info(f"Sum of calibrations: {result}")
test = sum_calibration(["1asdasdasd6"])
assert (test == 16)
test2 = sum_calibration(["asdasdasd"])
assert (test2 == 0)

assert (result == 54573)

logger.info("Part 2")
dict_numbers = {"one": "1", "two": "2", "three": "3", "four": "4",
                "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}


def get_number_from_dict(s: str):
    if s in dict_numbers:
        return dict_numbers[s]
    return s


def get_coincidende_numbers_from_string(s: str):
    pattern = "(?=(" + "|".join(dict_numbers.keys()) + "|\d))"
    p = re.compile(pattern)
    return p.findall(s)


def sum_calibration_letters(contents: list[str]) -> int:
    total = 0
    for line in contents:
        matches = get_coincidende_numbers_from_string(line)
        if len(matches) == 0:
            continue
        nums = list(map(get_number_from_dict, matches))
        total += int(nums[0] + nums[-1])
    return total


assert 0 == sum_calibration_letters(
    ["nonumbershere", "alsononumbershere"])
total = sum_calibration_letters(contents)
logger.info(f"Sum of calibrations with letters: {total}")
assert (total == 54591)
