from collections import Counter, defaultdict
from datetime import datetime

from global_utils.utils import read_file
from global_utils.logger import logger


def parse_data(lines):
    actions = list()
    for line in lines:
        parts = line.split("]")
        date = parts[0][1:]
        actions.append((date, parts[1].strip()))
    return actions


def get_naps_by_guard(sorted_actions):
    naps_by_guard = defaultdict(list)
    guard = 0
    start = 0
    for date, action in sorted_actions:
        minute = int(date.split(":")[1])
        if "begins shift" in action:
            guard = int(action.split("#")[1].split()[0])
        elif "falls asleep" in action:
            start = minute
        elif "wakes up" in action:
            naps_by_guard[guard].append((minute - start, start))
    return naps_by_guard


def get_best_minute(naps):
    counter = Counter()
    for duration, start in naps:
        counter.update(range(start, start + duration))
    return counter.most_common(1)[0]


def get_best_guard_and_minute(sorted_actions):
    naps_by_guard = get_naps_by_guard(sorted_actions)
    best_guard = -1
    best_minute = -1
    best_count = 0
    for guard, naps in naps_by_guard.items():
        minute, count = get_best_minute(naps)
        if count > best_count:
            best_count = count
            best_guard = guard
            best_minute = minute
    return best_guard, best_minute


def do_part_2() -> bool:
    logger.info("Part 2")
    lines = read_file("data/input.txt")
    actions = parse_data(lines)
    sorted_actions = sorted(actions, key=lambda x: datetime.strptime(
        x[0], "%Y-%m-%d %H:%M"))
    best_guard, best_minute = get_best_guard_and_minute(sorted_actions)
    result = best_guard * best_minute
    logger.info(f"Result: {result}")
    return 141071 == result
