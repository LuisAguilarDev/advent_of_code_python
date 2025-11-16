import re
import math
from global_utils.utils import read_file
from global_utils.logger import logger


def parse_input_games(lines: list[str]) -> list[list[list[str]]]:
    """
    Parse input lines into structured game data.
    ### games = [game,...,game]
    ### game = [step,...,step]
    ### step = [num,color,...,num,color]
    """
    pattern = "(" + "red|blue|green" + "|" + "\d+)"
    p = re.compile(pattern)
    games = list()
    for line in lines:
        if not line.strip():
            continue
        match = line.split(":")  # Game ID, Game Info
        game_info = match[1].strip().split(";")
        game = list()
        for step in game_info:
            step = step.strip()
            if step:
                score_matches = re.findall(p, step)
                game.append(score_matches)
        games.append(game)
    return games


def is_valid_game(step: list[str], valid_game: dict[str, int]) -> bool:
    # traverse in pairs
    for i in range(0, len(step), 2):
        color = step[i + 1]
        num = int(step[i])
        if num > valid_game[color]:
            return False
    return True


def sum_valid_games(games: list[list[list[str]]], valid_game: dict[str, int]) -> int:
    sum = 0
    for ID, game in enumerate(games, start=1):
        for step in game:
            is_valid = is_valid_game(step, valid_game)
            if not is_valid:
                break
        else:
            sum += ID

    return sum


def get_minimum_pieces_for_game(game: list[str]) -> dict[str, int]:
    game_list_colors = ["red", "blue", "green"]
    minimum_pieces = {color: 0 for color in game_list_colors}
    # traverse in pairs
    for step in game:
        for i in range(0, len(step), 2):
            color = step[i + 1]
            num = int(step[i])
            minimum_pieces[color] = max(minimum_pieces[color], num)
    return minimum_pieces


def get_product_of_minimum_pieces_for_all_games(games: list[list[list[str]]]) -> int:
    sum_product = 0
    for game in games:
        c_minimum_pieces = get_minimum_pieces_for_game(game)
        sum_product += math.prod(c_minimum_pieces.values())
    return sum_product


def do_part_1() -> bool:
    logger.info("Part 1")
    contents = read_file("input.txt")
    games = parse_input_games(contents)
    valid_game = {"red": 12, "green": 13, "blue": 14}
    return 2563 == sum_valid_games(games, valid_game)


def do_part_2() -> bool:
    logger.info(f"Part 2")
    contents = read_file("input.txt")
    games = parse_input_games(contents)
    return 70768 == get_product_of_minimum_pieces_for_all_games(games)


def main():
    logger.info("---- Day 2: Cube Conundrum ----")
    result_part_1 = do_part_1()
    assert (True == result_part_1)
    result_part_2 = do_part_2()
    assert (True == result_part_2)


if __name__ == "__main__":
    main()
