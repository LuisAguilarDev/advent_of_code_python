from collections import defaultdict
from global_utils.utils import read_file
from global_utils.logger import logger

from .part1 import parse_data

class Node:
    __slots__ = ("val", "prv", "nxt")

    def __init__(self, val: int):
        self.val = val
        self.prv: "Node" = self
        self.nxt: "Node" = self


class DoublyLinkedList:
    def __init__(self):
        self.current = Node(0)  # sentinel / starting node

    def forward(self, steps: int) -> None:
        for _ in range(steps):
            self.current = self.current.nxt

    def backward(self, steps: int) -> None:
        for _ in range(steps):
            self.current = self.current.prv

    def insert(self, val: int) -> None:
        """Move one step forward, then insert a new node after current."""
        self.forward(1)
        node = Node(val)
        nxt = self.current.nxt
        self.current.nxt = node
        node.prv = self.current
        node.nxt = nxt
        nxt.prv = node
        self.current = node

    def remove(self) -> int:
        """Remove current node, advance current to next, return its value."""
        self.backward(7)
        node = self.current
        node.prv.nxt = node.nxt
        node.nxt.prv = node.prv
        self.current = node.nxt
        return node.val


def solve(num_players: int, last_marble: int) -> int:
    dll = DoublyLinkedList()
    scores = defaultdict(int)

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            player = (marble - 1) % num_players
            scores[player] += marble
            scores[player] += dll.remove()
        else:
            dll.insert(marble)

    return max(scores.values()) if scores else 0


def do_part_2() -> bool:
    logger.info("Part 2")
    lines: list[str] = read_file("data/input.txt")
    num_players, last_marble = parse_data(lines[0])
    result: int = solve(num_players, last_marble * 100)
    logger.info(f"result: {result}")
    return 3066307353 == result
