from global_utils.utils import read_file
from global_utils.logger import logger


def parse_data(contents):
    games = list()
    for line in contents:
        game_str = line.split()
        games.append((game_str[0], int(game_str[1])))
    return games


def total_winings(games):
    total = 0
    games = sort_games_by_strength(games)
    for i, game in enumerate(games, start=1):
        _, bid = game
        total += (bid * i)
    return total


def sort_games_by_strength(games):
    all_high_card_hands = []
    one_pair_hands = []
    two_pair_hands = []
    three_of_a_kind_hands = []
    full_house_hands = []
    four_of_a_kind_hands = []
    five_of_a_kind_hands = []
    for game in games:
        hand_str, _ = game
        hand = list(hand_str)
        counts = {card: hand.count(card) for card in set(hand)}
        max_count = max(counts.values())
        if max_count == 5:
            five_of_a_kind_hands.append(game)
        elif max_count == 4:
            four_of_a_kind_hands.append(game)
        elif max_count == 3:
            if 2 in counts.values():
                full_house_hands.append(game)
            else:
                three_of_a_kind_hands.append(game)
        elif max_count == 2:
            pair_counts = list(counts.values()).count(2)
            if pair_counts == 2:
                two_pair_hands.append(game)
            else:
                one_pair_hands.append(game)
        else:
            all_high_card_hands.append(game)

    # Sort each category by hand strength
    all_high_card_hands.sort(
        key=get_hand_strength)
    one_pair_hands.sort(key=get_hand_strength)
    two_pair_hands.sort(key=get_hand_strength)
    three_of_a_kind_hands.sort(key=get_hand_strength)
    full_house_hands.sort(key=get_hand_strength)
    four_of_a_kind_hands.sort(key=get_hand_strength)
    five_of_a_kind_hands.sort(key=get_hand_strength)

    return (all_high_card_hands +
            one_pair_hands +
            two_pair_hands +
            three_of_a_kind_hands +
            full_house_hands +
            four_of_a_kind_hands +
            five_of_a_kind_hands
            )


def get_hand_strength(hand_tuple):
    strength_list = ["2", "3", "4", "5", "6",
                     "7", "8", "9", "T", "J", "Q", "K", "A"]
    hand_str, _ = hand_tuple
    strength_dict = {card: index for index, card in enumerate(strength_list)}
    return [strength_dict[card] for card in hand_str]


def sort_games_by_strength_with_jokers(games):
    all_high_card_hands = []
    one_pair_hands = []
    two_pair_hands = []
    three_of_a_kind_hands = []
    full_house_hands = []
    four_of_a_kind_hands = []
    five_of_a_kind_hands = []
    for game in games:
        hand_str, _ = game
        hand = list(hand_str)
        counts = {card: hand.count(card) for card in set(hand)}
        if "J" in counts:
            jokers = counts["J"]
            if jokers < 5:
                del counts["J"]
                # Find the card with the highest current count
                max_card = max(counts, key=counts.get)
                counts[max_card] += jokers
            else:
                # Case for "JJJJJ" - effectively 5 Aces
                counts = {"A": 5}
        max_count = max(counts.values())
        if max_count == 5:
            five_of_a_kind_hands.append(game)
        elif max_count == 4:
            four_of_a_kind_hands.append(game)
        elif max_count == 3:
            if 2 in counts.values():
                full_house_hands.append(game)
            else:
                three_of_a_kind_hands.append(game)
        elif max_count == 2:
            pair_counts = list(counts.values()).count(2)
            if pair_counts == 2:
                two_pair_hands.append(game)
            else:
                one_pair_hands.append(game)
        else:
            all_high_card_hands.append(game)

    # Sort each category by hand strength
    all_high_card_hands.sort(
        key=get_hand_strength_part_2)
    one_pair_hands.sort(key=get_hand_strength_part_2)
    two_pair_hands.sort(key=get_hand_strength_part_2)
    three_of_a_kind_hands.sort(key=get_hand_strength_part_2)
    full_house_hands.sort(key=get_hand_strength_part_2)
    four_of_a_kind_hands.sort(key=get_hand_strength_part_2)
    five_of_a_kind_hands.sort(key=get_hand_strength_part_2)

    return (all_high_card_hands +
            one_pair_hands +
            two_pair_hands +
            three_of_a_kind_hands +
            full_house_hands +
            four_of_a_kind_hands +
            five_of_a_kind_hands
            )


def get_hand_strength_part_2(hand_tuple):
    strength_list = ["J", "2", "3", "4", "5", "6",
                     "7", "8", "9", "T", "Q", "K", "A"]
    hand_str, _ = hand_tuple
    strength_dict = {card: index for index, card in enumerate(strength_list)}
    return [strength_dict[card] for card in hand_str]


def total_winings_part_2(games):
    total = 0
    games = sort_games_by_strength_with_jokers(games)
    for i, game in enumerate(games, start=1):
        _, bid = game
        total += (bid * i)
    return total


def do_part_1() -> bool:
    logger.info("Part 1")
    contents = read_file("input.txt")
    games = parse_data(contents)
    return 247823654 == total_winings(games)


def do_part_2() -> bool:
    logger.info(f"Part 2")
    contents = read_file("input.txt")
    games = parse_data(contents)
    return 245461700 == total_winings_part_2(games)


def main():
    logger.info("---- Day 7: Camel Cards ----")
    result_part_1 = do_part_1()
    assert (True == result_part_1)
    result_part_2 = do_part_2()
    assert (True == result_part_2)


if __name__ == "__main__":
    main()
