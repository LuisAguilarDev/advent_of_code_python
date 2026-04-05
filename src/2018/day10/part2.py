from global_utils.utils import read_file
from global_utils.logger import logger

from .part1 import parse_data, find_message_time


def do_part_2() -> bool:
    logger.info("Part 2")
    lines: list[str] = read_file("data/input.txt")
    points = parse_data(lines)
    result: int = find_message_time(points)
    logger.info(f"result: {result}")
    return True
