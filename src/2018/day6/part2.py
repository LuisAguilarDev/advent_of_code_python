from collections import Counter
from global_utils.utils import read_file
from global_utils.logger import logger


def parse_data(lines):
    coordinates = list()
    for line in lines:
        x, y = map(lambda val: int(val.strip()), line.split(","))
        coordinates.append((x, y))
    return coordinates


def get_edges(coordinates):
    x_max = x_min = y_max = y_min = 0
    for x, y in coordinates:
        x_max = max(x, x_max)
        x_min = min(x, x_min)
        y_max = max(y, y_max)
        y_min = min(y, y_min)
    return x_max, x_min, y_max, y_min


def get_safe_region(coordinates, max_distance=10000):
    x_max, x_min, y_max, y_min = get_edges(coordinates)
    count = 0
    for x in range(x_min - 1, x_max + 1):
        for y in range(y_min - 1, y_max + 1):
            total = sum(abs(x - cx) + abs(y - cy) for cx, cy in coordinates)
            if total < max_distance:
                count += 1
    return count


def do_part_2() -> bool:
    logger.info("Part 2")
    lines = read_file("data/input.txt")
    coordinates = parse_data(lines)
    size = get_safe_region(coordinates)
    logger.info(f"region size: {size}")
    return 40134 == size
