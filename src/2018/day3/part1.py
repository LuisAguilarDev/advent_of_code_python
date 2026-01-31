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

def get_total_overlaped(claims):
    overlaped = set()
    visited = set()
    for _, r, c, w, h in claims:
        for dr in range(h):
            for dc in range(w):
                square = (r + dr, c + dc)
                if square in visited:
                    overlaped.add(square)
                    continue
                else:
                    visited.add(square)
    return len(overlaped)

def do_part_1() -> bool:
    logger.info("Part 1")
    lines = read_file("data/input.txt")
    claims = parse_data(lines)
    total = get_total_overlaped(claims)
    logger.info(f"Total: {total}")
    return 116920 == total
