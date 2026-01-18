from global_utils.utils import read_file
from global_utils.logger import logger


# python understand _ on large numbers and removes them and they improve readability for humans
def get_first_repeated_total(numbers, max_cycles=1_000_000) -> int:
    """
    Detects the first coincident value on a loop and returns it
    
    numbers is a list of numbers
    max_cycles is the max number of iterations to avoid an infinite loop if no coincident number is found.
    """
    if len(numbers) == 0:
        return 0
    seen = set([0])
    total = 0
    for _ in range(max_cycles):
        for number in numbers:
            total += int(number)
            if total in seen:
                return total
            seen.add(total)

def do_part_2() -> bool:
    logger.info(f"Part 2")
    numbers = read_file("data/input.txt")
    repeated_total = get_first_repeated_total(numbers)
    logger.info(f"Repeated total: {repeated_total}")
    return 709 == repeated_total
