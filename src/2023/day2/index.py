import re
import math
from global_utils.utils import read_file
from global_utils.logger import logger

logger.info("---- Day 2: Cube Conundrum ----")

contents = read_file("input.txt")
sample_contents = read_file("sample.txt")

logger.info("Part 1")


def parse_input_games(lines: list[str]) -> list[list[list[str]]]:
    """
    Parse input lines into structured game data.
    ### games = [game,...,game]
    ### game = [step,...,step]
    ### step = [num,color,...,num,color]
    """
    game_list_colors = ["red", "blue", "green"]
    pattern = "(" + "|".join(game_list_colors) + "|" + "\d+)"
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


games_txt = """
Game 1: 3 blue, 4 red
"""
test_1 = "".join(parse_input_games(games_txt.splitlines())[0][0])
assert (test_1 == "3blue4red")


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


games = parse_input_games(contents)
valid_game = {"red": 12, "green": 13, "blue": 14}
sum_of_valid_games = sum_valid_games(games, valid_game)
logger.info(f"Sum of valid games: {sum_of_valid_games}")
assert (sum_of_valid_games == 2563)

logger.info("Part 2")


game_list_colors = ["red", "blue", "green"]


def get_minimum_pieces_for_game(game: list[str]) -> dict[str, int]:
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


result = get_product_of_minimum_pieces_for_all_games(games)
logger.info(f"Sum of products of minimum pieces for all games: {result}")

assert (result == 70768)
