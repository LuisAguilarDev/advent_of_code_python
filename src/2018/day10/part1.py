import re
from collections import deque

from constants.constants import all_directions
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


def find_message_time(points: list[tuple[int, int, int, int]]) -> int:
    """Find the time when points converge to form a message using BFS clustering."""
    n = len(points)
    max_cluster_size = 0
    best_time = 0

    for t in range(1, 20000):
        positions = [(px + vx * t, py + vy * t) for px, py, vx, vy in points]
        positions_set = set(positions)
        visited: set[tuple[int, int]] = set()

        for pos in positions:
            if pos not in visited:
                cluster_size = bfs(pos, positions_set, visited)
                if cluster_size > max_cluster_size:
                    max_cluster_size = cluster_size
                    best_time = t

        if max_cluster_size > n * 0.5:
            break

    return best_time


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
    logger.info("Part 1")
    lines: list[str] = read_file("data/input.txt")
    points = parse_data(lines)
    # t = find_message_time(points)
    # message = render_message(points, t)
    t = 10831
    message = render_message(points, t)
    logger.info(f"Message at t={t}:\n{message}")
    return True
