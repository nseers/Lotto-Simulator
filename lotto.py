import random
import json

TICKETS_DRAWING = 10000

white_balls = range(1, 71)
gold_balls = range(1, 26)

winnings = 0
total_tickets = 0
num_drawings = 0
years = 0
results = {
    "5+M": 0,
    "5": 0,
    "4+M": 0,
    "4": 0,
    "3+M": 0,
    "3": 0,
    "2+M": 0,
    "2": 0,
    "1+M": 0,
    "1": 0,
    "0+M": 0,
    "0": 0,
}


def amount_won(my_nums, winning_nums):

    white_matchs = len(my_white_nums.intersection(win_white_num))
    gold_match = my_nums["gold"] == winning_nums["gold"]
    won = 0

    if white_matchs == 5:
        if gold_match:
            print("You won the Jackpot!!!")
            won = 1_000_000_000
            results["5+M"] += 1
        else:
            print("You got 5/6!!!")
            won = 1_000_000
            results["5"] += 1
    elif white_matchs == 4:
        if gold_match:
            won = 10_000
            results["4+M"] += 1
        else:
            won = 500
            results["4"] += 1
    elif white_matchs == 3:
        if gold_match:
            won = 200
            results["3+M"] += 1
        else:
            won = 10
            results["3"] += 1
    elif white_matchs == 2:
        if gold_match:
            won = 10
            results["2+M"] += 1
        else:
            results["2"] += 1
    elif white_matchs == 1:
        if gold_match:
            won = 4
            results["1+M"] += 1
        else:
            results["1"] += 1
    else:
        if gold_match:
            won = 2
            results["0+M"] += 1
        else:
            results["0"] += 1
    return won


while True:
    jackpot_won = False
    num_drawings += 1
    win_white_num = set(random.sample(white_balls, k=5))
    win_gold_num = random.choice(gold_balls)
    winning_nums = {"white": win_white_num, "gold": win_gold_num}

    for n in range(TICKETS_DRAWING):
        my_white_nums = set(random.sample(white_balls, k=5))
        my_gold_num = random.choice(gold_balls)
        my_nums = {"white": my_white_nums, "gold": my_gold_num}

        won_amt = amount_won(my_nums, winning_nums)
        winnings += won_amt
        total_tickets += 1

        if won_amt == 1_000_000_000:
            jackpot_won = True
            break

    if jackpot_won:
        break

    if num_drawings % 104 == 0:
        years += 1
        print(f"Year: {years}")

print(f"Winnings: {winnings}")
print(f"Cost: {total_tickets * 2}")
print(json.dumps(results, indent=3))
