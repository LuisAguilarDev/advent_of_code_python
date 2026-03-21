from global_utils.utils import read_file
from global_utils.logger import logger


def node_value(numbers):
    q_children = numbers.pop(0)
    q_metadata = numbers.pop(0)

    if q_children == 0:
        total = 0
        for _ in range(q_metadata):
            total += numbers.pop(0)
        return total

    children_values = []
    for _ in range(q_children):
        children_values.append(node_value(numbers))

    total = 0
    for _ in range(q_metadata):
        index = numbers.pop(0)
        # if in range we add it otherwise its 0 unreferenced child
        if 1 <= index <= q_children:
            total += children_values[index - 1]

    return total


def do_part_2() -> bool:
    logger.info("Part 2")
    lines = read_file("data/input.txt")
    numbers = [int(x) for x in lines[0].split()]
    total = node_value(numbers)
    logger.info(f"total: {total}")
    return True
