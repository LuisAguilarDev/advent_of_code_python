from global_utils.utils import read_file
from global_utils.logger import logger


def sum_metadata(numbers: list[int]) -> int:
    """Recursively traverses the tree encoded in a flat list and sums all metadata entries.

    Consumes elements from `numbers` via pop(0) as it traverses.
    Each node is encoded as: [q_children, q_metadata, ...children_data..., ...metadata...]

    Args:
        numbers: Flat list of integers representing the serialized tree. Modified in place.

    Returns:
        The sum of all metadata entries across all nodes in this subtree.
    """
    q_children = numbers.pop(0)
    q_metadata = numbers.pop(0)

    total = 0
    for _ in range(q_children):
        total += sum_metadata(numbers)

    for _ in range(q_metadata):
        total += numbers.pop(0)

    return total


def do_part_1() -> bool:
    logger.info("Part 1")
    lines: list[str] = read_file("data/input.txt")
    numbers: list[int] = [int(x) for x in lines[0].split()]
    total: int = sum_metadata(numbers)
    logger.info(f"total: {total}")
    return 37439 == total
