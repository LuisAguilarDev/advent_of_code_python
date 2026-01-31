from global_utils.utils import read_file
from global_utils.logger import logger


def parse_data(lines):
    claims = list()
    for line in lines:
        parts = line.split(" ")
        claim_id = int(parts[0][1:])
        c_r = parts[2].split(",")
        c = int(c_r[0])
        r = int(c_r[1][:-1])
        size = parts[3].split("x")
        w = int(size[0])
        h = int(size[1])
        claims.append((claim_id, r, c, w, h))
    return claims


def get_not_overlaped_id(claims):
    visited_dict = dict()    # to store the id
    overlapped = set()
    visited = set()
    for id, r, c, w, h in claims:
        visited.add(id)
        for dr in range(h):
            for dc in range(w):
                square = (r + dr, c + dc)
                if square in visited_dict:
                    overlapped.add(visited_dict[square])
                    overlapped.add(id)
                else:
                    visited_dict[square] = id
    return (visited - overlapped).pop()

def do_part_2() -> bool:
    logger.info("Part 1")
    lines = read_file("data/input.txt")
    claims = parse_data(lines)
    not_overlaped_id = get_not_overlaped_id(claims)
    logger.info(f"Not overlaped ID: {not_overlaped_id}")
    return 382 == not_overlaped_id
