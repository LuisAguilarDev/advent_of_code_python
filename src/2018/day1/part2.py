from global_utils.utils import read_file
from global_utils.logger import logger


# python understand _ on large numbers and removes them and they improve readability for humans
def get_first_repeated_total(numbers) -> int:
    """
    Detects the first coincident value on a loop and returns it
    
    numbers is a list of numbers
    """
    if len(numbers) == 0:
        return 0
    seen = set([0])
    value = 0
    while True:
        for number in numbers:
            value += int(number)
            if value in seen:
                return value
            seen.add(value)

def do_part_2() -> bool:
    logger.info(f"Part 2")
    numbers = read_file("data/input.txt")
    repeated_total = get_first_repeated_total(numbers)
    logger.info(f"Repeated total: {repeated_total}")
    return 709 == repeated_total
