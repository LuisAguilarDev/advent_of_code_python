from global_utils.utils import read_file
from global_utils.logger import logger


def get_reacted_polymer(polymer):
    stack = []
    for unit in polymer:
        if stack and stack[-1].swapcase() == unit:
            stack.pop()    # reaccionan → elimina el tope
        else:
            stack.append(unit)  # no reacciona → apila
    return "".join(stack)


def get_shortest_polymer(polymer) -> int:
    units = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    best = float("inf")
    for unit in units:
        c_polymer = polymer.replace(unit, "").replace(unit.lower(), "")
        f_polymer = get_reacted_polymer(c_polymer)
        largo = len(f_polymer)
        if largo < best:
            best = largo
    return best


    
def do_part_2() -> bool:
    logger.info("Part 2")
    polymer_list = read_file("data/input.txt")
    reacted_polymer = get_shortest_polymer(polymer_list[0])
    logger.info(f"Largo: {reacted_polymer}")
    return 4122 == reacted_polymer
