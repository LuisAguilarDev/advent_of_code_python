import os
import re
import math

file_path = os.path.join(os.path.dirname(__file__), "day2.txt")
sample_path = os.path.join(os.path.dirname(__file__), "day2.sample.txt")
with open(file_path, "r") as file:
    contents = file.read().splitlines()
with open(sample_path, "r") as file:
    sample_contents = file.read().splitlines()

# Part 1

# Get high score for each color by game
list_colors = ["red", "blue", "green"]
valid_numbers = {"red": 12, "green": 13, "blue": 14}

sum_valid_games = 0
for ID, line in enumerate(contents, start=1):
    # list is ordered and goes from 1 to 100
    match = line.split(":")  # Game ID, Game Info
    game_info = match[1].strip().split(";")
    for step in game_info:
        step = step.strip()
        bad_game = False
        if step:
            # Extract color and score
            pattern = "(" + "|".join(list_colors) + "|" + "\d+)"
            p = re.compile(pattern)
            score_matches = re.findall(p, step)
            # Num, Color, ...., Num, Color
            # traverse in pairs
            for i in range(0, len(score_matches), 2):
                color = score_matches[i + 1]
                num = int(score_matches[i])
                if num > valid_numbers[color]:
                    bad_game = True
                    break
            if bad_game:
                break
    else:
        sum_valid_games += ID

assert (sum_valid_games == 2563)

# Part 2

response = 0
for ID, line in enumerate(contents, start=1):
    match = line.split(":")  # Game ID, Game Info
    game_info = match[1].strip().split(";")
    minimum_pieces = {"red": 0, "green": 0, "blue": 0}
    for step in game_info:
        step = step.strip()
        if step:
            pattern = "(" + "|".join(list_colors) + "|" + "\d+)"
            p = re.compile(pattern)
            score_matches = re.findall(p, step)
            for i in range(0, len(score_matches), 2):
                color = score_matches[i + 1]
                num = int(score_matches[i])
                print(color, num)
                minimum_pieces[color] = max(minimum_pieces[color], num)
    response += math.prod(minimum_pieces.values())

print(response)
