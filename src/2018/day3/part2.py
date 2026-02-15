from global_utils.utils import read_file
from global_utils.logger import logger


def get_coordinates(r, c, w, h):
    coordinates = set()
    for dr in range(h):
        for dc in range(w):
            coordinates.add((r + dr, c + dc))
    return coordinates


def parse_data(lines):
    registers = list()
    for line in lines:
        parts = line.split(" ")
        claim_id = int(parts[0][1:])
        c_r = parts[2].split(",")
        c = int(c_r[0])
        r = int(c_r[1][:-1])
        size = parts[3].split("x")
        w = int(size[0])
        h = int(size[1])
        registers.append((claim_id, get_coordinates(r, c, w, h)))
    return registers


def get_not_overlaped_id(registers):
    owners = dict() # coordinate -> register id
    overlapped = set()
    visited = set()
    for id, coordinates in registers:
        visited.add(id)
        for coordinate in coordinates:
            if coordinate in owners:
                overlapped.add(owners[coordinate])
                overlapped.add(id)
            else:
                owners[coordinate] = id
    return (visited - overlapped).pop()

def do_part_2() -> bool:
    logger.info("Part 2")
    lines = read_file("data/input.txt")
    registers = parse_data(lines)
    not_overlaped_id = get_not_overlaped_id(registers)
    logger.info(f"Not overlaped ID: {not_overlaped_id}")
    return 382 == not_overlaped_id
