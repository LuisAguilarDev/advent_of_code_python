from global_utils.utils import read_file
from global_utils.logger import logger


def get_common_letters_that_differs_by_one_char(boxes) -> str:
    for box1 in boxes:
        for box2 in boxes:
            letters = ""
            diff = 0
            for c1, c2 in zip(box1, box2):
                if c1 == c2:
                    letters += c1
                else:
                    diff += 1
            if diff == 1:
                return letters


def do_part_2() -> bool:
    logger.info(f"Part 2")
    boxes = read_file("data/input.txt")
    common_letter_correct_boxes = get_common_letters_that_differs_by_one_char(
        boxes)
    logger.info(f"Letters: {common_letter_correct_boxes}")
    return "uqcidadzwtnhsljvxyobmkfyr" == common_letter_correct_boxes
