from global_utils.utils import read_file
from global_utils.logger import logger


def node_value(numbers: list[int]) -> int:
    """Recursively computes the value of a node encoded in a flat list.

    - If a node has no children, its value is the sum of its metadata.
    - If a node has children, each metadata entry is a 1-based index into the
      children list. The node's value is the sum of the referenced children's values.
      Out-of-range indices are skipped (contribute 0).

    Args:
        numbers: Flat list of integers representing the serialized tree. Modified in place.

    Returns:
        The computed value of this node.
    """
    q_children = numbers.pop(0)
    q_metadata = numbers.pop(0)

    if q_children == 0:
        total = 0
        for _ in range(q_metadata):
            total += numbers.pop(0)
        return total

    children_values: list[int] = []
    for _ in range(q_children):
        children_values.append(node_value(numbers))

    total = 0
    for _ in range(q_metadata):
        index: int = numbers.pop(0)
        if 1 <= index <= q_children:
            total += children_values[index - 1]

    return total


def do_part_2() -> bool:
    logger.info("Part 2")
    lines: list[str] = read_file("data/input.txt")
    numbers: list[int] = [int(x) for x in lines[0].split()]
    total: int = node_value(numbers)
    logger.info(f"total: {total}")
    return 20815 == total
