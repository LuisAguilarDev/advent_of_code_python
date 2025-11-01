import os

file_path = os.path.join(os.path.dirname(__file__), "input.txt")
sample_path = os.path.join(os.path.dirname(__file__), "sample.txt")
with open(file_path, "r") as file:
    contents = file.read().splitlines()
with open(sample_path, "r") as file:
    sample_contents = file.read().splitlines()

result = 0
for line in contents:
    pairs = line.split(":")[1].split("|")
    winning_list = pairs[0].strip().split()
    having_list = pairs[1].strip().split()
    winning = set(map(int, winning_list))
    having = set(map(int, having_list))
    # intersection of winning and having
    intersection = winning.intersection(having)
    if len(intersection) == 0:
        continue
    result += 2 ** (len(intersection) - 1)

assert (28538 == result)

# Part 2
cards = dict()  # dict<card_num, num_of_cards>
total_cards = 0

for num, line in enumerate(contents, start=1):
    card_num = num
    num_cards = cards.get(card_num, 1)
    total_cards += num_cards
    pairs = line.split(":")[1].split("|")
    winning_list = pairs[0].strip().split()
    having_list = pairs[1].strip().split()
    winning = set(map(int, winning_list))
    having = set(map(int, having_list))
    num_winned = len(winning.intersection(having))
    win_index = card_num + 1
    while num_winned > 0:
        if win_index > len(contents):
            break
        if cards.get(win_index) is None:
            cards[win_index] = 1
        cards[win_index] += num_cards
        num_winned -= 1
        win_index += 1

assert (total_cards == 9425061)
