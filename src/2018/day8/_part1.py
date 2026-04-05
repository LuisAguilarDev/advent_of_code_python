from typing import TypedDict
from global_utils.utils import read_file
from global_utils.logger import logger


class TreeNode(TypedDict):
    children: list["TreeNode"]
    metadata: list[int]


def parse_tree(numbers: list[int]) -> TreeNode:
    """Parses a flat list of integers into a tree structure.

    Consumes elements from `numbers` via pop(0) as it builds the tree recursively.
    Each node is encoded as: [q_children, q_metadata, ...children_data..., ...metadata...]

    Args:
        numbers: Flat list of integers representing the serialized tree. Modified in place.

    Returns:
        A TreeNode dict with 'children' (list of TreeNode) and 'metadata' (list of int).
    """
    q_children: int = numbers.pop(0)
    q_metadata: int = numbers.pop(0)

    children: list[TreeNode] = [parse_tree(numbers) for _ in range(q_children)]
    metadata: list[int] = [numbers.pop(0) for _ in range(q_metadata)]

    return {"children": children, "metadata": metadata}


def sum_metadata(node: TreeNode) -> int:
    """Recursively sums all metadata entries across every node in the tree.

    Args:
        node: The root TreeNode to start summing from.

    Returns:
        The total sum of all metadata values in this subtree.
    """
    total: int = sum(node["metadata"])
    for child in node["children"]:
        total += sum_metadata(child)
    return total


def do_part_1() -> bool:
    logger.info("Part 1")
    lines: list[str] = read_file("data/input.txt")
    numbers: list[int] = [int(x) for x in lines[0].split()]
    tree: TreeNode = parse_tree(numbers)
    total: int = sum_metadata(tree)
    logger.info(f"total: {total}")
    return 37439 == total
