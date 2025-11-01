import os
import re

# 1 ---- Day 1: Trebuchet?! ----
file_path = os.path.join(os.path.dirname(__file__), "day1.txt")

with open(file_path, "r") as file:
    contents = file.read().splitlines()

# Part 1
total = 0
for line in contents:
    list_number = re.findall(r'\d+', line)
    number = "".join(list_number)
    if not number:
        continue
    if len(number) == 1:
        total += int(number + number)
    else:
        total += int(number[0] + number[-1])

assert (total == 54573)

# Part 2
numbers = {"one": "1", "two": "2", "three": "3", "four": "4",
           "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}


def get_number(s: str):
    if s in numbers:
        return numbers[s]
    return s


# lookahead to capture overlapped patterns by default \ are escape in python 3.13.1
pattern = "(?=(" + "|".join(numbers.keys()) + "|\d))"
p = re.compile(pattern)

total = 0
for line in contents:
    matches = re.findall(p, line)
    if len(matches) == 0:
        continue
    nums = list(map(get_number, matches))
    total += int(nums[0] + nums[-1])

assert (total == 54591)
