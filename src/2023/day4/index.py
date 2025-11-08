from global_utils.utils import read_file
from global_utils.logger import logger

logger.info("---- Day 4: Scratchcards ----")

contents = read_file("input.txt")
sample_contents = read_file("sample.txt")

logger.info("Part 1")


def get_cards(contents: list[str]):
    cards = list()
    for line in contents:
        pairs = line.split(":")[1].split("|")
        winning_list = pairs[0].strip().split()
        having_list = pairs[1].strip().split()
        winning = set(map(int, winning_list))
        having = set(map(int, having_list))
        cards.append((winning, having))
    return cards


cards = get_cards(contents)


def sum_of_worth(cards: list[tuple[set[int], set[int]]]) -> int:
    result = 0
    for winning, having in cards:
        intersection = winning.intersection(having)
        if len(intersection) == 0:
            continue
        result += 2 ** (len(intersection) - 1)
    return result


result = sum_of_worth(cards)
logger.info(f"Total worth of all scratchcards is {result}")
assert (28538 == result)

logger.info("Part 2")


def total_cards_end_up(cards: list[tuple[set[int], set[int]]]) -> int:
    cards_dict = dict()  # dict<card_num, num_of_cards>
    total_cards = 0

    for num, cards_info in enumerate(cards, start=1):
        card_num = num
        num_cards = cards_dict.get(card_num, 1)
        total_cards += num_cards
        winning, having = cards_info
        num_winned = len(winning.intersection(having))
        win_index = card_num + 1
        while num_winned > 0:
            if win_index > len(contents):
                break
            if cards_dict.get(win_index) is None:
                cards_dict[win_index] = 1
            cards_dict[win_index] += num_cards
            num_winned -= 1
            win_index += 1
    return total_cards


result = total_cards_end_up(cards)
logger.info(f"Total number of scratchcards end up is {result}")
assert (result == 9425061)
