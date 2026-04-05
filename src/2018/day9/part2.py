from collections import defaultdict

from global_utils.utils import read_file
from global_utils.logger import logger

from .part1 import parse_data


class DoublyLinkedList:
    def __init__(self):
        self.nxt = {0: 0}
        self.prv = {0: 0}
        self.current = 0

    def forward(self, steps: int) -> None:
        for _ in range(steps):
            self.current = self.nxt[self.current]

    def backward(self, steps: int) -> None:
        for _ in range(steps):
            self.current = self.prv[self.current]

    def insert(self, marble: int) -> None:
        """Insert marble after current, then set current to it."""
        self.forward(1)
        nxt_node = self.nxt[self.current]
        self.nxt[self.current] = marble
        self.nxt[marble] = nxt_node
        self.prv[marble] = self.current
        self.prv[nxt_node] = marble
        self.current = marble

    def remove(self) -> int:
        """Remove current node, advance current to next, return removed value."""
        self.backward(7)
        removed = self.current
        p, n = self.prv[removed], self.nxt[removed]
        self.nxt[p] = n
        self.prv[n] = p
        del self.nxt[removed], self.prv[removed]
        self.current = n
        return removed


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
