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

def do_part_1() -> bool:
    logger.info("Part 1")
    polymer_list = read_file("data/input.txt")
    reacted_polymer = get_reacted_polymer(polymer_list[0])
    logger.info(f"Largo: {len(reacted_polymer)}")
    return 10368 == len(reacted_polymer)
