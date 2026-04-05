from collections import defaultdict
from global_utils.utils import read_file
from global_utils.logger import logger


def parse_data(lines):
    """
    returns an adjacency list {A:[B,C]}
    """
    adjacency_list = defaultdict(list)

    for line in lines:
        pre, step = line[5], line[36]
        adjacency_list[pre].append(step)

    return adjacency_list


def get_order(adjacency_list:dict) -> str:
    nodes = set()
    nodes_required = defaultdict(int)

    for step, neighbors in adjacency_list.items():
        nodes.add(step)
        for neighbor in neighbors:
            nodes.add(neighbor)
            nodes_required[neighbor] += 1

    available = sorted([n for n in nodes if nodes_required[n] == 0])

    result = ""
    while available:
        available.sort()
        current = available.pop(0)  # toma el primero alfabéticamente
        result += current
        for neighbor in adjacency_list[current]:
            nodes_required[neighbor] -= 1
            if nodes_required[neighbor] == 0:
                available.append(neighbor)

    return result

def do_part_1() -> bool:
    logger.info("Part 1")
    lines = read_file("data/input.txt")
    adjacency_list = parse_data(lines)
    order = get_order(adjacency_list)
    logger.info(f"order: {order}")
    return "BDHNEGOLQASVWYPXUMZJIKRTFC" == order
