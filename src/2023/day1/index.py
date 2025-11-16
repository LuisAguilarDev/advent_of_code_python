import re
from global_utils.utils import read_file
from global_utils.logger import logger


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


def get_number_from_dict(s: str):
    dict_numbers = {"one": "1", "two": "2", "three": "3", "four": "4",
                    "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    if s in dict_numbers:
        return dict_numbers[s]
    return s


def get_coincidende_numbers_from_string(s: str):
    pattern = "(?=(" + "one|two|three|four|five|six|seven|eight|nine" + "|\d))"
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


def do_part_1() -> bool:
    logger.info("Part 1")
    contents = read_file("input.txt")
    return 54573 == sum_calibration(contents)


def do_part_2() -> bool:
    logger.info(f"Part 2")
    contents = read_file("input.txt")
    return 54591 == sum_calibration_letters(contents)


def main():
    logger.info("---- Day 1: Trebuchet?! ----")
    result_part_1 = do_part_1()
    assert (True == result_part_1)
    result_part_2 = do_part_2()
    assert (True == result_part_2)


if __name__ == "__main__":
    main()
