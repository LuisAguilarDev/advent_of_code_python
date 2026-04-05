from global_utils.utils import read_file
from global_utils.logger import logger

def parse_data(contents) -> list[list[str]]:
    positions = list()
    for line in contents:
        positions.append(tuple(list(map(int, line.split(",")))))
    return positions

def is_diagonal(pos1,pos2):
    r1,c1 = pos1
    r2,c2 = pos2
    if r1 == r2 or c1 == c2:
        return False
    return True

def get_area(pos1,pos2):
    r1, c1 = pos1
    r2,c2 = pos2
    w = abs(r1 - r2) + 1
    h = abs(c1 - c2) + 1
    return w * h

def get_biggest_area(positions: list[tuple[str, str]]) -> int:
    all_areas = list()
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            pos1 = positions[i]
            pos2 = positions[j]
            if is_diagonal(pos1,pos2):
                area = get_area(pos1,pos2)
                all_areas.append(area)
    return max(all_areas)

def do_part_1() -> bool:
    logger.info("Part 1")
    contents = read_file("data/input.txt")
    positions = parse_data(contents)
    sol = get_biggest_area(positions)
    logger.info(f"Biggest area: {sol}")
    return 4776487744 == sol