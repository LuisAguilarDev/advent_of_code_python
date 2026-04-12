import re

from src.constants.constants import all_directions
from global_utils.utils import read_file
from global_utils.logger import logger


def parse_data(lines: list[str]) -> list[tuple[int, int, int, int]]:
    """
    Parse input lines into a list of (px, py, vx, vy) tuples.
    Each line has the format: 'position=< x, y> velocity=< vx, vy>'.
    Uses regex to extract all integers (including negatives).
    """
    points: list[tuple[int, int, int, int]] = []
    for line in lines:
        nums: list[int] = list(map(int, re.findall(r"-?\d+", line)))
        points.append((nums[0], nums[1], nums[2], nums[3]))
    return points


def find_message_time(points: list[tuple[int, int, int, int]]) -> int:
    """
    Iterate second by second until all points form a connected message.
    At each time step t, computes every point's position as:
        (px + vx * t, py + vy * t)
    Stops when no point is isolated (i.e., every point has at least one neighbor).
    Returns the time t at which the message appears.
    """
    t: int = 0
    while True:
        positions: list[tuple[int, int]] = [
            (px + vx * t, py + vy * t) for px, py, vx, vy in points
        ]
        positions_set: set[tuple[int, int]] = set(positions)

        if validate_groups(positions_set):
            break
        t += 1

    return t


def validate_groups(positions_set: set[tuple[int, int]]) -> bool:
    """
    Check whether all points are connected to at least one neighbor.
    For each point, scans its 8 surrounding cells (all directions).
    If any point has zero neighbors, the points are still scattered → returns False.
    When every point has at least one neighbor, the message is formed → returns True.
    """
    for pos in positions_set:
        x, y = pos
        has_neighbor: bool = False

        for dx, dy in all_directions:
            neighbor_x: int = x + dx
            neighbor_y: int = y + dy
            neighbor: tuple[int, int] = (neighbor_x, neighbor_y)

            if neighbor in positions_set:
                has_neighbor = True
                break

        if not has_neighbor:
            return False

    return True


def render_message(points: list[tuple[int, int, int, int]], t: int) -> str:
    """
    Render the sky grid at time t as a human-readable string.
    Computes the bounding box from min/max X and Y across all points,
    then builds each row left-to-right: '#' where a point exists, '.' otherwise.
    Returns the full grid as a newline-separated string.
    """
    positions: set[tuple[int, int]] = set(
        (px + vx * t, py + vy * t) for px, py, vx, vy in points
    )
    min_x = min(p[0] for p in positions)
    max_x = max(p[0] for p in positions)
    min_y = min(p[1] for p in positions)
    max_y = max(p[1] for p in positions)

    lines: list[str] = []
    for y in range(min_y, max_y + 1):
        row: str = ""
        for x in range(min_x, max_x + 1):
            row += "#" if (x, y) in positions else "."
        lines.append(row)

    return "\n".join(lines)


def do_part_1() -> bool:
    """
    Entry point for Day 10.
    Reads the input, finds the time the message appears (Part 2),
    renders and logs the message grid (Part 1), and logs the time (Part 2).
    Returns True on successful execution.
    """
    lines: list[str] = read_file("data/input.txt")
    points = parse_data(lines)
    t = find_message_time(points)
    message = render_message(points, t)
    logger.info("Part 1")
    logger.info(f"Message:\n{message}")
    logger.info("Part 2")
    logger.info(f"Message appeared at t={t} seconds")
    return True
