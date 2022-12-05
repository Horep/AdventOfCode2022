file1 = open('RPS.txt')
Lines = file1.readlines()
Lines = [line.strip() for line in Lines]
EnemyPlay = [Game[0] for Game in Lines]
MyPlay = [Game[2] for Game in Lines]
print(EnemyPlay)
print(MyPlay)

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

myScore = 0
for i in range(len(EnemyPlay)):
    myScore += do_game(EnemyPlay[i],MyPlay[i]) + give_value(MyPlay[i])

print(myScore)