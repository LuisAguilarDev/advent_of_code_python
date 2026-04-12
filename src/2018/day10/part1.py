import re
from collections import deque

from src.constants.constants import all_directions
from global_utils.utils import read_file
from global_utils.logger import logger


def parse_data(lines: list[str]) -> list[tuple[int, int, int, int]]:
    """Parse 'position=< x, y> velocity=< vx, vy>'."""
    points = []
    for line in lines:
        nums = list(map(int, re.findall(r"-?\d+", line)))
        points.append((nums[0], nums[1], nums[2], nums[3]))
    return points


def bfs(start: tuple[int, int], positions_set: set, visited: set) -> int:
    visited.add(start)
    queue = deque([start])
    count = 0
    while queue:
        x, y = queue.popleft()
        count += 1
        for dx, dy in all_directions:
            neighbor = (x + dx, y + dy)
            if neighbor in positions_set and neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return count

# Lo mas importante es mostrar el proceso de pensamiento, no el resultado final.
# El resultado final es solo una consecuencia de un proceso de razonamiento riguroso y meticuloso.

def find_message_time(points: list[tuple[int, int, int, int]]) -> int:
    """Find the time when points converge to form a message using BFS clustering."""
    t = 0
    while True:
        positions = [(px + vx * t, py + vy * t) for px, py, vx, vy in points]
        positions_set = set(positions)
        
        is_valid = validate_groups(positions_set)
        if is_valid:
            break
        t += 1 
    return t


def validate_groups(positions_set: set[tuple[int, int]]) -> bool:
    """Return True if no point is completely isolated (all points are connected)."""

    for pos in positions_set:
        x, y = pos
        has_neighbor = False
        for dx, dy in all_directions:
            neighbor_x = x + dx
            neighbor_y = y + dy
            neighbor = (neighbor_x, neighbor_y)

            if neighbor in positions_set:
                has_neighbor = True
                break
        if not has_neighbor:
            return False  # isolated point found → not the message yet

    return True

def render_message(points: list[tuple[int, int, int, int]], t: int) -> str:
    positions = set((px + vx * t, py + vy * t) for px, py, vx, vy in points)
    min_x = min(p[0] for p in positions)
    max_x = max(p[0] for p in positions)
    min_y = min(p[1] for p in positions)
    max_y = max(p[1] for p in positions)

    lines = []
    for y in range(min_y, max_y + 1):
        row = ""
        for x in range(min_x, max_x + 1):
            row += "#" if (x, y) in positions else "."
        lines.append(row)
    return "\n".join(lines)


def do_part_1() -> bool:
    lines: list[str] = read_file("data/input.txt")
    points = parse_data(lines)
    t = find_message_time(points)
    message = render_message(points, t)
    logger.info("Part 1")
    logger.info(f"Message:\n{message}")
    logger.info("Part 2")
    logger.info(f"Message show at time={t}")
    return True
