from collections import Counter, defaultdict
from datetime import datetime

from global_utils.utils import read_file
from global_utils.logger import logger


def parse_data(lines: list[str]) -> dict[int, list[tuple[int, int]]]:
    """
    Parses raw log lines into datetime-action pairs, and returns nap
    intervals grouped by guard ID.
    
    Args:
        lines: Raw log lines in format "[YYYY-MM-DD HH:MM] action"
    
    Returns:
        Dict mapping guard ID to list of (min_sleep_start, min_wake_up) tuples.
    """
    actions = list()
    for line in lines:
        parts = line.split("]")
        date = datetime.strptime(parts[0][1:], "%Y-%m-%d %H:%M")
        actions.append((date, parts[1].strip()))
    return get_naps_by_guard(actions)


def get_naps_by_guard(actions: list[tuple[datetime, str]]):
    """
    Groups nap intervals by guard ID from a chronologically sorted list of actions.

    Args:
        sorted_actions: Sorted list of (datetime, action_string) tuples.

    Returns:
        Dict mapping guard ID to list of (min_sleep_start, min_wake_up) minute tuples.
    """
    actions =sorted(actions)
    naps_by_guard = defaultdict(list)
    guard, start = None, None
    for date, action in actions:
        minute = date.minute
        if "begins shift" in action:
            guard = int(action.split("#")[1].split()[0])
        elif "falls asleep" in action:
            start = minute
        elif "wakes up" in action:
            naps_by_guard[guard].append((start, minute - 1))
    return naps_by_guard


def get_best_minute(naps):
    """
    Finds the minute most frequently slept through across all nap intervals for a guard.

    Args:
        naps_by_guard: List of (min_sleep_start, min_wake_up) minute tuples.

    Returns:
        The minute with the highest sleep frequency.
    """
    counter = Counter() # {minute: count}
    for start, end in naps:
        counter.update(range(start, end + 1))
    return counter.most_common(1)[0][0]


def get_best_guard_and_minute(naps_by_guard):
    """
    Finds the guard with the most total sleep time and their most frequently slept minute.

    Args:
        naps_by_guard: Dict mapping guard ID to list of (min_sleep_start, min_wake_up) minute tuples.

    Returns:
        Tuple of (guard_id, most_slept_minute).
    """
    guard = max(naps_by_guard, key=lambda g: sum(end - start for start, end in naps_by_guard[g]))
    minute = get_best_minute(naps_by_guard[guard])
    return (guard, minute)


def do_part_1() -> bool:
    logger.info("Part 1")
    lines = read_file("data/input.txt")
    naps_by_guard = parse_data(lines)
    best_guard, best_minute = get_best_guard_and_minute(naps_by_guard)
    result = best_guard * best_minute
    logger.info(f"Result: {result}")
    return 38813 == result
