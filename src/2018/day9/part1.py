import re

from global_utils.utils import read_file
from global_utils.logger import logger


def parse_data(text: str) -> tuple[int, int]:
    """Parse '476 players; last marble is worth 71431 points'."""
    m = re.search(r"(\d+)\s+players.*?worth\s+(\d+)", text)
    if not m:
        raise ValueError(f"Cannot parse input: {text}")
    return int(m.group(1)), int(m.group(2))

#Separar la logica de la implementacion
def solve(num_players: int, last_marble: int) -> int:
    """Simulate the marble game and return the winning score.

    Uses a naive list-based approach with O(n) inserts and removals.
    """
    circle = [0]
    current = 0
    scores = [0] * num_players

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            player = (marble - 1) % num_players
            scores[player] += marble
            current = (current - 7) % len(circle)
            scores[player] += circle.pop(current)
            if current >= len(circle):
                current = 0
        else:
            insert_at = (current + 2) % len(circle)
            if insert_at == 0:
                insert_at = len(circle)
            circle.insert(insert_at, marble)
            current = insert_at

    return max(scores)


def do_part_1() -> bool:
    logger.info("Part 1")
    lines: list[str] = read_file("data/input.txt")
    num_players, last_marble = parse_data(lines[0])
    result: int = solve(num_players, last_marble)
    logger.info(f"result: {result}")
    return 384205 == result
