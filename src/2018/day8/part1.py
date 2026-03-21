from global_utils.utils import read_file
from global_utils.logger import logger


def sum_metadata(numbers):
    q_children = numbers.pop(0)
    q_metadata = numbers.pop(0)

    total = 0
    for _ in range(q_children):
        total += sum_metadata(numbers)

    for _ in range(q_metadata):
        total += numbers.pop(0)

    return total


def do_part_1() -> bool:
    logger.info("Part 1")
    lines = read_file("data/input.txt")
    numbers = [int(x) for x in lines[0].split()]
    total = sum_metadata(numbers)
    logger.info(f"total: {total}")
    return True
