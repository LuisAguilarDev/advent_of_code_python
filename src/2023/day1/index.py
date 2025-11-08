import re
from global_utils.utils import read_file
from global_utils.logger import logger

logger.info("---- Day 1: Trebuchet?! ----")

# Part 1
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
test = sum_calibration(["1asdasdasd6"])
assert (test == 16)
test2 = sum_calibration(["asdasdasd"])
assert (test2 == 0)

assert (result == 54573)

# Part 2
# numbers = {"one": "1", "two": "2", "three": "3", "four": "4",
#            "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}


# def get_number(s: str):
#     if s in numbers:
#         return numbers[s]
#     return s


# # lookahead to capture overlapped patterns by default \ are escape in python 3.13.1
# pattern = "(?=(" + "|".join(numbers.keys()) + "|\d))"
# p = re.compile(pattern)

# total = 0
# for line in contents:
#     matches = re.findall(p, line)
#     if len(matches) == 0:
#         continue
#     nums = list(map(get_number, matches))
#     total += int(nums[0] + nums[-1])

# assert (total == 54591)
