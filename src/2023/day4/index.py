from global_utils.utils import read_file
from global_utils.logger import logger


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


def sum_of_worth(cards: list[tuple[set[int], set[int]]]) -> int:
    result = 0
    for winning, having in cards:
        intersection = winning.intersection(having)
        if len(intersection) == 0:
            continue
        result += 2 ** (len(intersection) - 1)
    return result


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
            if win_index > len(cards):
                break
            if cards_dict.get(win_index) is None:
                cards_dict[win_index] = 1
            cards_dict[win_index] += num_cards
            num_winned -= 1
            win_index += 1
    return total_cards


def do_part_1() -> bool:
    logger.info("Part 1")
    contents = read_file("input.txt")
    cards = get_cards(contents)
    return 28538 == sum_of_worth(cards)


def do_part_2() -> bool:
    logger.info(f"Part 2")
    contents = read_file("input.txt")
    cards = get_cards(contents)
    return 9425061 == total_cards_end_up(cards)


def main():
    logger.info("---- Day 4: Scratchcards ----")
    result_part_1 = do_part_1()
    assert (True == result_part_1)
    result_part_2 = do_part_2()
    assert (True == result_part_2)


if __name__ == "__main__":
    main()
