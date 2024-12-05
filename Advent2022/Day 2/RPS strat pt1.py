'''
A for Rock          X for Rock      (1 point)
B for Paper         Y for Paper     (2 points)
C for Scissors      Z for Scissors  (3 points)

The score for a single round is the score for the shape you selected 
plus the score for the outcome of the round. 
(0 if you lost, 3 if the round was a draw, and 6 if you won).
'''
def round_played(round):
    if round[1] == "A":
        if round[0] == "A":     # Draw
            return 4
        elif round[0] == "B":   # Lost
            return 1
        elif round[0] == "C":   # Win
            return 7
    if round[1] == "B":
        if round[0] == "A":     # Win
            return 8
        elif round[0] == "B":   # Draw
            return 5
        elif round[0] == "C":   # Lost
            return 2
    if round[1] == "C":
        if round[0] == "A":     # Lost
            return 3
        elif round[0] == "B":   # Win
            return 9
        elif round[0] == "C":   # Draw
            return 6

def traductor(hand):
    if hand == "X":
        return "A"
    elif hand == "Y":
        return "B"
    else:
        return "C"

strategy_guide = open("Day 2\input.txt", "r")
total_points = 0

for round in strategy_guide.read().split("\n"):
    if round == '':
        break
    round = round.split(" ")
    round[1] = traductor(round[1])
    total_points += round_played(round)
    
print(total_points)
    
    