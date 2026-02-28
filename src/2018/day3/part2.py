from global_utils.utils import read_file
from global_utils.logger import logger


def get_coordinates(r, c, w, h):
    coordinates = set()
    for dr in range(h):
        for dc in range(w):
            coordinates.add((r + dr, c + dc))
    return coordinates


def parse_data(lines):
    pieces = list()
    for line in lines:
        parts = line.split(" ")
        claim_id = int(parts[0][1:])
        c_r = parts[2].split(",")
        c = int(c_r[0])
        r = int(c_r[1][:-1])
        size = parts[3].split("x")
        w = int(size[0])
        h = int(size[1])
        pieces.append((claim_id, (r,c,w,h)))
    return pieces

def are_overlapped(area_1,area_2):
    r1, c1, w1, h1 = area_1
    r2, c2, w2, h2 = area_2
    horizontal_overlapped = (c1 <= c2 + w2) and (c2 <= c1 + w1)
    vertical_overlapped = (r1 <= r2 + h2) and (r2 <= r1 + h1)
    return horizontal_overlapped and vertical_overlapped

def get_not_overlaped_id(pieces):
    overlapped = set()
    all_ids = {id for id,_ in pieces}
    for i in range(len(pieces)):
        for j in range(i+1, len(pieces)):
            id_1,area_1 = pieces[i]
            id_2,area_2 = pieces[j]
            if are_overlapped(area_1, area_2):
                overlapped.add(id_1)
                overlapped.add(id_2)
    return (all_ids - overlapped).pop()

def do_part_2() -> bool:
    logger.info("Part 2")
    lines = read_file("data/input.txt")
    pieces = parse_data(lines)
    not_overlaped_id = get_not_overlaped_id(pieces)
    logger.info(f"Not overlaped ID: {not_overlaped_id}")
    return 382 == not_overlaped_id
