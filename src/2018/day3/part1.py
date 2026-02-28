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
        registers.append((claim_id, (r,c,w,h)))
    return registers

def get_total_overlaped(registers):
    overlapped = set()
    visited = set()
    for _, rectangle in registers:
        coordinates = get_coordinates(*rectangle)
        for coordinate in coordinates:
            if coordinate in visited:
                overlapped.add(coordinate)
            else:
                visited.add(coordinate)
    return len(overlapped)

def do_part_1() -> bool:
    logger.info("Part 1")
    lines = read_file("data/input.txt")
    registers = parse_data(lines)
    total = get_total_overlaped(registers)
    logger.info(f"Total: {total}")
    return 116920 == total
