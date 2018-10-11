from random import random

DRAW = 0
WIN = 1
LOSE = -1

beats = {
        "rock": ["scissors"],
        "scissors": ["paper"],
        "paper": ["rock"]
    }

def rock_paper_scissors():

    winning_prob = { k: 1. / 3. for k in beats.keys() }

    while True:
        r = random()
        print(winning_prob)
        for k in beats.keys():
            if r < winning_prob[k]:
                played = k
                outcome, other_played = yield played
                break
            r -= winning_prob[k]

        if outcome == DRAW:
            pass
        elif outcome == WIN:
            winning_prob[played] += 1
            winning_prob = { k: v/2 for k, v in winning_prob.items()}
        else:
            winning_prob[played] -= 2
            winning_prob = { k: (v+3)/8 for k, v in winning_prob.items()}


player1 = rock_paper_scissors()
player2 = rock_paper_scissors()

a = next(player1)
b = next(player2)

for i in range(10):
    print(a, b)
    
    if a in beats[b]:
        result = WIN
        a, b = player1.send((WIN, b)), player2.send((LOSE, a))
    elif b in beats[a]:
        result = LOSE
        a, b = player1.send((LOSE, b)), player2.send((WIN, a))
    else:
        result = DRAW
        a, b = player1.send((result, b)), player2.send((result, a))
        
