from global_utils.utils import read_file
from global_utils.logger import logger
from ._part1 import parse_tree, TreeNode


def node_value(node: TreeNode) -> int:
    """Recursively computes the value of a node in the parsed tree.

    - If a node has no children, its value is the sum of its metadata.
    - If a node has children, each metadata entry is a 1-based index into the
      children list. The node's value is the sum of the referenced children's values.
      Out-of-range indices are skipped (contribute 0).

    Args:
        node: The TreeNode to compute the value for.

    Returns:
        The computed value of this node.
    """
    if not node["children"]:
        return sum(node["metadata"])

    children: list[TreeNode] = node["children"]
    total: int = 0
    for index in node["metadata"]:
        if 1 <= index <= len(children):
            total += node_value(children[index - 1])

    return total


def do_part_2() -> bool:
    logger.info("Part 2")
    lines: list[str] = read_file("data/input.txt")
    numbers: list[int] = [int(x) for x in lines[0].split()]
    tree: TreeNode = parse_tree(numbers)
    total: int = node_value(tree)
    logger.info(f"total: {total}")
    return 20815 == total
