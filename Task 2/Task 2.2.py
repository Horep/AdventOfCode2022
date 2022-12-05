file1 = open('RPS.txt')
Lines = file1.readlines()
Lines = [line.strip() for line in Lines]
EnemyPlay = [Game[0] for Game in Lines]
Outcome = [Game[2] for Game in Lines]
print(EnemyPlay)
print(Outcome)

def outcome_to_myplay(U,V):
    if U=='A':  # rock
        if V=='X':  # need to lose, scissors
            return 'Z'
        elif V=='Y':  # need to draw, rock
            return 'X'
        elif V=='Z':  # need to win, paper
            return 'Y'
    elif U=='B':  # paper
        if V=='X':  # need to lose, rock
            return 'X'
        elif V=='Y':  # need to draw, paper
            return 'Y'
        elif V=='Z':  # need to win, scissors
            return 'Z'
    elif U=='C':  # scissors
        if V=='X':  # need to lose, paper
            return 'Y'
        elif V=='Y':  # need to draw, scissors
            return 'Z'
        elif V=='Z':  # need to win, rock
            return 'X'

def do_game(U,V):
    if U=='A' and V=='X' or U=='B' and V=='Y' or U=='C' and V=='Z':  # draw
        return 3
    elif U == 'A' and V == 'Z' or U == 'B' and V == 'X' or U == 'C' and V == 'Y':  # I lose
        return 0
    elif U == 'A' and V == 'Y' or U == 'B' and V == 'Z' or U == 'C' and V == 'X':  # I win
        return 6
    else:
        print("Bad Input do game")

def give_value(V):
    if V=='X':
        return 1
    elif V=='Y':
        return 2
    elif V=='Z':
        return 3
    else:
        print("Bad Input give value")

MyPlay = []
for i in range(len(EnemyPlay)):
    MyPlay.append(outcome_to_myplay(EnemyPlay[i],Outcome[i]))
print(MyPlay)
myScore = 0
for i in range(len(EnemyPlay)):
    myScore += do_game(EnemyPlay[i],MyPlay[i]) + give_value(MyPlay[i])

print(myScore)