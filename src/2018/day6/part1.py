from collections import Counter
from global_utils.utils import read_file
from global_utils.logger import logger


def parse_data(lines):
    coordinates = list()
    for line in lines:
        x, y = map(lambda val: int(val.strip()),line.split(","))
        coordinates.append((x,y))
    return coordinates


def get_edges(coordinates):
    x_max = x_min = y_max = y_min = 0
    for x,y in coordinates:
        x_max = max(x,x_max)
        x_min = min(x,x_min)
        y_max = max(y,y_max)
        y_min = min(y,y_min)
    return x_max,x_min,y_max,y_min


def get_closest(place, coordinates):
    best_place, closest_distance = None, float("inf")
    c_x, c_y = place

    for i, (x, y) in enumerate(coordinates):
        distance = abs(x - c_x) + abs(y - c_y)
        if distance < closest_distance:
            best_place = i
            closest_distance = distance
        elif distance == closest_distance:  # tie → reset to None
            best_place = None

    return best_place


def get_biggest_area(coordinates):
    x_max, x_min, y_max, y_min = get_edges(coordinates)
    counter = Counter()
    infinites_area = set()
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            index = get_closest((x, y), coordinates)
            if index is not None:
                counter[index] += 1
                if x == x_min or x == x_max or y == y_min or y == y_max:
                    infinites_area.add(index)
    for index in infinites_area:
        counter.pop(index, None)
    return max(counter.values())


def do_part_1() -> bool:
    logger.info("Part 1")
    lines = read_file("data/input.txt")
    coordinates = parse_data(lines)
    area = get_biggest_area(coordinates)
    logger.info(f"area: {area}")
    return 3687 == area
