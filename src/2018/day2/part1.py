from global_utils.utils import read_file
from global_utils.logger import logger


def get_checksum(boxes) -> int:
    """
    Returns the checksum for the list of box IDs
    
    boxes is a list of box ID strings like "abbcde"
    """
    count_2 = 0
    count_3 = 0
    for box in boxes:
        chars_count = dict()
        for char in box:
            chars_count[char] = chars_count.get(char, 0) + 1
        has_2 = False
        has_3 = False
        for count in chars_count.values():
            if count == 2:
                has_2 = True
            elif count == 3:
                has_3 = True
        if has_2:
            count_2 += 1
        if has_3:
            count_3 += 1
    return count_2 * count_3

def do_part_1() -> bool:
    logger.info("Part 1")
    boxes = read_file("data/input.txt")
    # no transformation required
    checksum = get_checksum(boxes)
    logger.info(f"Checksum: {checksum}")
    return 9139 == checksum