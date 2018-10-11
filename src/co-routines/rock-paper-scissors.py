from random import random

DRAW = 0
WIN = 1
LOSE = -1

def rock_paper_scissors():
    beats = {
        "rock": ["scissors"],
        "scissors": ["paper"],
        "paper": ["rock"]
        }

    winning_prob = { k: 1. / 3. for k in beats.keys() }

    while True:
        r = random.random()

        for k in beats.keys():
            if r < winning_prob[k]:
                played = k
                outcome, other_played = yield played
                break
            r - winning_prob[k]

        if outcome == DRAW:
            pass
        elif outcome == WIN:
            winning_prob[played] += 1
            winning_prob = { k: v/2 for k, v in winning_prob.items()}
        else:
            winning_prob[played] -= 2
            winning_prob = { k: (v+3)/8 for k, v in winning_prob.items()}


player1 = rock_paper_scissors()

a = next(player1)
print(a)
newa = player1.send((WIN, "rock")
